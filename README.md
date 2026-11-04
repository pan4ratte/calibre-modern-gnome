<div align="center">
  <img src="images/calibre.png" width="128" height="128" alt="Calibre Modern GNOME logo">
  <h1>Calibre Modern GNOME</h1>
  <p>Modern, clean icon theme for calibre<br>in the style of Ubuntu's Yaru icons</p>
</div>

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
- Icons that are not replaced yet (the "Needs an update" and "Unchanged" tables) keep their original licenses. Most of them are calibre's original icons, which come with calibre under its own licenses. Icons with an unknown source ("???") will be replaced first.

## Icons Update Status and Source

The tables below represent the current update status of each icon in the collection and its source. There is one table per status, and the icons in each table are listed in alphabetical order. Status options:

1. "Updated": icon was replaced with a Yaru icon or an icon drawn in Yaru style;
2. "Needs an update": icon should be replaced with a Yaru icon or an icon drawn in Yaru style;
3. "Unchanged": icon do not need an update because it is good enough already.

In the "Updated" table, the "Light theme" column shows the icon calibre uses in light mode, and the "Dark theme" column the version it uses in dark mode, for icons that have one.

### Updated

| File name                      | Light theme                                | Dark theme                                               | Source                 |
|--------------------------------|--------------------------------------------|----------------------------------------------------------|------------------------|
| add_book.png                   | ![](images/add_book.png)                   |                                                          | Yaru-Blue              |
| ai.png                         | ![](images/ai.png)                         |                                                          | Mark Ingrem            |
| apple-touch-icon.png           | ![](images/apple-touch-icon.png)           |                                                          | Mark Ingrem            |
| arrow-down.png                 | ![](images/arrow-down.png)                 | ![](images/arrow-down-for-dark-theme.png)                | Mark Ingrem            |
| arrow-up.png                   | ![](images/arrow-up.png)                   | ![](images/arrow-up-for-dark-theme.png)                  | Mark Ingrem            |
| auto-reload.png                | ![](images/auto-reload.png)                | ![](images/auto-reload-for-dark-theme.png)               | Mark Ingrem            |
| auto-scroll.png                | ![](images/auto-scroll.png)                | ![](images/auto-scroll-for-dark-theme.png)               | Mark Ingrem            |
| auto_author_sort.png           | ![](images/auto_author_sort.png)           | ![](images/auto_author_sort-for-dark-theme.png)          | Mark Ingrem            |
| back.png                       | ![](images/back.png)                       | ![](images/back-for-dark-theme.png)                      | Mark Ingrem            |
| books_in_series.png            | ![](images/books_in_series.png)            |                                                          | Mark Ingrem            |
| bullhorn.png                   | ![](images/bullhorn.png)                   | ![](images/bullhorn-for-dark-theme.png)                  | Mark Ingrem            |
| calibre.png                    | ![](images/calibre.png)                    |                                                          | Mark Ingrem            |
| chapters.png                   | ![](images/chapters.png)                   | ![](images/chapters-for-dark-theme.png)                  | Mark Ingrem            |
| character-set.png              | ![](images/character-set.png)              |                                                          | Yaru-Blue              |
| clear_left-for-light-theme.png | ![](images/clear_left-for-light-theme.png) | ![](images/clear_left-for-dark-theme.png)                | Mark Ingrem            |
| close-for-light-theme.png      | ![](images/close-for-light-theme.png)      | ![](images/close-for-dark-theme.png)                     | Mark Ingrem            |
| code.png                       | ![](images/code.png)                       |                                                          | Yaru-Blue              |
| column.png                     | ![](images/column.png)                     |                                                          | Mark Ingrem            |
| config.png                     | ![](images/config.png)                     |                                                          | Yaru-Blue              |
| connect_share.png              | ![](images/connect_share.png)              |                                                          | Yaru-Blue (customized) |
| connect_share_on.png           | ![](images/connect_share_on.png)           |                                                          | Yaru-Blue              |
| context_menu.png               | ![](images/context_menu.png)               |                                                          | Yaru-Blue              |
| convert.png                    | ![](images/convert.png)                    |                                                          | Yaru-Blue              |
| dialog_error.png               | ![](images/dialog_error.png)               |                                                          | Yaru-Blue              |
| dialog_information.png         | ![](images/dialog_information.png)         |                                                          | Yaru-Blue              |
| dialog_question.png            | ![](images/dialog_question.png)            |                                                          | Yaru-Blue              |
| dialog_warning.png             | ![](images/dialog_warning.png)             |                                                          | Yaru-Blue              |
| dictionary.png                 | ![](images/dictionary.png)                 |                                                          | Yaru-Blue              |
| diff.png                       | ![](images/diff.png)                       | ![](images/diff-for-dark-theme.png)                      | Mark Ingrem            |
| document-encrypt.png           | ![](images/document-encrypt.png)           |                                                          | Yaru-Blue              |
| document-import.png            | ![](images/document-import.png)            |                                                          | Yaru-Blue              |
| document-new.png               | ![](images/document-new.png)               |                                                          | Yaru-Blue              |
| document-split.png             | ![](images/document-split.png)             | ![](images/document-split-for-dark-theme.png)            | Mark Ingrem            |
| document_open.png              | ![](images/document_open.png)              |                                                          | Yaru-Blue              |
| donate.png                     | ![](images/donate.png)                     |                                                          | Mark Ingrem            |
| dot_green.png                  | ![](images/dot_green.png)                  |                                                          | Yaru-Blue (customized) |
| dot_red.png                    | ![](images/dot_red.png)                    |                                                          | Yaru-Blue (customized) |
| download-metadata.png          | ![](images/download-metadata.png)          |                                                          | Yaru-Blue              |
| drm-locked.png                 | ![](images/drm-locked.png)                 |                                                          | Yaru-Blue (customized) |
| drm-unlocked.png               | ![](images/drm-unlocked.png)               |                                                          | Yaru-Blue (customized) |
| edit-clear.png                 | ![](images/edit-clear.png)                 | ![](images/edit-clear-for-dark-theme.png)                | Mark Ingrem            |
| edit-copy.png                  | ![](images/edit-copy.png)                  |                                                          | Yaru-Blue              |
| edit-cut.png                   | ![](images/edit-cut.png)                   |                                                          | Yaru-Blue              |
| edit-paste.png                 | ![](images/edit-paste.png)                 |                                                          | Yaru-Blue              |
| edit-redo.png                  | ![](images/edit-redo.png)                  | ![](images/edit-redo-for-dark-theme.png)                 | Mark Ingrem            |
| edit-select-all.png            | ![](images/edit-select-all.png)            |                                                          | Yaru-Blue              |
| edit-undo.png                  | ![](images/edit-undo.png)                  | ![](images/edit-undo-for-dark-theme.png)                 | Mark Ingrem            |
| edit_book.png                  | ![](images/edit_book.png)                  |                                                          | Yaru-Blue              |
| edit_input.png                 | ![](images/edit_input.png)                 |                                                          | Yaru-Blue              |
| eject.png                      | ![](images/eject.png)                      |                                                          | Yaru-Blue              |
| embed-fonts.png                | ![](images/embed-fonts.png)                |                                                          | Yaru-Blue              |
| exec.png                       | ![](images/exec.png)                       |                                                          | Yaru-Blue              |
| external-link.png              | ![](images/external-link.png)              |                                                          | Yaru-Blue              |
| favicon-192.png                | ![](images/favicon-192.png)                |                                                          | Mark Ingrem            |
| favicon-512.png                | ![](images/favicon-512.png)                |                                                          | Mark Ingrem            |
| filter.png                     | ![](images/filter.png)                     | ![](images/filter-for-dark-theme.png)                    | Mark Ingrem            |
| folder_saved_search.png        | ![](images/folder_saved_search.png)        |                                                          | Yaru-Blue              |
| font.png                       | ![](images/font.png)                       |                                                          | Yaru-Blue              |
| font_size_larger.png           | ![](images/font_size_larger.png)           | ![](images/font_size_larger-for-dark-theme.png)          | Mark Ingrem            |
| font_size_smaller.png          | ![](images/font_size_smaller.png)          | ![](images/font_size_smaller-for-dark-theme.png)         | Mark Ingrem            |
| format-fill-color.png          | ![](images/format-fill-color.png)          | ![](images/format-fill-color-for-dark-theme.png)         | Mark Ingrem            |
| format-indent-less.png         | ![](images/format-indent-less.png)         |                                                          | Yaru-Blue              |
| format-indent-more.png         | ![](images/format-indent-more.png)         |                                                          | Yaru-Blue              |
| format-justify-center.png      | ![](images/format-justify-center.png)      |                                                          | Yaru-Blue              |
| format-justify-fill.png        | ![](images/format-justify-fill.png)        |                                                          | Yaru-Blue              |
| format-justify-left.png        | ![](images/format-justify-left.png)        |                                                          | Yaru-Blue              |
| format-justify-right.png       | ![](images/format-justify-right.png)       |                                                          | Yaru-Blue              |
| format-list-ordered.png        | ![](images/format-list-ordered.png)        | ![](images/format-list-ordered-for-dark-theme.png)       | Mark Ingrem            |
| format-list-unordered.png      | ![](images/format-list-unordered.png)      | ![](images/format-list-unordered-for-dark-theme.png)     | Mark Ingrem            |
| format-text-bold.png           | ![](images/format-text-bold.png)           | ![](images/format-text-bold-for-dark-theme.png)          | Yaru-Blue (customized) |
| format-text-color.png          | ![](images/format-text-color.png)          | ![](images/format-text-color-for-dark-theme.png)         | Mark Ingrem            |
| format-text-heading.png        | ![](images/format-text-heading.png)        | ![](images/format-text-heading-for-dark-theme.png)       | Mark Ingrem            |
| format-text-hr.png             | ![](images/format-text-hr.png)             | ![](images/format-text-hr-for-dark-theme.png)            | Mark Ingrem            |
| format-text-italic.png         | ![](images/format-text-italic.png)         | ![](images/format-text-italic-for-dark-theme.png)        | Yaru-Blue (customized) |
| format-text-strikethrough.png  | ![](images/format-text-strikethrough.png)  | ![](images/format-text-strikethrough-for-dark-theme.png) | Yaru-Blue (customized) |
| format-text-subscript.png      | ![](images/format-text-subscript.png)      | ![](images/format-text-subscript-for-dark-theme.png)     | Mark Ingrem            |
| format-text-superscript.png    | ![](images/format-text-superscript.png)    | ![](images/format-text-superscript-for-dark-theme.png)   | Mark Ingrem            |
| format-text-underline.png      | ![](images/format-text-underline.png)      | ![](images/format-text-underline-for-dark-theme.png)     | Yaru-Blue (customized) |
| forward.png                    | ![](images/forward.png)                    | ![](images/forward-for-dark-theme.png)                   | Mark Ingrem            |
| fts.png                        | ![](images/fts.png)                        |                                                          | Yaru-Blue (customized) |
| gear.png                       | ![](images/gear.png)                       | ![](images/gear-for-dark-theme.png)                      | Mark Ingrem            |
| generic-library.png            | ![](images/generic-library.png)            | ![](images/generic-library-for-dark-theme.png)           | Mark Ingrem            |
| gmail_logo.png                 | ![](images/gmail_logo.png)                 |                                                          | Mark Ingrem            |
| grid.png                       | ![](images/grid.png)                       |                                                          | Yaru-Blue              |
| h-ellipsis.png                 | ![](images/h-ellipsis.png)                 |                                                          | Yaru-Blue              |
| help.png                       | ![](images/help.png)                       |                                                          | Yaru-Blue              |
| heuristics.png                 | ![](images/heuristics.png)                 |                                                          | Yaru-Blue (customized) |
| highlight.png                  | ![](images/highlight.png)                  | ![](images/highlight-for-dark-theme.png)                 | Mark Ingrem            |
| highlight_only_off.png         | ![](images/highlight_only_off.png)         | ![](images/highlight_only_off-for-dark-theme.png)        | Mark Ingrem            |
| highlight_only_on.png          | ![](images/highlight_only_on.png)          | ![](images/highlight_only_on-for-dark-theme.png)         | Mark Ingrem            |
| hotmail.png                    | ![](images/hotmail.png)                    |                                                          | Mark Ingrem            |
| html-fix.png                   | ![](images/html-fix.png)                   |                                                          | Yaru-Blue (customized) |
| icon_choose.png                | ![](images/icon_choose.png)                |                                                          | Yaru-Blue              |
| identifiers.png                | ![](images/identifiers.png)                |                                                          | Mark Ingrem            |
| insert-link.png                | ![](images/insert-link.png)                | ![](images/insert-link-for-dark-theme.png)               | Mark Ingrem            |
| jobs.png                       | ![](images/jobs.png)                       | ![](images/jobs-for-dark-theme.png)                      | Mark Ingrem            |
| keyboard-prefs.png             | ![](images/keyboard-prefs.png)             |                                                          | Yaru-Blue              |
| languages.png                  | ![](images/languages.png)                  |                                                          | Yaru-Blue              |
| layout.png                     | ![](images/layout.png)                     |                                                          | Yaru-Blue              |
| library.png                    | ![](images/library.png)                    |                                                          | Mark Ingrem            |
| list_remove.png                | ![](images/list_remove.png)                | ![](images/list_remove-for-dark-theme.png)               | Mark Ingrem            |
| lookfeel.png                   | ![](images/lookfeel.png)                   |                                                          | Yaru-Blue              |
| lt.png                         | ![](images/lt.png)                         |                                                          | Mark Ingrem            |
| mail.png                       | ![](images/mail.png)                       |                                                          | Yaru-Blue              |
| marked.png                     | ![](images/marked.png)                     | ![](images/marked-for-dark-theme.png)                    | Mark Ingrem            |
| minus.png                      | ![](images/minus.png)                      | ![](images/minus-for-dark-theme.png)                     | Mark Ingrem            |
| minusminus.png                 | ![](images/minusminus.png)                 | ![](images/minusminus-for-dark-theme.png)                | Mark Ingrem            |
| network-server.png             | ![](images/network-server.png)             |                                                          | Yaru-Blue              |
| news.png                       | ![](images/news.png)                       |                                                          | Yaru-Blue              |
| next.png                       | ![](images/next.png)                       | ![](images/next-for-dark-theme.png)                      | Mark Ingrem            |
| notes.png                      | ![](images/notes.png)                      | ![](images/notes-for-dark-theme.png)                     | Mark Ingrem            |
| ok.png                         | ![](images/ok.png)                         | ![](images/ok-for-dark-theme.png)                        | Mark Ingrem            |
| plugboard.png                  | ![](images/plugboard.png)                  |                                                          | Yaru-Blue              |
| plugins.png                    | ![](images/plugins.png)                    |                                                          | Yaru-Blue              |
| plus.png                       | ![](images/plus.png)                       | ![](images/plus-for-dark-theme.png)                      | Mark Ingrem            |
| plusplus.png                   | ![](images/plusplus.png)                   | ![](images/plusplus-for-dark-theme.png)                  | Mark Ingrem            |
| previous.png                   | ![](images/previous.png)                   | ![](images/previous-for-dark-theme.png)                  | Mark Ingrem            |
| print-preview.png              | ![](images/print-preview.png)              |                                                          | Yaru-Blue              |
| print.png                      | ![](images/print.png)                      |                                                          | Yaru-Blue              |
| publisher.png                  | ![](images/publisher.png)                  |                                                          | Mark Ingrem            |
| quickview.png                  | ![](images/quickview.png)                  | ![](images/quickview-for-dark-theme.png)                 | Mark Ingrem            |
| reader.png                     | ![](images/reader.png)                     |                                                          | Yaru-Blue              |
| remove_books.png               | ![](images/remove_books.png)               |                                                          | Yaru-Blue              |
| reports.png                    | ![](images/reports.png)                    |                                                          | Yaru-Blue              |
| restart.png                    | ![](images/restart.png)                    |                                                          | Yaru-Blue              |
| rotate-right.png               | ![](images/rotate-right.png)               | ![](images/rotate-right-for-dark-theme.png)              | Mark Ingrem            |
| save.png                       | ![](images/save.png)                       |                                                          | Yaru-Blue              |
| scheduler.png                  | ![](images/scheduler.png)                  |                                                          | Yaru-Blue              |
| sd.png                         | ![](images/sd.png)                         |                                                          | Yaru-Blue              |
| search.png                     | ![](images/search.png)                     |                                                          | Yaru-Blue              |
| search_add_saved.png           | ![](images/search_add_saved.png)           |                                                          | Yaru-Blue              |
| search_delete_saved.png        | ![](images/search_delete_saved.png)        |                                                          | Yaru-Blue              |
| series.png                     | ![](images/series.png)                     |                                                          | Mark Ingrem            |
| store.png                      | ![](images/store.png)                      |                                                          | Yaru-Blue              |
| sync-right.png                 | ![](images/sync-right.png)                 | ![](images/sync-right-for-dark-theme.png)                | Mark Ingrem            |
| sync.png                       | ![](images/sync.png)                       |                                                          | Yaru-Blue              |
| tags.png                       | ![](images/tags.png)                       |                                                          | Mark Ingrem            |
| tb_folder.png                  | ![](images/tb_folder.png)                  |                                                          | Yaru-Blue              |
| template_funcs.png             | ![](images/template_funcs.png)             |                                                          | Yaru-Blue              |
| trash.png                      | ![](images/trash.png)                      |                                                          | Yaru-Blue              |
| trim.png                       | ![](images/trim.png)                       |                                                          | Yaru-Blue              |
| tweak.png                      | ![](images/tweak.png)                      |                                                          | Yaru-Blue              |
| tweaks.png                     | ![](images/tweaks.png)                     |                                                          | Yaru-Blue              |
| user_profile.png               | ![](images/user_profile.png)               |                                                          | Yaru-Blue              |
| v-ellipsis.png                 | ![](images/v-ellipsis.png)                 |                                                          | Yaru-Blue              |
| view-image.png                 | ![](images/view-image.png)                 |                                                          | Yaru-Blue              |
| view-refresh.png               | ![](images/view-refresh.png)               | ![](images/view-refresh-for-dark-theme.png)              | Mark Ingrem            |
| view.png                       | ![](images/view.png)                       |                                                          | Yaru-Blue              |
| viewer.png                     | ![](images/viewer.png)                     |                                                          | Yaru-Blue              |
| vl.png                         | ![](images/vl.png)                         |                                                          | Mark Ingrem            |
| window-close.png               | ![](images/window-close.png)               |                                                          | Yaru-Blue              |
| wizard.png                     | ![](images/wizard.png)                     |                                                          | Yaru-Blue              |

### Needs an update

| File name                      | Icon                                       | Source                 |
|--------------------------------|--------------------------------------------|------------------------|
| beautify.png                   | ![](images/beautify.png)                   | Calibre original icon  |
| book.png                       | ![](images/book.png)                       | Calibre original icon  |
| bookmarks.svg                  | ![](images/bookmarks.svg)                  | Yaru-Blue              |
| bookshelf.png                  | ![](images/bookshelf.png)                  | Calibre original icon  |
| catalog.png                    | ![](images/catalog.png)                    | Calibre original icon  |
| compress-image.png             | ![](images/compress-image.png)             | Calibre original icon  |
| copy-to-library.png            | ![](images/copy-to-library.png)            | Calibre original icon  |
| cover_flow.png                 | ![](images/cover_flow.png)                 | Calibre original icon  |
| cyoa.png                       | ![](images/cyoa.png)                       | Calibre original icon  |
| debug.svg                      | ![](images/debug.svg)                      | ???                    |
| default_cover.png              | ![](images/default_cover.png)              | Calibre original icon  |
| merge.png                      | ![](images/merge.png)                      | Calibre original icon  |
| merge_books.png                | ![](images/merge_books.png)                | Calibre original icon  |
| metadata.png                   | ![](images/metadata.png)                   | Calibre original icon  |
| modified-for-dark-theme.png    | ![](images/modified-for-dark-theme.png)    | Calibre original icon  |
| modified-for-light-theme.png   | ![](images/modified-for-light-theme.png)   | Calibre original icon  |
| page.svg                       | ![](images/page.svg)                       | ???                    |
| polish.png                     | ![](images/polish.png)                     | Calibre original icon  |
| random.png                     | ![](images/random.png)                     | Calibre original icon  |
| rating.png                     | ![](images/rating.png)                     | Yaru-Blue              |
| reference.png                  | ![](images/reference.png)                  | Calibre original icon  |
| resize.png                     | ![](images/resize.png)                     | Calibre original icon  |
| scene-divider.png              | ![](images/scene-divider.png)              | Calibre original icon  |
| scroll.png                     | ![](images/scroll.png)                     | Calibre original icon  |
| search_copy_saved.png          | ![](images/search_copy_saved.png)          | Calibre original icon  |
| send.png                       | ![](images/send.png)                       | Calibre original icon  |
| similar.png                    | ![](images/similar.png)                    | Calibre original icon  |
| smarten-punctuation.png        | ![](images/smarten-punctuation.png)        | Calibre original icon  |
| snippets.png                   | ![](images/snippets.png)                   | Calibre original icon  |
| sort.png                       | ![](images/sort.png)                       | Calibre original icon  |
| spell-check.png                | ![](images/spell-check.png)                | Yaru-Blue              |
| split.png                      | ![](images/split.png)                      | Calibre original icon  |
| subset-fonts.png               | ![](images/subset-fonts.png)               | Calibre original icon  |
| swap.png                       | ![](images/swap.png)                       | Calibre original icon  |
| toc.png                        | ![](images/toc.png)                        | Calibre original icon  |
| unpack-book.png                | ![](images/unpack-book.png)                | Calibre original icon  |
| width.png                      | ![](images/width.png)                      | Calibre original icon  |

### Unchanged

| File name                      | Icon                                       | Source                 |
|--------------------------------|--------------------------------------------|------------------------|
| blank.png                      | ![](images/blank.png)                      | Calibre original icon  |
