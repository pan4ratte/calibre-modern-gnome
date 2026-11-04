# Calibre Modern GNOME

This is a Calibre icon theme, a modern and a clean one. All themes, that are currently available in the Calibre icon store, are morally deprecated and should be replaced with some modern alternative. This is that alternative. See [CHANGELOG.md](CHANGELOG.md) for the changes in each release.

## Installation

The theme is not in calibre's icon theme list yet, so for now it is installed by hand:

1. Download this repository (Code → Download ZIP) and unpack it.
2. In calibre, open Preferences → Advanced → Miscellaneous → Open calibre configuration directory.
3. Copy the `images` folder from the download into the `resources` folder there (create `resources` if it does not exist).
4. Restart calibre.

Icons in that folder are used instead of any icon theme chosen in calibre. To go back to the default icons, delete `resources/images` and restart calibre.


## Key Principles

1. Use modern Ubuntu GNOME icons as much as it is possible, particularly Yaru-Blue version. I really like GNOME iteration of Ununtu Linux in terms of UI and try to implement their icons in Calibre interface. If there is a good Ubuntu GNOME icon for a certain UI element in Calibre, it should be prioritised for implementation. Yaru-Blue is my choice because it feels more more fitting in Calibre interface than others, if we speak of what is available in Yaru.

2. If there is no Ununtu GNOME icon that fits, use suitable icons from other themes available in the Calibre icon store. Some of these themes have good icons for certain UI elements, while not conflicting with modern GNOME style. If there is no suitable GNOME icon, you should try to find one in other themes. The key requirement is to avoid style conflicts with Yaru-Blue.

3. Use any other suitable open-source icons that do not conflict stylistically with modern GNOME icons. Sometimes there is no good icon for certain UI element in either Yaru-Blue or Calibre icon themes. In that case you should try to find a good open-source (or free for non-commercial use) icon alternative.

First stage of the project is to replace all default icons with something better. Second stage of the prject will be to redraw every non-Yaru icon on the Yaru style. 

## Icons Update Status and Source

The tables below represent the current update status of each icon in the collection and its source. There is one table per status, and the icons in each table are listed in alphabetical order. Status options:

1. "Updated": icon was successfully replaced;
2. "Needs an update": icon should be replaced with a modern alternative;
3. "Unable to update": icon is not replacable because it used for multiple, contradicting purposes in the Calibre UI. Such icons could be updated only after UI changes in the Calibre itself;
4. "Unchanged": icon do not need an update because it is good enough already.

### Updated

| File name                      | Icon                                       | Source                                    |
|--------------------------------|--------------------------------------------|-------------------------------------------|
| add_book.png                   | ![](images/add_book.png)                   | Ubuntu GNOME Yaru-Blue                    |
| apple-touch-icon.png           | ![](images/apple-touch-icon.png)           | Pan4ratte (Me)                            |
| book.png                       | ![](images/book.png)                       | Calibre original icon                     |
| bookmarks.svg                  | ![](images/bookmarks.svg)                  | Ubuntu GNOME Yaru-Blue                    |
| books_in_series.svg            | ![](images/books_in_series.svg)            | Ubuntu GNOME Yaru-Blue                    |
| character-set.png              | ![](images/character-set.png)              | Ubuntu GNOME Yaru-Blue                    |
| code.png                       | ![](images/code.png)                       | Ubuntu GNOME Yaru-Blue                    |
| column.png                     | ![](images/column.png)                     | Icons8 (???)                              |
| config.png                     | ![](images/config.png)                     | Ubuntu GNOME Yaru-Blue                    |
| connect_share.png              | ![](images/connect_share.png)              | Ubuntu GNOME Yaru-Blue (customized by me) |
| connect_share_on.png           | ![](images/connect_share_on.png)           | Ubuntu GNOME Yaru-Blue                    |
| context_menu.png               | ![](images/context_menu.png)               | Ubuntu GNOME Yaru-Blue                    |
| convert.png                    | ![](images/convert.png)                    | Ubuntu GNOME Yaru-Blue                    |
| debug.svg                      | ![](images/debug.svg)                      | ???                                       |
| dialog_error.png               | ![](images/dialog_error.png)               | Ubuntu GNOME Yaru-Blue                    |
| dialog_information.png         | ![](images/dialog_information.png)         | Ubuntu GNOME Yaru-Blue                    |
| dialog_question.png            | ![](images/dialog_question.png)            | Ubuntu GNOME Yaru-Blue                    |
| dialog_warning.png             | ![](images/dialog_warning.png)             | Ubuntu GNOME Yaru-Blue                    |
| dictionary.png                 | ![](images/dictionary.png)                 | Ubuntu GNOME Yaru-Blue                    |
| document_open.png              | ![](images/document_open.png)              | Ubuntu GNOME Yaru-Blue                    |
| document-encrypt.png           | ![](images/document-encrypt.png)           | Ubuntu GNOME Yaru-Blue                    |
| document-import.png            | ![](images/document-import.png)            | Ubuntu GNOME Yaru-Blue                    |
| document-new.png               | ![](images/document-new.png)               | Ubuntu GNOME Yaru-Blue                    |
| donate.svg                     | ![](images/donate.svg)                     | ???                                       |
| dot_green.svg                  | ![](images/dot_green.svg)                  | ???                                       |
| dot_red.svg                    | ![](images/dot_red.svg)                    | ???                                       |
| download-metadata.png          | ![](images/download-metadata.png)          | Ubuntu GNOME Yaru-Blue                    |
| drm-locked.svg                 | ![](images/drm-locked.svg)                 | ???                                       |
| drm-unlocked.svg               | ![](images/drm-unlocked.svg)               | ???                                       |
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
| font_size_larger.svg           | ![](images/font_size_larger.svg)           | ???                                       |
| font_size_smaller.svg          | ![](images/font_size_smaller.svg)          | ???                                       |
| format-fill-color.svg          | ![](images/format-fill-color.svg)          | ???                                       |
| format-indent-less.png         | ![](images/format-indent-less.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-indent-more.png         | ![](images/format-indent-more.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-justify-center.png      | ![](images/format-justify-center.png)      | Ubuntu GNOME Yaru-Blue                    |
| format-justify-fill.png        | ![](images/format-justify-fill.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-justify-left.png        | ![](images/format-justify-left.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-justify-right.png       | ![](images/format-justify-right.png)       | Ubuntu GNOME Yaru-Blue                    |
| format-list-ordered.png        | ![](images/format-list-ordered.png)        | Ubuntu GNOME Yaru-Blue                    |
| format-text-color.png          | ![](images/format-text-color.png)          | Ubuntu GNOME Yaru-Blue                    |
| format-text-italic.png         | ![](images/format-text-italic.png)         | Ubuntu GNOME Yaru-Blue                    |
| format-text-strikethrough.png  | ![](images/format-text-strikethrough.png)  | Ubuntu GNOME Yaru-Blue                    |
| format-text-underline.png      | ![](images/format-text-underline.png)      | Ubuntu GNOME Yaru-Blue                    |
| gmail_logo.svg                 | ![](images/gmail_logo.svg)                 | ???                                       |
| grid.png                       | ![](images/grid.png)                       | Ubuntu GNOME Yaru-Blue                    |
| h-ellipsis.png                 | ![](images/h-ellipsis.png)                 | Ubuntu GNOME Yaru-Blue                    |
| help.png                       | ![](images/help.png)                       | Ubuntu GNOME Yaru-Blue                    |
| hotmail.svg                    | ![](images/hotmail.svg)                    | ???                                       |
| icon_choose.png                | ![](images/icon_choose.png)                | Ubuntu GNOME Yaru-Blue                    |
| identifiers.png                | ![](images/identifiers.png)                | ???                                       |
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
| next.svg                       | ![](images/next.svg)                       | ???                                       |
| ok.svg                         | ![](images/ok.svg)                         | ???                                       |
| page.svg                       | ![](images/page.svg)                       | ???                                       |
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
| bullhorn.png                   | ![](images/bullhorn.png)                   | Calibre original icon                     |
| catalog.png                    | ![](images/catalog.png)                    | Calibre original icon                     |
| chapters.png                   | ![](images/chapters.png)                   | Calibre original icon                     |
| clear_left-for-dark-theme.png  | ![](images/clear_left-for-dark-theme.png)  | Calibre original icon                     |
| clear_left-for-light-theme.png | ![](images/clear_left-for-light-theme.png) | Calibre original icon                     |
| close-for-dark-theme.png       | ![](images/close-for-dark-theme.png)       | Calibre original icon                     |
| close-for-light-theme.png      | ![](images/close-for-light-theme.png)      | Calibre original icon                     |
| compress-image.png             | ![](images/compress-image.png)             | Calibre original icon                     |
| copy-to-library.png            | ![](images/copy-to-library.png)            | Calibre original icon                     |
| cover_flow.png                 | ![](images/cover_flow.png)                 | Calibre original icon                     |
| default_cover.png              | ![](images/default_cover.png)              | Calibre original icon                     |
| diff.png                       | ![](images/diff.png)                       | Calibre original icon                     |
| document-split.png             | ![](images/document-split.png)             | Calibre original icon                     |
| edit-clear.png                 | ![](images/edit-clear.png)                 | Calibre original icon                     |
| filter.png                     | ![](images/filter.png)                     | Calibre original icon                     |
| format-list-unordered.png      | ![](images/format-list-unordered.png)      | Calibre original icon                     |
| format-text-bold.png           | ![](images/format-text-bold.png)           | Calibre original icon                     |
| format-text-heading.png        | ![](images/format-text-heading.png)        | Calibre original icon                     |
| format-text-hr.png             | ![](images/format-text-hr.png)             | Calibre original icon                     |
| format-text-subscript.png      | ![](images/format-text-subscript.png)      | Calibre original icon                     |
| format-text-superscript.png    | ![](images/format-text-superscript.png)    | Calibre original icon                     |
| forward.png                    | ![](images/forward.png)                    | Calibre original icon                     |
| fts.png                        | ![](images/fts.png)                        | Calibre original icon                     |
| generic-library.png            | ![](images/generic-library.png)            | Calibre original icon                     |
| heuristics.png                 | ![](images/heuristics.png)                 | Calibre original icon                     |
| highlight.png                  | ![](images/highlight.png)                  | Calibre original icon                     |
| highlight_only_off.png         | ![](images/highlight_only_off.png)         | Calibre original icon                     |
| highlight_only_on.png          | ![](images/highlight_only_on.png)          | Calibre original icon                     |
| html-fix.png                   | ![](images/html-fix.png)                   | Calibre original icon                     |
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
| notes-for-dark-theme.png       | ![](images/notes-for-dark-theme.png)       | Calibre original icon                     |
| notes.png                      | ![](images/notes.png)                      | Calibre original icon                     |
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
