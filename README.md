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

## About the author

My name is Mark Ingrem. I build various tools for scientific research, and add-ons that make life easier for people using Obsidian and other programs. More of my projects can be found on my [GitHub](https://github.com/pan4ratte) page.

If Calibre Modern GNOME is useful to you, you can [support its development](https://pay.cloudtips.ru/p/c0e8eac4). The page takes cards issued in Russia.

## License

The theme is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE) (CC BY-SA 4.0), the same license as the Yaru icons it is based on.

- Yaru icons are made by the [Yaru team](https://github.com/ubuntu/yaru) and licensed under CC BY-SA 4.0. Customized Yaru icons are shared under the same license.
- Icons drawn for this project are licensed under CC BY-SA 4.0.
- Icons that are not replaced yet (the "Needs an update" table, and the empty `blank.png`) keep their original licenses. Most of them are calibre's original icons, which come with calibre under its own licenses. Icons with an unknown source ("???") will be replaced first.

## Icons Update Status and Source

The tables below represent the current update status of each icon in the collection and its source. There is one table per status, and the icons in each table are listed in alphabetical order. Status options:

1. "Updated": icon was replaced with a Yaru icon or an icon drawn in Yaru style;
2. "Needs an update": icon should be replaced with a Yaru icon or an icon drawn in Yaru style.

In the "Updated" table, the "Light theme" column shows the icon calibre uses in light mode, and the "Dark theme" column the version it uses in dark mode, for icons that have one.

### Updated

| File name                      | Light theme                                                  | Dark theme                                                                 | Source                 |
|--------------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|------------------------|
| add_book.png                   | <img src="images/add_book.png" width="96">                   |                                                                            | Yaru-Blue              |
| ai.png                         | <img src="images/ai.png" width="96">                         |                                                                            | Mark Ingrem            |
| apple-touch-icon.png           | <img src="images/apple-touch-icon.png" width="96">           |                                                                            | Mark Ingrem            |
| arrow-down.png                 | <img src="images/arrow-down.png" width="96">                 | <img src="images/arrow-down-for-dark-theme.png" width="96">                | Mark Ingrem            |
| arrow-up.png                   | <img src="images/arrow-up.png" width="96">                   | <img src="images/arrow-up-for-dark-theme.png" width="96">                  | Mark Ingrem            |
| auto-reload.png                | <img src="images/auto-reload.png" width="96">                | <img src="images/auto-reload-for-dark-theme.png" width="96">               | Mark Ingrem            |
| auto-scroll.png                | <img src="images/auto-scroll.png" width="96">                | <img src="images/auto-scroll-for-dark-theme.png" width="96">               | Mark Ingrem            |
| auto_author_sort.png           | <img src="images/auto_author_sort.png" width="96">           | <img src="images/auto_author_sort-for-dark-theme.png" width="96">          | Mark Ingrem            |
| back.png                       | <img src="images/back.png" width="96">                       | <img src="images/back-for-dark-theme.png" width="96">                      | Mark Ingrem            |
| blank.png                      | <img src="images/blank.png" width="96">                      |                                                                            | Calibre original icon  |
| books_in_series.png            | <img src="images/books_in_series.png" width="96">            |                                                                            | Mark Ingrem            |
| bullhorn.png                   | <img src="images/bullhorn.png" width="96">                   | <img src="images/bullhorn-for-dark-theme.png" width="96">                  | Mark Ingrem            |
| calibre.png                    | <img src="images/calibre.png" width="96">                    |                                                                            | Mark Ingrem            |
| chapters.png                   | <img src="images/chapters.png" width="96">                   | <img src="images/chapters-for-dark-theme.png" width="96">                  | Mark Ingrem            |
| character-set.png              | <img src="images/character-set.png" width="96">              |                                                                            | Yaru-Blue              |
| clear_left-for-light-theme.png | <img src="images/clear_left-for-light-theme.png" width="96"> | <img src="images/clear_left-for-dark-theme.png" width="96">                | Mark Ingrem            |
| close-for-light-theme.png      | <img src="images/close-for-light-theme.png" width="96">      | <img src="images/close-for-dark-theme.png" width="96">                     | Mark Ingrem            |
| code.png                       | <img src="images/code.png" width="96">                       |                                                                            | Yaru-Blue              |
| column.png                     | <img src="images/column.png" width="96">                     |                                                                            | Mark Ingrem            |
| config.png                     | <img src="images/config.png" width="96">                     |                                                                            | Yaru-Blue              |
| connect_share.png              | <img src="images/connect_share.png" width="96">              |                                                                            | Yaru-Blue (customized) |
| connect_share_on.png           | <img src="images/connect_share_on.png" width="96">           |                                                                            | Yaru-Blue              |
| context_menu.png               | <img src="images/context_menu.png" width="96">               |                                                                            | Yaru-Blue              |
| convert.png                    | <img src="images/convert.png" width="96">                    |                                                                            | Yaru-Blue              |
| dialog_error.png               | <img src="images/dialog_error.png" width="96">               |                                                                            | Yaru-Blue              |
| dialog_information.png         | <img src="images/dialog_information.png" width="96">         |                                                                            | Yaru-Blue              |
| dialog_question.png            | <img src="images/dialog_question.png" width="96">            |                                                                            | Yaru-Blue              |
| dialog_warning.png             | <img src="images/dialog_warning.png" width="96">             |                                                                            | Yaru-Blue              |
| dictionary.png                 | <img src="images/dictionary.png" width="96">                 |                                                                            | Yaru-Blue              |
| diff.png                       | <img src="images/diff.png" width="96">                       | <img src="images/diff-for-dark-theme.png" width="96">                      | Mark Ingrem            |
| document-encrypt.png           | <img src="images/document-encrypt.png" width="96">           |                                                                            | Yaru-Blue              |
| document-import.png            | <img src="images/document-import.png" width="96">            |                                                                            | Yaru-Blue              |
| document-new.png               | <img src="images/document-new.png" width="96">               |                                                                            | Yaru-Blue              |
| document-split.png             | <img src="images/document-split.png" width="96">             | <img src="images/document-split-for-dark-theme.png" width="96">            | Mark Ingrem            |
| document_open.png              | <img src="images/document_open.png" width="96">              |                                                                            | Yaru-Blue              |
| donate.png                     | <img src="images/donate.png" width="96">                     |                                                                            | Mark Ingrem            |
| dot_green.png                  | <img src="images/dot_green.png" width="96">                  |                                                                            | Yaru-Blue (customized) |
| dot_red.png                    | <img src="images/dot_red.png" width="96">                    |                                                                            | Yaru-Blue (customized) |
| download-metadata.png          | <img src="images/download-metadata.png" width="96">          |                                                                            | Yaru-Blue              |
| drm-locked.png                 | <img src="images/drm-locked.png" width="96">                 |                                                                            | Yaru-Blue (customized) |
| drm-unlocked.png               | <img src="images/drm-unlocked.png" width="96">               |                                                                            | Yaru-Blue (customized) |
| edit-clear.png                 | <img src="images/edit-clear.png" width="96">                 | <img src="images/edit-clear-for-dark-theme.png" width="96">                | Mark Ingrem            |
| edit-copy.png                  | <img src="images/edit-copy.png" width="96">                  |                                                                            | Yaru-Blue              |
| edit-cut.png                   | <img src="images/edit-cut.png" width="96">                   |                                                                            | Yaru-Blue              |
| edit-paste.png                 | <img src="images/edit-paste.png" width="96">                 |                                                                            | Yaru-Blue              |
| edit-redo.png                  | <img src="images/edit-redo.png" width="96">                  | <img src="images/edit-redo-for-dark-theme.png" width="96">                 | Mark Ingrem            |
| edit-select-all.png            | <img src="images/edit-select-all.png" width="96">            |                                                                            | Yaru-Blue              |
| edit-undo.png                  | <img src="images/edit-undo.png" width="96">                  | <img src="images/edit-undo-for-dark-theme.png" width="96">                 | Mark Ingrem            |
| edit_book.png                  | <img src="images/edit_book.png" width="96">                  |                                                                            | Yaru-Blue              |
| edit_input.png                 | <img src="images/edit_input.png" width="96">                 |                                                                            | Yaru-Blue              |
| eject.png                      | <img src="images/eject.png" width="96">                      |                                                                            | Yaru-Blue              |
| embed-fonts.png                | <img src="images/embed-fonts.png" width="96">                |                                                                            | Yaru-Blue              |
| exec.png                       | <img src="images/exec.png" width="96">                       |                                                                            | Yaru-Blue              |
| external-link.png              | <img src="images/external-link.png" width="96">              |                                                                            | Yaru-Blue              |
| favicon-192.png                | <img src="images/favicon-192.png" width="96">                |                                                                            | Mark Ingrem            |
| favicon-512.png                | <img src="images/favicon-512.png" width="96">                |                                                                            | Mark Ingrem            |
| filter.png                     | <img src="images/filter.png" width="96">                     | <img src="images/filter-for-dark-theme.png" width="96">                    | Mark Ingrem            |
| folder_saved_search.png        | <img src="images/folder_saved_search.png" width="96">        |                                                                            | Yaru-Blue              |
| font.png                       | <img src="images/font.png" width="96">                       |                                                                            | Yaru-Blue              |
| font_size_larger.png           | <img src="images/font_size_larger.png" width="96">           | <img src="images/font_size_larger-for-dark-theme.png" width="96">          | Mark Ingrem            |
| font_size_smaller.png          | <img src="images/font_size_smaller.png" width="96">          | <img src="images/font_size_smaller-for-dark-theme.png" width="96">         | Mark Ingrem            |
| format-fill-color.png          | <img src="images/format-fill-color.png" width="96">          | <img src="images/format-fill-color-for-dark-theme.png" width="96">         | Mark Ingrem            |
| format-indent-less.png         | <img src="images/format-indent-less.png" width="96">         |                                                                            | Yaru-Blue              |
| format-indent-more.png         | <img src="images/format-indent-more.png" width="96">         |                                                                            | Yaru-Blue              |
| format-justify-center.png      | <img src="images/format-justify-center.png" width="96">      |                                                                            | Yaru-Blue              |
| format-justify-fill.png        | <img src="images/format-justify-fill.png" width="96">        |                                                                            | Yaru-Blue              |
| format-justify-left.png        | <img src="images/format-justify-left.png" width="96">        |                                                                            | Yaru-Blue              |
| format-justify-right.png       | <img src="images/format-justify-right.png" width="96">       |                                                                            | Yaru-Blue              |
| format-list-ordered.png        | <img src="images/format-list-ordered.png" width="96">        | <img src="images/format-list-ordered-for-dark-theme.png" width="96">       | Mark Ingrem            |
| format-list-unordered.png      | <img src="images/format-list-unordered.png" width="96">      | <img src="images/format-list-unordered-for-dark-theme.png" width="96">     | Mark Ingrem            |
| format-text-bold.png           | <img src="images/format-text-bold.png" width="96">           | <img src="images/format-text-bold-for-dark-theme.png" width="96">          | Yaru-Blue (customized) |
| format-text-color.png          | <img src="images/format-text-color.png" width="96">          | <img src="images/format-text-color-for-dark-theme.png" width="96">         | Mark Ingrem            |
| format-text-heading.png        | <img src="images/format-text-heading.png" width="96">        | <img src="images/format-text-heading-for-dark-theme.png" width="96">       | Mark Ingrem            |
| format-text-hr.png             | <img src="images/format-text-hr.png" width="96">             | <img src="images/format-text-hr-for-dark-theme.png" width="96">            | Mark Ingrem            |
| format-text-italic.png         | <img src="images/format-text-italic.png" width="96">         | <img src="images/format-text-italic-for-dark-theme.png" width="96">        | Yaru-Blue (customized) |
| format-text-strikethrough.png  | <img src="images/format-text-strikethrough.png" width="96">  | <img src="images/format-text-strikethrough-for-dark-theme.png" width="96"> | Yaru-Blue (customized) |
| format-text-subscript.png      | <img src="images/format-text-subscript.png" width="96">      | <img src="images/format-text-subscript-for-dark-theme.png" width="96">     | Mark Ingrem            |
| format-text-superscript.png    | <img src="images/format-text-superscript.png" width="96">    | <img src="images/format-text-superscript-for-dark-theme.png" width="96">   | Mark Ingrem            |
| format-text-underline.png      | <img src="images/format-text-underline.png" width="96">      | <img src="images/format-text-underline-for-dark-theme.png" width="96">     | Yaru-Blue (customized) |
| forward.png                    | <img src="images/forward.png" width="96">                    | <img src="images/forward-for-dark-theme.png" width="96">                   | Mark Ingrem            |
| fts.png                        | <img src="images/fts.png" width="96">                        |                                                                            | Yaru-Blue (customized) |
| gear.png                       | <img src="images/gear.png" width="96">                       | <img src="images/gear-for-dark-theme.png" width="96">                      | Mark Ingrem            |
| generic-library.png            | <img src="images/generic-library.png" width="96">            | <img src="images/generic-library-for-dark-theme.png" width="96">           | Mark Ingrem            |
| gmail_logo.png                 | <img src="images/gmail_logo.png" width="96">                 |                                                                            | Mark Ingrem            |
| grid.png                       | <img src="images/grid.png" width="96">                       |                                                                            | Yaru-Blue              |
| h-ellipsis.png                 | <img src="images/h-ellipsis.png" width="96">                 |                                                                            | Yaru-Blue              |
| help.png                       | <img src="images/help.png" width="96">                       |                                                                            | Yaru-Blue              |
| heuristics.png                 | <img src="images/heuristics.png" width="96">                 |                                                                            | Yaru-Blue (customized) |
| highlight.png                  | <img src="images/highlight.png" width="96">                  | <img src="images/highlight-for-dark-theme.png" width="96">                 | Mark Ingrem            |
| highlight_only_off.png         | <img src="images/highlight_only_off.png" width="96">         | <img src="images/highlight_only_off-for-dark-theme.png" width="96">        | Mark Ingrem            |
| highlight_only_on.png          | <img src="images/highlight_only_on.png" width="96">          | <img src="images/highlight_only_on-for-dark-theme.png" width="96">         | Mark Ingrem            |
| hotmail.png                    | <img src="images/hotmail.png" width="96">                    |                                                                            | Mark Ingrem            |
| html-fix.png                   | <img src="images/html-fix.png" width="96">                   |                                                                            | Yaru-Blue (customized) |
| icon_choose.png                | <img src="images/icon_choose.png" width="96">                |                                                                            | Yaru-Blue              |
| identifiers.png                | <img src="images/identifiers.png" width="96">                |                                                                            | Mark Ingrem            |
| insert-link.png                | <img src="images/insert-link.png" width="96">                | <img src="images/insert-link-for-dark-theme.png" width="96">               | Mark Ingrem            |
| jobs.png                       | <img src="images/jobs.png" width="96">                       | <img src="images/jobs-for-dark-theme.png" width="96">                      | Mark Ingrem            |
| keyboard-prefs.png             | <img src="images/keyboard-prefs.png" width="96">             |                                                                            | Yaru-Blue              |
| languages.png                  | <img src="images/languages.png" width="96">                  |                                                                            | Yaru-Blue              |
| layout.png                     | <img src="images/layout.png" width="96">                     |                                                                            | Yaru-Blue              |
| library.png                    | <img src="images/library.png" width="96">                    |                                                                            | Mark Ingrem            |
| list_remove.png                | <img src="images/list_remove.png" width="96">                | <img src="images/list_remove-for-dark-theme.png" width="96">               | Mark Ingrem            |
| lookfeel.png                   | <img src="images/lookfeel.png" width="96">                   |                                                                            | Yaru-Blue              |
| lt.png                         | <img src="images/lt.png" width="96">                         |                                                                            | Mark Ingrem            |
| mail.png                       | <img src="images/mail.png" width="96">                       |                                                                            | Yaru-Blue              |
| marked.png                     | <img src="images/marked.png" width="96">                     | <img src="images/marked-for-dark-theme.png" width="96">                    | Mark Ingrem            |
| minus.png                      | <img src="images/minus.png" width="96">                      | <img src="images/minus-for-dark-theme.png" width="96">                     | Mark Ingrem            |
| minusminus.png                 | <img src="images/minusminus.png" width="96">                 | <img src="images/minusminus-for-dark-theme.png" width="96">                | Mark Ingrem            |
| network-server.png             | <img src="images/network-server.png" width="96">             |                                                                            | Yaru-Blue              |
| news.png                       | <img src="images/news.png" width="96">                       |                                                                            | Yaru-Blue              |
| next.png                       | <img src="images/next.png" width="96">                       | <img src="images/next-for-dark-theme.png" width="96">                      | Mark Ingrem            |
| notes.png                      | <img src="images/notes.png" width="96">                      | <img src="images/notes-for-dark-theme.png" width="96">                     | Mark Ingrem            |
| ok.png                         | <img src="images/ok.png" width="96">                         | <img src="images/ok-for-dark-theme.png" width="96">                        | Mark Ingrem            |
| plugboard.png                  | <img src="images/plugboard.png" width="96">                  |                                                                            | Yaru-Blue              |
| plugins.png                    | <img src="images/plugins.png" width="96">                    |                                                                            | Yaru-Blue              |
| plus.png                       | <img src="images/plus.png" width="96">                       | <img src="images/plus-for-dark-theme.png" width="96">                      | Mark Ingrem            |
| plusplus.png                   | <img src="images/plusplus.png" width="96">                   | <img src="images/plusplus-for-dark-theme.png" width="96">                  | Mark Ingrem            |
| previous.png                   | <img src="images/previous.png" width="96">                   | <img src="images/previous-for-dark-theme.png" width="96">                  | Mark Ingrem            |
| print-preview.png              | <img src="images/print-preview.png" width="96">              |                                                                            | Yaru-Blue              |
| print.png                      | <img src="images/print.png" width="96">                      |                                                                            | Yaru-Blue              |
| publisher.png                  | <img src="images/publisher.png" width="96">                  |                                                                            | Mark Ingrem            |
| quickview.png                  | <img src="images/quickview.png" width="96">                  | <img src="images/quickview-for-dark-theme.png" width="96">                 | Mark Ingrem            |
| reader.png                     | <img src="images/reader.png" width="96">                     |                                                                            | Yaru-Blue              |
| remove_books.png               | <img src="images/remove_books.png" width="96">               |                                                                            | Yaru-Blue              |
| reports.png                    | <img src="images/reports.png" width="96">                    |                                                                            | Yaru-Blue              |
| restart.png                    | <img src="images/restart.png" width="96">                    |                                                                            | Yaru-Blue              |
| rotate-right.png               | <img src="images/rotate-right.png" width="96">               | <img src="images/rotate-right-for-dark-theme.png" width="96">              | Mark Ingrem            |
| save.png                       | <img src="images/save.png" width="96">                       |                                                                            | Yaru-Blue              |
| scheduler.png                  | <img src="images/scheduler.png" width="96">                  |                                                                            | Yaru-Blue              |
| sd.png                         | <img src="images/sd.png" width="96">                         |                                                                            | Yaru-Blue              |
| search.png                     | <img src="images/search.png" width="96">                     |                                                                            | Yaru-Blue              |
| search_add_saved.png           | <img src="images/search_add_saved.png" width="96">           |                                                                            | Yaru-Blue              |
| search_delete_saved.png        | <img src="images/search_delete_saved.png" width="96">        |                                                                            | Yaru-Blue              |
| series.png                     | <img src="images/series.png" width="96">                     |                                                                            | Mark Ingrem            |
| store.png                      | <img src="images/store.png" width="96">                      |                                                                            | Yaru-Blue              |
| sync-right.png                 | <img src="images/sync-right.png" width="96">                 | <img src="images/sync-right-for-dark-theme.png" width="96">                | Mark Ingrem            |
| sync.png                       | <img src="images/sync.png" width="96">                       |                                                                            | Yaru-Blue              |
| tags.png                       | <img src="images/tags.png" width="96">                       |                                                                            | Mark Ingrem            |
| tb_folder.png                  | <img src="images/tb_folder.png" width="96">                  |                                                                            | Yaru-Blue              |
| template_funcs.png             | <img src="images/template_funcs.png" width="96">             |                                                                            | Yaru-Blue              |
| trash.png                      | <img src="images/trash.png" width="96">                      |                                                                            | Yaru-Blue              |
| trim.png                       | <img src="images/trim.png" width="96">                       |                                                                            | Yaru-Blue              |
| tweak.png                      | <img src="images/tweak.png" width="96">                      |                                                                            | Yaru-Blue              |
| tweaks.png                     | <img src="images/tweaks.png" width="96">                     |                                                                            | Yaru-Blue              |
| user_profile.png               | <img src="images/user_profile.png" width="96">               |                                                                            | Yaru-Blue              |
| v-ellipsis.png                 | <img src="images/v-ellipsis.png" width="96">                 |                                                                            | Yaru-Blue              |
| view-image.png                 | <img src="images/view-image.png" width="96">                 |                                                                            | Yaru-Blue              |
| view-refresh.png               | <img src="images/view-refresh.png" width="96">               | <img src="images/view-refresh-for-dark-theme.png" width="96">              | Mark Ingrem            |
| view.png                       | <img src="images/view.png" width="96">                       |                                                                            | Yaru-Blue              |
| viewer.png                     | <img src="images/viewer.png" width="96">                     |                                                                            | Yaru-Blue              |
| vl.png                         | <img src="images/vl.png" width="96">                         |                                                                            | Mark Ingrem            |
| window-close.png               | <img src="images/window-close.png" width="96">               |                                                                            | Yaru-Blue              |
| wizard.png                     | <img src="images/wizard.png" width="96">                     |                                                                            | Yaru-Blue              |

### Needs an update

| File name                    | Icon                                                       | Source                |
|------------------------------|:----------------------------------------------------------:|-----------------------|
| beautify.png                 | <img src="images/beautify.png" width="96">                 | Calibre original icon |
| book.png                     | <img src="images/book.png" width="96">                     | Calibre original icon |
| bookmarks.svg                | <img src="images/bookmarks.svg" width="96">                | Yaru-Blue             |
| bookshelf.png                | <img src="images/bookshelf.png" width="96">                | Calibre original icon |
| catalog.png                  | <img src="images/catalog.png" width="96">                  | Calibre original icon |
| compress-image.png           | <img src="images/compress-image.png" width="96">           | Calibre original icon |
| copy-to-library.png          | <img src="images/copy-to-library.png" width="96">          | Calibre original icon |
| cover_flow.png               | <img src="images/cover_flow.png" width="96">               | Calibre original icon |
| cyoa.png                     | <img src="images/cyoa.png" width="96">                     | Calibre original icon |
| debug.svg                    | <img src="images/debug.svg" width="96">                    | ???                   |
| default_cover.png            | <img src="images/default_cover.png" width="96">            | Calibre original icon |
| merge.png                    | <img src="images/merge.png" width="96">                    | Calibre original icon |
| merge_books.png              | <img src="images/merge_books.png" width="96">              | Calibre original icon |
| metadata.png                 | <img src="images/metadata.png" width="96">                 | Calibre original icon |
| modified-for-dark-theme.png  | <img src="images/modified-for-dark-theme.png" width="96">  | Calibre original icon |
| modified-for-light-theme.png | <img src="images/modified-for-light-theme.png" width="96"> | Calibre original icon |
| page.svg                     | <img src="images/page.svg" width="96">                     | ???                   |
| polish.png                   | <img src="images/polish.png" width="96">                   | Calibre original icon |
| random.png                   | <img src="images/random.png" width="96">                   | Calibre original icon |
| rating.png                   | <img src="images/rating.png" width="96">                   | Yaru-Blue             |
| reference.png                | <img src="images/reference.png" width="96">                | Calibre original icon |
| resize.png                   | <img src="images/resize.png" width="96">                   | Calibre original icon |
| scene-divider.png            | <img src="images/scene-divider.png" width="96">            | Calibre original icon |
| scroll.png                   | <img src="images/scroll.png" width="96">                   | Calibre original icon |
| search_copy_saved.png        | <img src="images/search_copy_saved.png" width="96">        | Calibre original icon |
| send.png                     | <img src="images/send.png" width="96">                     | Calibre original icon |
| similar.png                  | <img src="images/similar.png" width="96">                  | Calibre original icon |
| smarten-punctuation.png      | <img src="images/smarten-punctuation.png" width="96">      | Calibre original icon |
| snippets.png                 | <img src="images/snippets.png" width="96">                 | Calibre original icon |
| sort.png                     | <img src="images/sort.png" width="96">                     | Calibre original icon |
| spell-check.png              | <img src="images/spell-check.png" width="96">              | Yaru-Blue             |
| split.png                    | <img src="images/split.png" width="96">                    | Calibre original icon |
| subset-fonts.png             | <img src="images/subset-fonts.png" width="96">             | Calibre original icon |
| swap.png                     | <img src="images/swap.png" width="96">                     | Calibre original icon |
| toc.png                      | <img src="images/toc.png" width="96">                      | Calibre original icon |
| unpack-book.png              | <img src="images/unpack-book.png" width="96">              | Calibre original icon |
| width.png                    | <img src="images/width.png" width="96">                    | Calibre original icon |
