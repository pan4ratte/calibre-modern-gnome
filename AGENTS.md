# Agent Instructions

## Icon sources

The theme only uses two kinds of icons:

- icons from the Ubuntu Yaru icon theme (Yaru-Blue version), as they are or customized;
- icons drawn for this project in Yaru style.

Never add icons from other themes, websites or icon packs, even if their license allows it. Everything in the theme is licensed CC BY-SA 4.0 (see the License section in `README.md`), so every new icon must be shareable under it.

Use one of these values in the README "Source" column for replaced icons:

- `Ubuntu GNOME Yaru-Blue`
- `Ubuntu GNOME Yaru-Blue (customized by me)`
- `Pan4ratte (Me)` (drawn for this project)

## Drawing icons

- Every icon drawn for this project has its source in `src/<icon-name>.svg`. `tools\theme.cmd render` turns it into `images/<icon-name>.png` (256×256). Never edit those PNG files by hand.
- Base new icons on Yaru: its full-color sources (`icons/src/fullcolor` in github.com/ubuntu/yaru) for the look, and its symbolic icons (`icons/src/scalable`) for the idea when there is no full-color one.
- Match the 256px Yaru icons already in the theme: glyphs use a #4d4d4d to #151515 gradient (top left to bottom right) with a 4px white outline; text lines are #232629 bars with a white copy 8px below; keep the drawing inside 32..224 px.
- Check every new icon on light and dark backgrounds and at small sizes (16 to 48 px) before calling it done.

## Icon status tables in README.md

The "Icons Update Status and Source" section of `README.md` has four tables, one per status: "Updated", "Needs an update", "Unable to update" and "Unchanged".

- When an icon's status changes, move its row from its current table to the table of the new status. Never keep the same icon in two tables.
- Update the row's "Source" column if the new icon comes from a different source.
- An icon goes into "Updated" only if its source is one of the values listed above. Icons from any other source belong in "Needs an update".
- Keep each table in alphabetical order by file name.
- A new icon goes into the table that matches its status.

## Tools

- Run `tools\theme.cmd check` after changing icons or the README tables, and fix every error it reports.
- After changing icons, run `tools\theme.cmd preview` yourself so the user sees them in calibre; don't ask the user to run it. It restarts calibre and stops running calibre jobs. It builds in memory and never touches `dist/`.
- Never run calibre's `read_theme_from_folder` on `images/` itself: it writes `.png` copies of the `.svg` icons into the folder it reads. `tools/theme.py` always works on a temporary copy.
- `tools\theme.cmd build` writes the release `.zip` to `dist/`, which is not committed. The theme version calibre sees is the number of released versions in `CHANGELOG.md`.

## Changelog

Add an entry to `CHANGELOG.md` for every user-visible change (new or replaced icons, license, theme details), under a `## Unreleased` heading at the top. A release renames that heading to the version and date, for example `## 1.1.0 (2026-12-01)`.
