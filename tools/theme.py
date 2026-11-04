"""Check, build and preview the icon theme with calibre's own tools.

Run it with calibre's Python:
    tools\\theme.cmd <command>          (Windows)
    calibre-debug tools/theme.py <command>

Commands:
    check     Compare images/ with the icons calibre uses and with the README tables.
    render    Render the icons drawn for this project (src/*.svg) to 256px PNGs in images/.
    build    Package the theme as a calibre icon theme .zip in dist/.
    preview   Close calibre, build and install the theme, then start calibre again.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(globals().get('__file__') or sys.argv[0])))
IMAGES = os.path.join(ROOT, 'images')
SRC = os.path.join(ROOT, 'src')
ICON_SIZE = 256
DIST = os.path.join(ROOT, 'dist')
README = os.path.join(ROOT, 'README.md')
CHANGELOG = os.path.join(ROOT, 'CHANGELOG.md')
METADATA = os.path.join(IMAGES, 'metadata.json')
CALIBRE_DIR = os.path.dirname(sys.executable)
PALETTES = ('any', 'light', 'dark')


def canonical(name):
    # calibre renders .svg icons to .png and treats -for-dark/light-theme files as variants of one icon
    base, ext = os.path.splitext(name)
    for suffix in ('-for-dark-theme', '-for-light-theme'):
        if base.endswith(suffix):
            base = base[:-len(suffix)]
    return base + ('.png' if ext.lower() == '.svg' else ext.lower())


def list_icons(folder):
    names = set()
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(('.png', '.svg', '.jpg', '.jpeg')):
                names.add(os.path.relpath(os.path.join(root, f), folder).replace(os.sep, '/'))
    return names


def read_theme(images_copy):
    # calibre's reader writes .png renders of .svg icons into the folder it reads, so only ever pass it a copy
    from calibre.gui2.icon_theme import read_theme_from_folder
    return read_theme_from_folder(images_copy)


def copy_images(tmp):
    dest = os.path.join(tmp, 'images')
    shutil.copytree(IMAGES, dest)
    return dest


def releases():
    with open(CHANGELOG, encoding='utf-8') as f:
        return re.findall(r'^## \[?(\d+\.\d+\.\d+)', f.read(), re.MULTILINE)


def readme_rows():
    rows, table = [], None
    with open(README, encoding='utf-8') as f:
        for line in f:
            if line.startswith('### '):
                table = line[4:].strip()
            m = re.search(r'!\[\]\(images/([^)]+)\)', line)
            if m and line.startswith('|'):
                rows.append((m.group(1), table))
    return rows


def check():
    from calibre.utils.resources import get_path as P
    builtin = {canonical(n) for n in list_icons(P('images', allow_user_override=False))}
    ours = list_icons(IMAGES)
    ours_canonical = {canonical(n) for n in ours}
    errors = []

    with tempfile.TemporaryDirectory() as tmp:
        report = read_theme(copy_images(tmp))
    for name, err in sorted(report.bad.items()):
        errors.append(f'Broken image: {name} ({err})')

    missing = sorted(builtin - ours_canonical)
    unused = sorted(n for n in ours if canonical(n) not in builtin)

    rows = readme_rows()
    seen = {}
    for name, table in rows:
        if name in seen:
            errors.append(f'README: {name} is listed in both "{seen[name]}" and "{table}"')
        seen[name] = table
        if name not in ours:
            errors.append(f'README: {name} is listed in "{table}" but the file does not exist')
    # calibre itself ships a few tmp*.png files in its images folder, they are not real icons
    top_level = sorted(n for n in ours if '/' not in n and not n.startswith('tmp'))
    not_in_readme = [n for n in top_level if n not in seen]

    from calibre.constants import __version__
    print(f'Icons in images/: {len(ours)} files, calibre {__version__} uses {len(builtin)} icons')
    section('calibre icons this theme does not have (calibre shows its default icon)', missing)
    section('Icons calibre does not use', unused)
    section('Icons in images/ that have no row in the README tables', not_in_readme)
    section('Errors', errors)
    if not errors:
        print('\nNo errors.')
    return not errors


def section(title, items):
    if items:
        print(f'\n{title} ({len(items)}):')
        for item in items:
            print('  ' + item)


def render():
    from qt.core import QApplication, QImage, QPainter, QRectF, QSvgRenderer, Qt
    app = QApplication.instance() or QApplication([])  # noqa: F841
    for name in sorted(os.listdir(SRC)):
        if not name.endswith('.svg'):
            continue
        renderer = QSvgRenderer(os.path.join(SRC, name))
        if not renderer.isValid():
            raise SystemExit(f'Cannot read src/{name}')
        img = QImage(ICON_SIZE, ICON_SIZE, QImage.Format.Format_ARGB32_Premultiplied)
        img.fill(Qt.GlobalColor.transparent)
        p = QPainter(img)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        renderer.render(p, QRectF(0, 0, ICON_SIZE, ICON_SIZE))
        p.end()
        out = name[:-4] + '.png'
        if not img.save(os.path.join(IMAGES, out)):
            raise SystemExit(f'Cannot write images/{out}')
        print(f'src/{name} -> images/{out}')


def build(save=True):
    from calibre.gui2.icon_theme import create_themeball
    versions = releases()
    if not versions:
        raise SystemExit('CHANGELOG.md has no released version yet')
    version = versions[0]
    with open(METADATA, encoding='utf-8') as f:
        metadata = json.load(f)
    # calibre needs a whole number as the theme version; use the release count so every release is higher
    metadata['version'] = len(versions)

    with tempfile.TemporaryDirectory() as tmp:
        images = copy_images(tmp)
        with open(os.path.join(images, 'metadata.json'), 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        report = read_theme(images)
        if report.bad:
            raise SystemExit('Broken images, run "check" for details: ' + ', '.join(sorted(report.bad)))
        print(f'Building {metadata["title"]} {version} ({len(report.name_map)} icons)...')
        raw, prefix, icon_zip = create_themeball(report, metadata)

    if not save:
        return metadata, icon_zip
    os.makedirs(DIST, exist_ok=True)
    dest = os.path.join(DIST, f'{prefix}-{version}.zip')
    with open(dest, 'wb') as f:
        f.write(raw)
    print(f'Saved {os.path.relpath(dest, ROOT)} ({len(raw) // 1024} KB)')
    return metadata, icon_zip


def calibre_running():
    out = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq calibre.exe', '/NH'],
                         capture_output=True, text=True, errors='replace').stdout
    return 'calibre.exe' in out.lower()


def preview():
    calibre = os.path.join(CALIBRE_DIR, 'calibre.exe')
    if calibre_running():
        print('Closing calibre...')
        subprocess.run([calibre, '--shutdown-running-calibre'])
        for _ in range(60):
            if not calibre_running():
                break
            time.sleep(0.5)
        else:
            raise SystemExit('calibre did not close, close it by hand and run preview again')

    try:
        install_preview()
    finally:
        # start calibre again even if the install failed, so it is never left closed
        print('Starting calibre...')
        flags = getattr(subprocess, 'DETACHED_PROCESS', 0) | getattr(subprocess, 'CREATE_NEW_PROCESS_GROUP', 0)
        subprocess.Popen([calibre], creationflags=flags, close_fds=True,
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def install_preview():
    # build in memory only: dist/ keeps the release files
    metadata, icon_zip = build(save=False)

    from calibre.gui2 import icon_resource_manager
    from calibre.gui2.icon_theme import install_icon_theme
    from qt.core import QResource
    # calibre's startup code (run inside this script too) keeps the installed theme files open,
    # and Windows cannot overwrite an open file, so release them first
    for path in list(icon_resource_manager.registered_user_resource_files):
        QResource.unregisterResource(path)
    icon_resource_manager.registered_user_resource_files = ()
    palette = metadata.get('color_palette', 'any')
    icon_zip.seek(0)
    install_icon_theme(metadata, icon_zip, icon_resource_manager.user_theme_resource_file(palette), palette)
    print(f'Installed the theme in calibre for "{palette}" color palette')
    if palette == 'any':
        # a theme installed only for light or dark mode would win over this one, so set it aside
        for other in ('light', 'dark'):
            path = icon_resource_manager.user_theme_resource_file(other)
            if os.path.exists(path):
                os.replace(path, path + '.bak')
                print(f'Moved the old {other} mode theme aside: {path}.bak')


def main():
    commands = {'check': check, 'render': render, 'build': build, 'preview': preview}
    args = [a for a in sys.argv[1:] if a != '--']
    if len(args) != 1 or args[0] not in commands:
        print(__doc__)
        raise SystemExit(1)
    result = commands[args[0]]()
    if result is False:
        raise SystemExit(1)


main()
