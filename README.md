# Calibre Modern GNOME

This is a Calibre icon theme, a modern and a clean one. All themes, that are currently available in the Calibre icon store, are morally deprecated and should be replaced with some modern alternative. This is that alternative. See [CHANGELOG.md](CHANGELOG.md) for the changes in each release.

## Installation

The theme is not in calibre's icon theme list yet, so for now it is installed by hand:

1. Download this repository (Code → Download ZIP) and unpack it.
2. In calibre, open Preferences → Advanced → Miscellaneous → Open calibre configuration directory.
3. Copy the `images` folder from the download into the `resources` folder there (create `resources` if it does not exist).
4. Restart calibre.

Icons in that folder are used instead of any icon theme chosen in calibre. To go back to the default icons, delete `resources/images` and restart calibre.

## Development

This repository is meant to be cloned as calibre's `resources` folder, so calibre uses the icons in `images/` directly. Icons drawn for this project follow the [Yaru style guide](docs/yaru-style.md). `tools\theme.cmd` runs calibre's own icon theme tools on them (it needs calibre installed):

- `tools\theme.cmd check` lists calibre icons the theme does not have, icons calibre no longer uses, broken images and README tables that do not match the `images` folder.
- `tools\theme.cmd render` turns the icons drawn for this project, kept as SVG files in `src/`, into the 256×256 PNG files in `images/` that calibre uses. Edit the SVG, never the PNG.
- `tools\theme.cmd preview` closes calibre, builds the theme, installs it in calibre and starts calibre again, so you see exactly what a release would look like. Close calibre jobs first, the restart stops them.
- `tools\theme.cmd build` saves the theme as a calibre icon theme `.zip` in `dist/`, named after the newest version in [CHANGELOG.md](CHANGELOG.md). This is the file to send for inclusion in calibre's icon theme list.

## Key Principles

1. Use Ubuntu GNOME Yaru icons, particularly the Yaru-Blue version. I really like the GNOME iteration of Ubuntu Linux in terms of UI, and Yaru-Blue feels the most fitting in the calibre interface. If Yaru has a good icon for a certain UI element in calibre, use it.

2. If Yaru has no icon that fits, draw a new one in Yaru style. A Yaru icon with a similar meaning, changed or combined with other Yaru elements, is a good starting point.

3. No icons from other themes, websites or icon packs. Every icon in the theme is either a Yaru icon or drawn for this project, so the whole theme has one style and one license.

The goal is to replace every calibre icon this way. Icons that still come from other sources, including calibre's original icons, are listed under "Needs an update" until they are replaced.

## License

The theme is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE) (CC BY-SA 4.0), the same license as the Yaru icons it is based on.

- Yaru icons are made by the [Yaru team](https://github.com/ubuntu/yaru) and licensed under CC BY-SA 4.0. Customized Yaru icons are shared under the same license.
- Icons drawn for this project are licensed under CC BY-SA 4.0.
- Icons that are not replaced yet (the "Needs an update", "Unable to update" and "Unchanged" tables) keep their original licenses. Most of them are calibre's original icons, which come with calibre under its own licenses. Icons with an unknown source ("???") will be replaced first.

## Icons Update Status and Source

The tables below represent the current update status of each icon in the collection and its source. There is one table per status, and the icons in each table are listed in alphabetical order. Status options:

1. "Updated": icon was replaced with a Yaru icon or an icon drawn in Yaru style;
2. "Needs an update": icon should be replaced with a Yaru icon or an icon drawn in Yaru style;
3. "Unable to update": icon is not replacable because it used for multiple, contradicting purposes in the Calibre UI. Such icons could be updated only after UI changes in the Calibre itself;
4. "Unchanged": icon do not need an update because it is good enough already.

### Updated

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| add_book.png                   | ![](images/add_book.png)                   | Ubuntu GNOME Yaru-Blue                    |
| apple-touch-icon.png           | ![](images/apple-touch-icon.png)           | Pan4ratte (Me)                            |
| arrow-down-for-dark-theme.png  | ![](images/arrow-down-for-dark-theme.png)  | Pan4ratte (Me)                            |
| arrow-down.png                 | ![](images/arrow-down.png)                 | Pan4ratte (Me)                            |
| arrow-up-for-dark-theme.png    | ![](images/arrow-up-for-dark-theme.png)    | Pan4ratte (Me)                            |
| arrow-up.png                   | ![](images/arrow-up.png)                   | Pan4ratte (Me)                            |
| auto-reload-for-dark-theme.png | ![](images/auto-reload-for-dark-theme.png) | Pan4ratte (Me)                            |
| auto-reload.png                | ![](images/auto-reload.png)                | Pan4ratte (Me)                            |
| auto-scroll-for-dark-theme.png | ![](images/auto-scroll-for-dark-theme.png) | Pan4ratte (Me)                            |
| auto-scroll.png                | ![](images/auto-scroll.png)                | Pan4ratte (Me)                            |
| auto_author_sort-for-dark-theme.png | ![](images/auto_author_sort-for-dark-theme.png) | Pan4ratte (Me)                            |
| auto_author_sort.png           | ![](images/auto_author_sort.png)           | Pan4ratte (Me)                            |
| back-for-dark-theme.png        | ![](images/back-for-dark-theme.png)        | Pan4ratte (Me)                            |
| back.png                       | ![](images/back.png)                       | Pan4ratte (Me)                            |
| books_in_series.png            | ![](images/books_in_series.png)            | Pan4ratte (Me)                            |
| bullhorn-for-dark-theme.png    | ![](images/bullhorn-for-dark-theme.png)    | Pan4ratte (Me)                            |
| bullhorn.png                   | ![](images/bullhorn.png)                   | Pan4ratte (Me)                            |
| chapters-for-dark-theme.png    | ![](images/chapters-for-dark-theme.png)    | Pan4ratte (Me)                            |
| chapters.png                   | ![](images/chapters.png)                   | Pan4ratte (Me)                            |
| character-set.png              | ![](images/character-set.png)              | Ubuntu GNOME Yaru-Blue                    |
| clear_left-for-dark-theme.png  | ![](images/clear_left-for-dark-theme.png)  | Pan4ratte (Me)                            |
| clear_left-for-light-theme.png | ![](images/clear_left-for-light-theme.png) | Pan4ratte (Me)                            |
| close-for-dark-theme.png       | ![](images/close-for-dark-theme.png)       | Pan4ratte (Me)                            |
| close-for-light-theme.png      | ![](images/close-for-light-theme.png)      | Pan4ratte (Me)                            |
| code.png                       | ![](images/code.png)                       | Ubuntu GNOME Yaru-Blue                    |
| column.png                     | ![](images/column.png)                     | Pan4ratte (Me)                            |
| config.png                     | ![](images/config.png)                     | Ubuntu GNOME Yaru-Blue                    |
| connect_share.png              | ![](images/connect_share.png)              | Ubuntu GNOME Yaru-Blue (customized by me) |
| connect_share_on.png           | ![](images/connect_share_on.png)           | Ubuntu GNOME Yaru-Blue                    |
| context_menu.png               | ![](images/context_menu.png)               | Ubuntu GNOME Yaru-Blue                    |
| convert.png                    | ![](images/convert.png)                    | Ubuntu GNOME Yaru-Blue                    |
| dialog_error.png               | ![](images/dialog_error.png)               | Ubuntu GNOME Yaru-Blue                    |
| dialog_information.png         | ![](images/dialog_information.png)         | Ubuntu GNOME Yaru-Blue                    |
| dialog_question.png            | ![](images/dialog_question.png)            | Ubuntu GNOME Yaru-Blue                    |
| dialog_warning.png             | ![](images/dialog_warning.png)             | Ubuntu GNOME Yaru-Blue                    |
| dictionary.png                 | ![](images/dictionary.png)                 | Ubuntu GNOME Yaru-Blue                    |
| diff-for-dark-theme.png        | ![](images/diff-for-dark-theme.png)        | Pan4ratte (Me)                            |
| diff.png                       | ![](images/diff.png)                       | Pan4ratte (Me)                            |
| document-encrypt.png           | ![](images/document-encrypt.png)           | Ubuntu GNOME Yaru-Blue                    |
| document-import.png            | ![](images/document-import.png)            | Ubuntu GNOME Yaru-Blue                    |
| document-new.png               | ![](images/document-new.png)               | Ubuntu GNOME Yaru-Blue                    |
| document-split-for-dark-theme.png | ![](images/document-split-for-dark-theme.png) | Pan4ratte (Me)                            |
| document-split.png             | ![](images/document-split.png)             | Pan4ratte (Me)                            |
| document_open.png              | ![](images/document_open.png)              | Ubuntu GNOME Yaru-Blue                    |
| download-metadata.png          | ![](images/download-metadata.png)          | Ubuntu GNOME Yaru-Blue                    |
| edit-clear-for-dark-theme.png  | ![](images/edit-clear-for-dark-theme.png)  | Pan4ratte (Me)                            |
| edit-clear.png                 | ![](images/edit-clear.png)                 | Pan4ratte (Me)                            |
| edit-copy.png                  | ![](images/edit-copy.png)                  | Ubuntu GNOME Yaru-Blue                    |
| edit-cut.png                   | ![](images/edit-cut.png)                   | Ubuntu GNOME Yaru-Blue                    |
| edit-paste.png                 | ![](images/edit-paste.png)                 | Ubuntu GNOME Yaru-Blue                    |
| edit-redo.png                  | ![](images/edit-redo.png)                  | Ubuntu GNOME Yaru-Blue                    |
| edit-select-all.png            | ![](images/edit-select-all.png)            | Ubuntu GNOME Yaru-Blue                    |
| edit-undo.png                  | ![](images/edit-undo.png)                  | Ubuntu GNOME Yaru-Blue                    |
| edit_book.png                  | ![](images/edit_book.png)                  | Ubuntu GNOME Yaru-Blue                    |
| edit_input.png                 | ![](images/edit_input.png)                 | Ubuntu GNOME Yaru-Blue                    |
| eject.png                      | ![](images/eject.png)                      | Ubuntu GNOME Yaru-Blue                    |
| embed-fonts.png                | ![](images/embed-fonts.png)                | Ubuntu GNOME Yaru-Blue                    |
| exec.png                       | ![](images/exec.png)                       | Ubuntu GNOME Yaru-Blue                    |
| external-link.png              | ![](images/external-link.png)              | Ubuntu GNOME Yaru-Blue                    |
| folder_saved_search.png        | ![](images/folder_saved_search.png)        | Ubuntu GNOME Yaru-Blue                    |
| font.png                       | ![](images/font.png)                       | Ubuntu GNOME Yaru-Blue                    |
| font_size_larger-for-dark-theme.png | ![](images/font_size_larger-for-dark-theme.png) | Pan4ratte (Me)                            |
| font_size_larger.png           | ![](images/font_size_larger.png)           | Pan4ratte (Me)                            |
| font_size_smaller-for-dark-theme.png | ![](images/font_size_smaller-for-dark-theme.png) | Pan4ratte (Me)                            |
| font_size_smaller.png          | ![](images/font_size_smaller.png)          | Pan4ratte (Me)                            |
| format-fill-color-for-dark-theme.png | ![](images/format-fill-color-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-fill-color.png          | ![](images/format-fill-color.png)          | Pan4ratte (Me)                            |
| format-indent-less.png         | ![](images/format-indent-less.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-indent-more.png         | ![](images/format-indent-more.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-justify-center.png      | ![](images/format-justify-center.png)      | Ubuntu GNOME Yaru-Blue                    |
| format-justify-fill.png        | ![](images/format-justify-fill.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-justify-left.png        | ![](images/format-justify-left.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-justify-right.png       | ![](images/format-justify-right.png)       | Ubuntu GNOME Yaru-Blue                    |
| format-list-ordered-for-dark-theme.png | ![](images/format-list-ordered-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-list-ordered.png        | ![](images/format-list-ordered.png)        | Pan4ratte (Me)                            |
| format-list-unordered-for-dark-theme.png | ![](images/format-list-unordered-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-list-unordered.png      | ![](images/format-list-unordered.png)      | Pan4ratte (Me)                            |
| format-text-bold-for-dark-theme.png | ![](images/format-text-bold-for-dark-theme.png) | Ubuntu GNOME Yaru-Blue (customized by me) |
| format-text-bold.png           | ![](images/format-text-bold.png)           | Ubuntu GNOME Yaru-Blue                    |
| format-text-color-for-dark-theme.png | ![](images/format-text-color-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-text-color.png          | ![](images/format-text-color.png)          | Pan4ratte (Me)                            |
| format-text-heading-for-dark-theme.png | ![](images/format-text-heading-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-text-heading.png        | ![](images/format-text-heading.png)        | Pan4ratte (Me)                            |
| format-text-hr-for-dark-theme.png | ![](images/format-text-hr-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-text-hr.png             | ![](images/format-text-hr.png)             | Pan4ratte (Me)                            |
| format-text-italic-for-dark-theme.png | ![](images/format-text-italic-for-dark-theme.png) | Ubuntu GNOME Yaru-Blue (customized by me) |
| format-text-italic.png         | ![](images/format-text-italic.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-text-strikethrough-for-dark-theme.png | ![](images/format-text-strikethrough-for-dark-theme.png) | Ubuntu GNOME Yaru-Blue (customized by me) |
| format-text-strikethrough.png  | ![](images/format-text-strikethrough.png)  | Ubuntu GNOME Yaru-Blue                    |
| format-text-subscript-for-dark-theme.png | ![](images/format-text-subscript-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-text-subscript.png      | ![](images/format-text-subscript.png)      | Pan4ratte (Me)                            |
| format-text-superscript-for-dark-theme.png | ![](images/format-text-superscript-for-dark-theme.png) | Pan4ratte (Me)                            |
| format-text-superscript.png    | ![](images/format-text-superscript.png)    | Pan4ratte (Me)                            |
| format-text-underline-for-dark-theme.png | ![](images/format-text-underline-for-dark-theme.png) | Ubuntu GNOME Yaru-Blue (customized by me) |
| format-text-underline.png      | ![](images/format-text-underline.png)      | Ubuntu GNOME Yaru-Blue                    |
| forward-for-dark-theme.png     | ![](images/forward-for-dark-theme.png)     | Pan4ratte (Me)                            |
| forward.png                    | ![](images/forward.png)                    | Pan4ratte (Me)                            |
| grid.png                       | ![](images/grid.png)                       | Ubuntu GNOME Yaru-Blue                    |
| h-ellipsis.png                 | ![](images/h-ellipsis.png)                 | Ubuntu GNOME Yaru-Blue                    |
| help.png                       | ![](images/help.png)                       | Ubuntu GNOME Yaru-Blue                    |
| icon_choose.png                | ![](images/icon_choose.png)                | Ubuntu GNOME Yaru-Blue                    |
| identifiers.png                | ![](images/identifiers.png)                | Pan4ratte (Me)                            |
| insert-link-for-dark-theme.png | ![](images/insert-link-for-dark-theme.png) | Pan4ratte (Me)                            |
| insert-link.png                | ![](images/insert-link.png)                | Pan4ratte (Me)                            |
| keyboard-prefs.png             | ![](images/keyboard-prefs.png)             | Ubuntu GNOME Yaru-Blue                    |
| languages.png                  | ![](images/languages.png)                  | Ubuntu GNOME Yaru-Blue                    |
| layout.png                     | ![](images/layout.png)                     | Ubuntu GNOME Yaru-Blue                    |
| library.png                    | ![](images/library.png)                    | Pan4ratte (Me)                            |
| list_remove-for-dark-theme.png | ![](images/list_remove-for-dark-theme.png) | Pan4ratte (Me)                            |
| list_remove.png                | ![](images/list_remove.png)                | Pan4ratte (Me)                            |
| lookfeel.png                   | ![](images/lookfeel.png)                   | Ubuntu GNOME Yaru-Blue                    |
| lt.png                         | ![](images/lt.png)                         | Pan4ratte (Me)                            |
| mail.png                       | ![](images/mail.png)                       | Ubuntu GNOME Yaru-Blue                    |
| minus-for-dark-theme.png       | ![](images/minus-for-dark-theme.png)       | Pan4ratte (Me)                            |
| minus.png                      | ![](images/minus.png)                      | Pan4ratte (Me)                            |
| minusminus-for-dark-theme.png  | ![](images/minusminus-for-dark-theme.png)  | Pan4ratte (Me)                            |
| minusminus.png                 | ![](images/minusminus.png)                 | Pan4ratte (Me)                            |
| network-server.png             | ![](images/network-server.png)             | Ubuntu GNOME Yaru-Blue                    |
| news.png                       | ![](images/news.png)                       | Ubuntu GNOME Yaru-Blue                    |
| next-for-dark-theme.png        | ![](images/next-for-dark-theme.png)        | Pan4ratte (Me)                            |
| next.png                       | ![](images/next.png)                       | Pan4ratte (Me)                            |
| ok-for-dark-theme.png          | ![](images/ok-for-dark-theme.png)          | Pan4ratte (Me)                            |
| ok.png                         | ![](images/ok.png)                         | Pan4ratte (Me)                            |
| plugboard.png                  | ![](images/plugboard.png)                  | Ubuntu GNOME Yaru-Blue                    |
| plugins.png                    | ![](images/plugins.png)                    | Ubuntu GNOME Yaru-Blue                    |
| plus-for-dark-theme.png        | ![](images/plus-for-dark-theme.png)        | Pan4ratte (Me)                            |
| plus.png                       | ![](images/plus.png)                       | Pan4ratte (Me)                            |
| plusplus-for-dark-theme.png    | ![](images/plusplus-for-dark-theme.png)    | Pan4ratte (Me)                            |
| plusplus.png                   | ![](images/plusplus.png)                   | Pan4ratte (Me)                            |
| previous-for-dark-theme.png    | ![](images/previous-for-dark-theme.png)    | Pan4ratte (Me)                            |
| previous.png                   | ![](images/previous.png)                   | Pan4ratte (Me)                            |
| print-preview.png              | ![](images/print-preview.png)              | Ubuntu GNOME Yaru-Blue                    |
| print.png                      | ![](images/print.png)                      | Ubuntu GNOME Yaru-Blue                    |
| publisher.png                  | ![](images/publisher.png)                  | Pan4ratte (Me)                            |
| reader.png                     | ![](images/reader.png)                     | Ubuntu GNOME Yaru-Blue                    |
| remove_books.png               | ![](images/remove_books.png)               | Ubuntu GNOME Yaru-Blue                    |
| reports.png                    | ![](images/reports.png)                    | Ubuntu GNOME Yaru-Blue                    |
| restart.png                    | ![](images/restart.png)                    | Ubuntu GNOME Yaru-Blue                    |
| rotate-right-for-dark-theme.png | ![](images/rotate-right-for-dark-theme.png) | Pan4ratte (Me)                            |
| rotate-right.png               | ![](images/rotate-right.png)               | Pan4ratte (Me)                            |
| save.png                       | ![](images/save.png)                       | Ubuntu GNOME Yaru-Blue                    |
| scheduler.png                  | ![](images/scheduler.png)                  | Ubuntu GNOME Yaru-Blue                    |
| sd.png                         | ![](images/sd.png)                         | Ubuntu GNOME Yaru-Blue                    |
| search.png                     | ![](images/search.png)                     | Ubuntu GNOME Yaru-Blue                    |
| search_add_saved.png           | ![](images/search_add_saved.png)           | Ubuntu GNOME Yaru-Blue                    |
| search_delete_saved.png        | ![](images/search_delete_saved.png)        | Ubuntu GNOME Yaru-Blue                    |
| series.png                     | ![](images/series.png)                     | Pan4ratte (Me)                            |
| store.png                      | ![](images/store.png)                      | Ubuntu GNOME Yaru-Blue                    |
| sync-right-for-dark-theme.png  | ![](images/sync-right-for-dark-theme.png)  | Pan4ratte (Me)                            |
| sync-right.png                 | ![](images/sync-right.png)                 | Pan4ratte (Me)                            |
| sync.png                       | ![](images/sync.png)                       | Ubuntu GNOME Yaru-Blue                    |
| tags.png                       | ![](images/tags.png)                       | Pan4ratte (Me)                            |
| tb_folder.png                  | ![](images/tb_folder.png)                  | Ubuntu GNOME Yaru-Blue                    |
| template_funcs.png             | ![](images/template_funcs.png)             | Ubuntu GNOME Yaru-Blue                    |
| trash.png                      | ![](images/trash.png)                      | Ubuntu GNOME Yaru-Blue                    |
| trim.png                       | ![](images/trim.png)                       | Ubuntu GNOME Yaru-Blue                    |
| tweak.png                      | ![](images/tweak.png)                      | Ubuntu GNOME Yaru-Blue                    |
| tweaks.png                     | ![](images/tweaks.png)                     | Ubuntu GNOME Yaru-Blue                    |
| user_profile.png               | ![](images/user_profile.png)               | Ubuntu GNOME Yaru-Blue                    |
| v-ellipsis.png                 | ![](images/v-ellipsis.png)                 | Ubuntu GNOME Yaru-Blue                    |
| view-image.png                 | ![](images/view-image.png)                 | Ubuntu GNOME Yaru-Blue                    |
| view-refresh-for-dark-theme.png | ![](images/view-refresh-for-dark-theme.png) | Pan4ratte (Me)                            |
| view-refresh.png               | ![](images/view-refresh.png)               | Pan4ratte (Me)                            |
| view.png                       | ![](images/view.png)                       | Ubuntu GNOME Yaru-Blue                    |
| viewer.png                     | ![](images/viewer.png)                     | Ubuntu GNOME Yaru-Blue                    |
| window-close.png               | ![](images/window-close.png)               | Ubuntu GNOME Yaru-Blue                    |
| wizard.png                     | ![](images/wizard.png)                     | Ubuntu GNOME Yaru-Blue                    |

### Needs an update

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| ai.png                         | ![](images/ai.png)                         | Calibre original icon                     |
| beautify.png                   | ![](images/beautify.png)                   | Calibre original icon                     |
| book.png                       | ![](images/book.png)                       | Calibre original icon                     |
| bookmarks.svg                  | ![](images/bookmarks.svg)                  | Ubuntu GNOME Yaru-Blue                    |
| bookshelf.png                  | ![](images/bookshelf.png)                  | Calibre original icon                     |
| calibre.svg                    | ![](images/calibre.svg)                    | Calibre original icon                     |
| catalog.png                    | ![](images/catalog.png)                    | Calibre original icon                     |
| compress-image.png             | ![](images/compress-image.png)             | Calibre original icon                     |
| copy-to-library.png            | ![](images/copy-to-library.png)            | Calibre original icon                     |
| cover_flow.png                 | ![](images/cover_flow.png)                 | Calibre original icon                     |
| cyoa.png                       | ![](images/cyoa.png)                       | Calibre original icon                     |
| debug.svg                      | ![](images/debug.svg)                      | ???                                       |
| default_cover.png              | ![](images/default_cover.png)              | Calibre original icon                     |
| donate.svg                     | ![](images/donate.svg)                     | ???                                       |
| dot_green.svg                  | ![](images/dot_green.svg)                  | ???                                       |
| dot_red.svg                    | ![](images/dot_red.svg)                    | ???                                       |
| drm-locked.svg                 | ![](images/drm-locked.svg)                 | ???                                       |
| drm-unlocked.svg               | ![](images/drm-unlocked.svg)               | ???                                       |
| favicon-192.png                | ![](images/favicon-192.png)                | Calibre original icon                     |
| favicon-512.png                | ![](images/favicon-512.png)                | Calibre original icon                     |
| filter.png                     | ![](images/filter.png)                     | Calibre original icon                     |
| fts.png                        | ![](images/fts.png)                        | Calibre original icon                     |
| gear.png                       | ![](images/gear.png)                       | Calibre original icon                     |
| generic-library.png            | ![](images/generic-library.png)            | Calibre original icon                     |
| gmail_logo.svg                 | ![](images/gmail_logo.svg)                 | ???                                       |
| heuristics.png                 | ![](images/heuristics.png)                 | Calibre original icon                     |
| highlight.png                  | ![](images/highlight.png)                  | Calibre original icon                     |
| highlight_only_off.png         | ![](images/highlight_only_off.png)         | Calibre original icon                     |
| highlight_only_on.png          | ![](images/highlight_only_on.png)          | Calibre original icon                     |
| hotmail.svg                    | ![](images/hotmail.svg)                    | ???                                       |
| html-fix.png                   | ![](images/html-fix.png)                   | Calibre original icon                     |
| jobs.png                       | ![](images/jobs.png)                       | Calibre original icon                     |
| marked.png                     | ![](images/marked.png)                     | Calibre original icon                     |
| merge.png                      | ![](images/merge.png)                      | Calibre original icon                     |
| merge_books.png                | ![](images/merge_books.png)                | Calibre original icon                     |
| metadata.png                   | ![](images/metadata.png)                   | Calibre original icon                     |
| modified-for-dark-theme.png    | ![](images/modified-for-dark-theme.png)    | Calibre original icon                     |
| modified-for-light-theme.png   | ![](images/modified-for-light-theme.png)   | Calibre original icon                     |
| notes-for-dark-theme.png       | ![](images/notes-for-dark-theme.png)       | Calibre original icon                     |
| notes.png                      | ![](images/notes.png)                      | Calibre original icon                     |
| page.svg                       | ![](images/page.svg)                       | ???                                       |
| polish.png                     | ![](images/polish.png)                     | Calibre original icon                     |
| quickview.png                  | ![](images/quickview.png)                  | Calibre original icon                     |
| random.png                     | ![](images/random.png)                     | Calibre original icon                     |
| rating.png                     | ![](images/rating.png)                     | Ubuntu GNOME Yaru-Blue                    |
| reference.png                  | ![](images/reference.png)                  | Calibre original icon                     |
| resize.png                     | ![](images/resize.png)                     | Calibre original icon                     |
| scene-divider.png              | ![](images/scene-divider.png)              | Calibre original icon                     |
| scroll.png                     | ![](images/scroll.png)                     | Calibre original icon                     |
| search_copy_saved.png          | ![](images/search_copy_saved.png)          | Calibre original icon                     |
| send.png                       | ![](images/send.png)                       | Calibre original icon                     |
| similar.png                    | ![](images/similar.png)                    | Calibre original icon                     |
| smarten-punctuation.png        | ![](images/smarten-punctuation.png)        | Calibre original icon                     |
| snippets.png                   | ![](images/snippets.png)                   | Calibre original icon                     |
| sort.png                       | ![](images/sort.png)                       | Calibre original icon                     |
| spell-check.png                | ![](images/spell-check.png)                | Ubuntu GNOME Yaru-Blue                    |
| split.png                      | ![](images/split.png)                      | Calibre original icon                     |
| subset-fonts.png               | ![](images/subset-fonts.png)               | Calibre original icon                     |
| swap.png                       | ![](images/swap.png)                       | Calibre original icon                     |
| toc.png                        | ![](images/toc.png)                        | Calibre original icon                     |
| unpack-book.png                | ![](images/unpack-book.png)                | Calibre original icon                     |
| vl.png                         | ![](images/vl.png)                         | Calibre original icon                     |
| width.png                      | ![](images/width.png)                      | Calibre original icon                     |

### Unable to update

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|

### Unchanged

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| blank.png                      | ![](images/blank.png)                      | Calibre original icon                     |
