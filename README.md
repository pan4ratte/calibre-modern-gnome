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

This repository is meant to be cloned as calibre's `resources` folder, so calibre uses the icons in `images/` directly. `tools\theme.cmd` runs calibre's own icon theme tools on them (it needs calibre installed):

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
| bookmarks.svg                  | ![](images/bookmarks.svg)                  | Ubuntu GNOME Yaru-Blue                    |
| books_in_series.svg            | ![](images/books_in_series.svg)            | Ubuntu GNOME Yaru-Blue                    |
| character-set.png              | ![](images/character-set.png)              | Ubuntu GNOME Yaru-Blue                    |
| code.png                       | ![](images/code.png)                       | Ubuntu GNOME Yaru-Blue                    |
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
| document_open.png              | ![](images/document_open.png)              | Ubuntu GNOME Yaru-Blue                    |
| document-encrypt.png           | ![](images/document-encrypt.png)           | Ubuntu GNOME Yaru-Blue                    |
| document-import.png            | ![](images/document-import.png)            | Ubuntu GNOME Yaru-Blue                    |
| document-new.png               | ![](images/document-new.png)               | Ubuntu GNOME Yaru-Blue                    |
| download-metadata.png          | ![](images/download-metadata.png)          | Ubuntu GNOME Yaru-Blue                    |
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
| font_size_larger.png           | ![](images/font_size_larger.png)           | Pan4ratte (Me)                            |
| font_size_smaller.png          | ![](images/font_size_smaller.png)          | Pan4ratte (Me)                            |
| format-fill-color.png          | ![](images/format-fill-color.png)          | Pan4ratte (Me)                            |
| format-indent-less.png         | ![](images/format-indent-less.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-indent-more.png         | ![](images/format-indent-more.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-justify-center.png      | ![](images/format-justify-center.png)      | Ubuntu GNOME Yaru-Blue                    |
| format-justify-fill.png        | ![](images/format-justify-fill.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-justify-left.png        | ![](images/format-justify-left.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-justify-right.png       | ![](images/format-justify-right.png)       | Ubuntu GNOME Yaru-Blue                    |
| format-list-ordered.png        | ![](images/format-list-ordered.png)        | Pan4ratte (Me)                            |
| format-list-unordered.png      | ![](images/format-list-unordered.png)      | Pan4ratte (Me)                            |
| format-text-bold.png           | ![](images/format-text-bold.png)           | Ubuntu GNOME Yaru-Blue                    |
| format-text-color.png          | ![](images/format-text-color.png)          | Pan4ratte (Me)                            |
| format-text-heading.png        | ![](images/format-text-heading.png)        | Pan4ratte (Me)                            |
| format-text-hr.png             | ![](images/format-text-hr.png)             | Pan4ratte (Me)                            |
| format-text-italic.png         | ![](images/format-text-italic.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-text-strikethrough.png  | ![](images/format-text-strikethrough.png)  | Ubuntu GNOME Yaru-Blue                    |
| format-text-subscript.png      | ![](images/format-text-subscript.png)      | Pan4ratte (Me)                            |
| format-text-superscript.png    | ![](images/format-text-superscript.png)    | Pan4ratte (Me)                            |
| format-text-underline.png      | ![](images/format-text-underline.png)      | Ubuntu GNOME Yaru-Blue                    |
| grid.png                       | ![](images/grid.png)                       | Ubuntu GNOME Yaru-Blue                    |
| h-ellipsis.png                 | ![](images/h-ellipsis.png)                 | Ubuntu GNOME Yaru-Blue                    |
| help.png                       | ![](images/help.png)                       | Ubuntu GNOME Yaru-Blue                    |
| icon_choose.png                | ![](images/icon_choose.png)                | Ubuntu GNOME Yaru-Blue                    |
| insert-link.png                | ![](images/insert-link.png)                | Ubuntu GNOME Yaru-Blue                    |
| keyboard-prefs.png             | ![](images/keyboard-prefs.png)             | Ubuntu GNOME Yaru-Blue                    |
| languages.png                  | ![](images/languages.png)                  | Ubuntu GNOME Yaru-Blue                    |
| layout.png                     | ![](images/layout.png)                     | Ubuntu GNOME Yaru-Blue                    |
| library.png                    | ![](images/library.png)                    | Pan4ratte (Me)                            |
| lookfeel.png                   | ![](images/lookfeel.png)                   | Ubuntu GNOME Yaru-Blue                    |
| lt.png                         | ![](images/lt.png)                         | Pan4ratte (Me)                            |
| mail.png                       | ![](images/mail.png)                       | Ubuntu GNOME Yaru-Blue                    |
| minusminus.png                 | ![](images/minusminus.png)                 | Ubuntu GNOME Yaru-Blue                    |
| network-server.png             | ![](images/network-server.png)             | Ubuntu GNOME Yaru-Blue                    |
| plugboard.png                  | ![](images/plugboard.png)                  | Ubuntu GNOME Yaru-Blue                    |
| plugins.png                    | ![](images/plugins.png)                    | Ubuntu GNOME Yaru-Blue                    |
| print-preview.png              | ![](images/print-preview.png)              | Ubuntu GNOME Yaru-Blue                    |
| print.png                      | ![](images/print.png)                      | Ubuntu GNOME Yaru-Blue                    |
| rating.png                     | ![](images/rating.png)                     | Ubuntu GNOME Yaru-Blue                    |
| remove_books.png               | ![](images/remove_books.png)               | Ubuntu GNOME Yaru-Blue                    |
| restart.png                    | ![](images/restart.png)                    | Ubuntu GNOME Yaru-Blue                    |
| rotate-right.png               | ![](images/rotate-right.png)               | Ubuntu GNOME Yaru-Blue                    |
| save.png                       | ![](images/save.png)                       | Ubuntu GNOME Yaru-Blue                    |
| search.png                     | ![](images/search.png)                     | Ubuntu GNOME Yaru-Blue                    |
| spell-check.png                | ![](images/spell-check.png)                | Ubuntu GNOME Yaru-Blue                    |
| sync.png                       | ![](images/sync.png)                       | Ubuntu GNOME Yaru-Blue                    |
| tags.png                       | ![](images/tags.png)                       | Ubuntu GNOME Yaru-Blue                    |
| tb_folder.png                  | ![](images/tb_folder.png)                  | Ubuntu GNOME Yaru-Blue                    |
| trash.png                      | ![](images/trash.png)                      | Ubuntu GNOME Yaru-Blue                    |
| user_profile.png               | ![](images/user_profile.png)               | Ubuntu GNOME Yaru-Blue                    |
| v-ellipsis.png                 | ![](images/v-ellipsis.png)                 | Ubuntu GNOME Yaru-Blue                    |
| view-image.png                 | ![](images/view-image.png)                 | Ubuntu GNOME Yaru-Blue                    |
| view-refresh.png               | ![](images/view-refresh.png)               | Ubuntu GNOME Yaru-Blue                    |
| view.png                       | ![](images/view.png)                       | Ubuntu GNOME Yaru-Blue                    |
| window-close.png               | ![](images/window-close.png)               | Ubuntu GNOME Yaru-Blue                    |

### Needs an update

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| auto_author_sort.png           | ![](images/auto_author_sort.png)           | Calibre original icon                     |
| auto-reload.png                | ![](images/auto-reload.png)                | Calibre original icon                     |
| auto-scroll.png                | ![](images/auto-scroll.png)                | Calibre original icon                     |
| back.png                       | ![](images/back.png)                       | Calibre original icon                     |
| beautify.png                   | ![](images/beautify.png)                   | Calibre original icon                     |
| book.png                       | ![](images/book.png)                       | Calibre original icon                     |
| bullhorn.png                   | ![](images/bullhorn.png)                   | Calibre original icon                     |
| catalog.png                    | ![](images/catalog.png)                    | Calibre original icon                     |
| chapters.png                   | ![](images/chapters.png)                   | Calibre original icon                     |
| clear_left-for-dark-theme.png  | ![](images/clear_left-for-dark-theme.png)  | Calibre original icon                     |
| clear_left-for-light-theme.png | ![](images/clear_left-for-light-theme.png) | Calibre original icon                     |
| close-for-dark-theme.png       | ![](images/close-for-dark-theme.png)       | Calibre original icon                     |
| close-for-light-theme.png      | ![](images/close-for-light-theme.png)      | Calibre original icon                     |
| column.png                     | ![](images/column.png)                     | Icons8 (???)                              |
| compress-image.png             | ![](images/compress-image.png)             | Calibre original icon                     |
| copy-to-library.png            | ![](images/copy-to-library.png)            | Calibre original icon                     |
| cover_flow.png                 | ![](images/cover_flow.png)                 | Calibre original icon                     |
| debug.svg                      | ![](images/debug.svg)                      | ???                                       |
| default_cover.png              | ![](images/default_cover.png)              | Calibre original icon                     |
| diff.png                       | ![](images/diff.png)                       | Calibre original icon                     |
| document-split.png             | ![](images/document-split.png)             | Calibre original icon                     |
| donate.svg                     | ![](images/donate.svg)                     | ???                                       |
| dot_green.svg                  | ![](images/dot_green.svg)                  | ???                                       |
| dot_red.svg                    | ![](images/dot_red.svg)                    | ???                                       |
| drm-locked.svg                 | ![](images/drm-locked.svg)                 | ???                                       |
| drm-unlocked.svg               | ![](images/drm-unlocked.svg)               | ???                                       |
| filter.png                     | ![](images/filter.png)                     | Calibre original icon                     |
| forward.png                    | ![](images/forward.png)                    | Calibre original icon                     |
| fts.png                        | ![](images/fts.png)                        | Calibre original icon                     |
| generic-library.png            | ![](images/generic-library.png)            | Calibre original icon                     |
| gmail_logo.svg                 | ![](images/gmail_logo.svg)                 | ???                                       |
| heuristics.png                 | ![](images/heuristics.png)                 | Calibre original icon                     |
| highlight.png                  | ![](images/highlight.png)                  | Calibre original icon                     |
| highlight_only_off.png         | ![](images/highlight_only_off.png)         | Calibre original icon                     |
| highlight_only_on.png          | ![](images/highlight_only_on.png)          | Calibre original icon                     |
| hotmail.svg                    | ![](images/hotmail.svg)                    | ???                                       |
| html-fix.png                   | ![](images/html-fix.png)                   | Calibre original icon                     |
| identifiers.png                | ![](images/identifiers.png)                | ???                                       |
| jobs.png                       | ![](images/jobs.png)                       | Calibre original icon                     |
| list_remove.png                | ![](images/list_remove.png)                | ???                                       |
| marked.png                     | ![](images/marked.png)                     | Calibre original icon                     |
| merge.png                      | ![](images/merge.png)                      | Calibre original icon                     |
| merge_books.png                | ![](images/merge_books.png)                | Calibre original icon                     |
| metadata.png                   | ![](images/metadata.png)                   | Calibre original icon                     |
| minus.svg                      | ![](images/minus.svg)                      | Calibre original icon                     |
| modified-for-dark-theme.png    | ![](images/modified-for-dark-theme.png)    | Calibre original icon                     |
| modified-for-light-theme.png   | ![](images/modified-for-light-theme.png)   | Calibre original icon                     |
| news.png                       | ![](images/news.png)                       | Calibre original icon                     |
| next.svg                       | ![](images/next.svg)                       | ???                                       |
| notes-for-dark-theme.png       | ![](images/notes-for-dark-theme.png)       | Calibre original icon                     |
| notes.png                      | ![](images/notes.png)                      | Calibre original icon                     |
| ok.svg                         | ![](images/ok.svg)                         | ???                                       |
| page.svg                       | ![](images/page.svg)                       | ???                                       |
| plus.svg                       | ![](images/plus.svg)                       | Calibre original icon (-)                 |
| plusplus.png                   | ![](images/plusplus.png)                   | Calibre original icon                     |
| polish.png                     | ![](images/polish.png)                     | Calibre original icon                     |
| previous.svg                   | ![](images/previous.svg)                   | Calibre original icon                     |
| publisher.svg                  | ![](images/publisher.svg)                  | Calibre original icon                     |
| quickview.png                  | ![](images/quickview.png)                  | Calibre original icon                     |
| random.png                     | ![](images/random.png)                     | Calibre original icon                     |
| reader.png                     | ![](images/reader.png)                     | Calibre original icon                     |
| reference.png                  | ![](images/reference.png)                  | Calibre original icon                     |
| reports.png                    | ![](images/reports.png)                    | Calibre original icon                     |
| resize.png                     | ![](images/resize.png)                     | Calibre original icon                     |
| scheduler.png                  | ![](images/scheduler.png)                  | Calibre original icon                     |
| scroll.png                     | ![](images/scroll.png)                     | Calibre original icon                     |
| sd.png                         | ![](images/sd.png)                         | Calibre original icon                     |
| search_add_saved.png           | ![](images/search_add_saved.png)           | Calibre original icon                     |
| search_copy_saved.png          | ![](images/search_copy_saved.png)          | Calibre original icon                     |
| search_delete_saved.png        | ![](images/search_delete_saved.png)        | Calibre original icon                     |
| series.svg                     | ![](images/series.svg)                     | Calibre original icon                     |
| similar.png                    | ![](images/similar.png)                    | Calibre original icon                     |
| smarten-punctuation.png        | ![](images/smarten-punctuation.png)        | Calibre original icon                     |
| snippets.png                   | ![](images/snippets.png)                   | Calibre original icon                     |
| sort.png                       | ![](images/sort.png)                       | Calibre original icon                     |
| split.png                      | ![](images/split.png)                      | Calibre original icon                     |
| store.png                      | ![](images/store.png)                      | Calibre original icon                     |
| subset-fonts.png               | ![](images/subset-fonts.png)               | Calibre original icon                     |
| swap.png                       | ![](images/swap.png)                       | Calibre original icon                     |
| sync-right.png                 | ![](images/sync-right.png)                 | Calibre original icon                     |
| template_funcs.png             | ![](images/template_funcs.png)             | Calibre original icon                     |
| toc.png                        | ![](images/toc.png)                        | Calibre original icon                     |
| trim.png                       | ![](images/trim.png)                       | Calibre original icon                     |
| tweak.png                      | ![](images/tweak.png)                      | Calibre original icon                     |
| tweaks.png                     | ![](images/tweaks.png)                     | Calibre original icon                     |
| unpack-book.png                | ![](images/unpack-book.png)                | Calibre original icon                     |
| viewer.png                     | ![](images/viewer.png)                     | Calibre original icon                     |
| vl.png                         | ![](images/vl.png)                         | Calibre original icon                     |
| width.png                      | ![](images/width.png)                      | Calibre original icon                     |
| wizard.png                     | ![](images/wizard.png)                     | Calibre original icon                     |

### Unable to update

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| arrow-down.png                 | ![](images/arrow-down.png)                 | Calibre original icon                     |
| arrow-up.png                   | ![](images/arrow-up.png)                   | Calibre original icon                     |

### Unchanged

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| blank.png                      | ![](images/blank.png)                      | Calibre original icon                     |
