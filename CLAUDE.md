# Instructions for Claude

## Icon sources

The theme only uses two kinds of icons:

- icons from the Ubuntu Yaru icon theme (Yaru-Blue version), as they are or customized;
- icons drawn for this project in Yaru style.

Never add icons from other themes, websites or icon packs, even if their license allows it. Everything in the theme is licensed CC BY-SA 4.0 (see the License section in `README.md`), so every new icon must be shareable under it.

Use one of these values in the README "Source" column for replaced icons:

- `Yaru-Blue`
- `Yaru-Blue (customized)`
- `Mark Ingrem` (drawn for this project)

## Drawing icons

- Every icon drawn for this project has its source in `src/<icon-name>.svg`. `tools\theme.cmd render` turns it into `images/<icon-name>.png` (256×256). Never edit those PNG files by hand.
- Read `docs/yaru-style.md` before drawing. Yaru's general design drives every icon: match the closest Yaru icons of the same kind, build from Yaru's sources and templates, use Yaru's palette. If Yaru already has the icon, use Yaru's PNG. The guide's rules for a family of icons (such as text formatting) apply only to that family.
- When it isn't clear which approach fits an icon (which Yaru icons to match, Yaru's symbol or calibre's idea, color or neutral, code or Illustrator), ask the user before drawing and show the options.
- Add to the guide when a new rule is agreed with the user.
- Simple icons are written as SVG code. Icons with detailed artwork are made with the user in Adobe Illustrator: draft the SVG, open it in Illustrator by script, let the user refine it, then export and clean it (see "Working in Illustrator" in the guide).
- Check every new icon on light and dark backgrounds and at small sizes (16 to 48 px) before calling it done.

## Icon status tables in README.md

The "Icons Update Status and Source" section of `README.md` has two tables, one per status: "Updated" and "Needs an update". `blank.png`, an empty transparent image, is the one exception: it stays in "Updated" with the source "Calibre original icon".

- When an icon's status changes, move its row from its current table to the table of the new status. Never keep the same icon in two tables.
- Update the row's "Source" column if the new icon comes from a different source.
- An icon goes into "Updated" only if its source is one of the values listed above. Icons from any other source belong in "Needs an update".
- Keep each table in alphabetical order by file name.
- Show icons as `<img src="images/<file>" width="96">` in centered columns, so the "Light theme" and "Dark theme" columns have the same width.
- A new icon goes into the table that matches its status.

## Tools

- Run `tools\theme.cmd check` after changing icons or the README tables, and fix every error it reports.
- After changing icons, run `tools\theme.cmd preview` yourself so the user sees them in calibre; don't ask the user to run it. It restarts calibre and stops running calibre jobs. It builds in memory and never touches `dist/`.
- Never run calibre's `read_theme_from_folder` on `images/` itself: it writes `.png` copies of the `.svg` icons into the folder it reads. `tools/theme.py` always works on a temporary copy.
- `tools\theme.cmd build` writes the release `.zip` to `dist/`, which is not committed. The theme version calibre sees is the number of released versions in `CHANGELOG.md`.

## Changelog

Add an entry to `CHANGELOG.md` for every user-visible change (new or replaced icons, license, theme details), under a `## Unreleased` heading at the top. A release renames that heading to the version and date, for example `## 1.1.0 (2026-12-01)`.
