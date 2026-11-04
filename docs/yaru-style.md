# Yaru style guide for this theme

Yaru's own design drives every icon in this theme. This guide has four parts: the general approach, which comes first and applies to every icon; Yaru's palette and sources; rules agreed for particular families of icons, which apply only to icons of that family; and how to work with Illustrator.

## General approach

1. **If Yaru already has the icon, use it.** Take Yaru's 256 px PNG.
2. **Match the closest Yaru icons.** Find the Yaru icons nearest to the new one: the same context (actions, apps, categories, devices, emblems, mimetypes, places, status) and a similar meaning. Draw the new icon the way they are drawn: shape language, colors, shading, size on the canvas, outline. A device icon should look like Yaru's device icons, a folder like its places icons, a toolbar action like its action icons. Yaru builds on the [Suru](https://snwh.org/suru) icons of Ubuntu Touch, so Suru icons are the next reference.
3. **Build it the way Yaru does.** Yaru requires new full-color icons to start from an existing Yaru icon or from one of its templates (`icons/src/fullcolor/`: blank, square, round and oblong app icons, mimetype, legacy action). Its templates are organized in layers: Background (the color), Pictogram (the symbol), Folds, Highlights, Shadows and Emblems.
4. **Pick the idea.** Use Yaru's symbolic icon for the same action when there is one. If not, keep the idea of calibre's original icon. If that doesn't work either, use the most common design for that action (a paint bucket for fill color).
5. **Use Yaru's colors.** Take colors from Yaru's palette (below) or from the Yaru icons being matched.
6. **Make it make sense.** Drawings must be physically plausible: a pouring bucket's liquid is level and reaches the spout the drop comes from; an eraser touches the line it erases.
7. **Ask when unsure.** If it isn't clear which approach fits an icon, ask the user before drawing. For example: which Yaru icons to match, Yaru's symbol or calibre's idea, color or neutral, drawn in code or in Illustrator. Show the options rather than picking one silently.
8. **Check it.** Look at every icon on light and dark backgrounds and at 16, 24, 32 and 48 px before calling it done.

## Yaru's palette

From `icons/src/Yaru.gpl`, Yaru's Inkscape palette. Each family has five shades, 01 darkest to 05 lightest.

| Family | 01 | 02 | 03 | 04 | 05 |
|---|---|---|---|---|---|
| Aubergine | #62237C | #9B33AE | #C43AC4 | #D85ECA | #E97CC8 |
| Purple | #7839B7 | #8C59D9 | #8F76E4 | #A7A7F1 | #C5C9F5 |
| Deep Blue | #234DB8 | #2F5FDD | #5884F4 | #80A3FA | #A2BCFE |
| Blue | #1463A5 | #1A7FD4 | #37A6E6 | #6DC7F1 | #AEE3F8 |
| Turquoise | #2B898F | #2DAAAA | #31C6B7 | #5BDBC1 | #81E9C0 |
| Green | #28851E | #46A926 | #76C22B | #A6D74F | #CBE667 |
| Yellow | #EAB305 | #FDC92B | #FFDA64 | #FEE581 | #FFF4C9 |
| Orange | #D64310 | #F34F17 | #FB7C38 | #FDA463 | #FEC589 |
| Red | #BC1938 | #DA1636 | #F22C42 | #F76363 | #FA9381 |
| Beige | #AEA795 | #C8C4B7 | #E3DFD5 | #F1F0E9 | #FAF8F6 |

Neutrals: Jet #111111, Inkstone #3B3B3B, Slate #5D5D5D, Graphite #666666, Ash #888888, Silk #CDCDCD, Porcelain #F7F7F7, White #FFFFFF. Ubuntu brand colors: Orange #E95420, Blue #19B6EE, Green #3EB34F, Red #ED3146.

## Where Yaru's sources are

All in [github.com/ubuntu/yaru](https://github.com/ubuntu/yaru), licensed CC BY-SA 4.0:

| What | Path | Use it for |
|---|---|---|
| Full-color sources | `icons/src/fullcolor/default/<context>/<name>.svg` | The look: shapes, gradients, outlines. Each file holds the 16, 24, 32, 48 and 256 px versions side by side; the 256 px one is the 256×256 square at x 24, y 28. |
| Full-color PNGs | `icons/Yaru/256x256/<context>/<name>.png` | Icons Yaru already has: use them as they are. |
| Symbolic icons | `icons/src/scalable/default/<context>/<name>-symbolic.svg` | The idea, when Yaru has no full-color icon for it (16 px, one color). |
| Old full-color actions | `icons/src/fullcolor/default/legacy/` | Badges and bullets: `list-add`, `list-remove`. |
| Templates and Yaru's rules | `icons/src/fullcolor/README.md`, `icons/CONTRIBUTING.md` | |
| Palette | `icons/src/Yaru.gpl` | |

Yaru's own rules that matter here: new full-color icons start from a template or an existing Yaru icon; names follow the freedesktop icon naming spec; Yaru draws in Inkscape and warns that other editors add their own elements to SVG files, so anything made elsewhere must be saved as plain SVG (see [Working in Illustrator](#working-in-illustrator)).

## Canvas

- One 256×256 image per icon. calibre takes a single image and scales it, so unlike Yaru there are no separate small-size drawings. Draw in `src/<icon-name>.svg` with `viewBox="0 0 256 256"`; `tools\theme.cmd render` makes the PNG.
- Use the space the Yaru icons being matched use. Yaru's action icons keep their drawing inside about 32..224 px; its letters run from 21 to 234 px with their outline.

## Rules for icon families

These rules were measured from Yaru and agreed with the user for one family of icons each. They apply only to that family. Add a new section here when a new family's rules are agreed.

### Text formatting and editing actions

Toolbar icons for working with text: bold, italic, underline, strikethrough, heading, subscript, superscript, lists, alignment, indent, horizontal rule, text and background color, font size, clear. They match Yaru's 256 px `format-text-*`, `format-justify-*` and `format-indent-*` icons, and its legacy `list-add` and `list-remove`. Working examples: the matching files in `src/`.

- **Neutral by default.** Glyphs and solid shapes use a linear gradient from #4d4d4d at the top left to #151515 at the bottom right (`x1="1" y1="1" x2="0" y2="0"`: stop 0 #151515, stop 1 #4d4d4d), with a 4 px white outline: a white copy of the shape with an 8 px white stroke and round joins, under the shape. The outline keeps them readable on dark backgrounds.
- **A dark mode version of each icon**, `<name>-for-dark-theme.png`, which calibre uses instead in dark mode. It has the same drawing with the neutral colors inverted: #151515 → #d5d5d5, #4d4d4d → #f7f7f7 (the lighter end of a gradient stays lighter), the white outline → #232629, light surfaces → the dark glyph gradient, and #232629 text lines → #e5e5e5 (their white copy below → #232629). Colors that mean something (badges, swatch, blue) and the white signs on badges stay as they are. Icons drawn here get a `src/<name>-for-dark-theme.svg` next to the light source. For Yaru's own icons, the source is the 256 px drawing from Yaru's full-color source with the same color changes, and the light version stays Yaru's PNG.
- **Text lines.** #232629 bars, 8 px high, with a white copy of each bar 8 px below it. In a paragraph they repeat every 24 px; full lines are 192 px long from x 32, shorter ones 160 or 128 px.
- **Light surfaces** (inside of a bucket, an eraser's rubber): a gradient from #f7f7f7 at the top left to #d5d5d5 at the bottom right; next to white, a thin #232629 edge.
- **Letters and digits.** The Ubuntu font, as in Yaru. Ubuntu Bold for letters and digits (heading "H", subscript "x", list numbers). The "A" in the text color and font size icons is the Ubuntu Medium "A" from Yaru's `font-color-symbolic.svg`. Letters that stand alone are as tall as Yaru's B, I, U: about 206 px.
- **Color only where it means something.**

  | Color | Values | Means | Used in |
  |---|---|---|---|
  | Yaru Blue 02 → 03 | gradient #1a7fd4 → #37a6e6 (Yaru's `list-remove` bullets) | the thing the button inserts or moves | list bullets, the "2" in subscript and superscript, the horizontal rule |
  | Yaru Green 02 | #45a925 (Yaru's `list-add`) | add, more | plus badges |
  | Ubuntu red | #c7162b (Yaru's `list-remove`); as a gradient #a51d2d → #e2364c | remove, less; the text color | minus badges, the text color swatch |

  Buttons about color in general (background color) or used in many places (clear) stay neutral.
- **Layout.** Lists have three rows centered at y 52, 124 and 196; the marker column is 32..80 (digits centered in it, bullets are 32 px circles centered at x 56), and the text lines run from x 96 to 224. Yaru's `list-remove` puts its bullets at the same rows. Badges (plus, minus, color swatch) sit at the bottom right, over the main shape, with the same 4 px white outline.

### Basic action symbols

Small generic symbols and buttons that calibre uses in many places: OK, plus, minus, double plus and minus, next, previous, back, forward, up, down, close, remove, clear, refresh, auto reload, rotate, auto scroll, sort, read aloud, link, compare, split. Working examples: the matching files in `src/`.

- **Neutral, never colored.** Not Yaru's colored round buttons (`dialog-apply`, `list-add`): draw them the same way as the text formatting glyphs above, with the dark gradient and the 4 px white outline.
- **A dark mode version of each**, made as for the text formatting icons.
- **Shapes from Yaru's symbolic icons**, scaled up: `object-select` for OK, `list-add` and `list-remove` for plus and minus, `go-next` and `go-previous` (a tall chevron, ends cut flat) for next and previous, and for back and forward too, as in Yaru. `window-close` (a plain X) for close, `edit-clear` (an outlined backspace tag with an X) for clear, `view-refresh` for reload, `emblem-synchronizing` (two arrows round a circle, turned clockwise like reload) for refresh, `object-rotate-right` for rotate, `pan-down` chevrons for scroll, `view-sort-descending` for sort, `audio-volume-high` for read aloud, `insert-link` (two links and a bar, set on the diagonal, without the insert triangle) for links. Without a Yaru symbol, keep calibre's idea (two pages for compare, a page cut in two for split).
- **Reuse shapes for the same idea.** Up and down are the next chevron turned, remove is the close X (it pairs with the OK check mark as yes / no), sync to the right is the next chevron.
- **Strokes** are 24 to 32 px wide, and a single symbol spans 160 to 192 px. The double symbols keep calibre's layout, two symbols on a diagonal (centers at 168,88 and 88,168), each 112 px long with 28 px strokes.
- **Filled shapes, sharp corners.** Draw lines as filled shapes (an X is the plus turned 45°, a ring segment is two arcs joined), not as stroked paths: a stroke's white outline stops at its ends and leaves them unfinished. Corners and joins are sharp and line ends are cut flat, as in the chevrons; no round caps. Parts of one object can be drawn as separate shapes, each with its own outline, so the outline shows where they meet (such as the parts of a machine).
- **Pages** (compare, split) are Yaru's page: rounded corners (14 px), the top right corner folded (36 px, a solid triangle), a light surface with a 14 px glyph edge. Arrows that show content moving are Yaru blue, as in the formatting icons. With several shapes, the gradient is set on the whole canvas (`gradientUnits="userSpaceOnUse"`, from #4d4d4d at 0,0 to #151515 at 256,256) so it runs evenly across them.
- **Icons calibre has only as a light and dark pair** (`close`, `clear_left`) get a source for each: `<name>-for-light-theme.svg` and `<name>-for-dark-theme.svg`.

## Working in Illustrator

Simple icons (letters, lines, badges, basic shapes) are written as SVG code directly. Icons with detailed artwork are made together with the user in Adobe Illustrator 2025, which is installed and can be driven by scripts through its COM interface (`Illustrator.Application`):

1. Draw a first version as `src/<icon-name>.svg` from Yaru's sources and open it in Illustrator by script, so the user can refine it there. Only touch documents opened this way or that the user points to.
2. When the user is done, export the document by script as plain SVG 1.1: shapes as paths (text converted to outlines), styles as presentation attributes, no Illustrator editing data, no embedded images.
3. Clean the exported file: remove Illustrator's extra elements and metadata, keep the 256×256 `viewBox`, and check the drawing still follows this guide.
4. Render, check and preview as for any other icon (`tools\theme.cmd render`, `check`, `preview`).

What survives the round trip, learned on the books in a series, publisher, tags, identifiers and column icons:

- **Plain shapes only.** Illustrator drops SVG filters (it fills the shape solid black instead) and exports clipping paths as `<use>` references that calibre's SVG renderer can't draw. Draw Yaru's darker bottom edge and top highlight as real shapes (the shape intersected with a copy of itself moved up, or minus a copy moved down), not with clip paths.
- **Shadows as named groups.** Put each drop shadow in its own group `shadow-N` right under its shape. For Illustrator the group is plain black at 22% opacity; when cleaning the export, give these groups Yaru's blur back (`feGaussianBlur` 2.5, 2 px down, 22% black). Illustrator keeps group ids as their names, so the groups come back with the same ids.
- **Linear gradients, stop opacity, even-odd fills and fill opacity** survive as they are.
- **Turn off alerts.** Set `app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS` while a script opens files; otherwise an import warning dialog blocks the script until someone clicks OK.

Export with `ExportOptionsSVG`: `DTD` SVG1_1, `cssProperties` PRESENTATIONATTRIBUTES, `fontType` OUTLINEFONT, `preserveEditability`, `embedRasterImages`, `includeFileInfo` and `optimizeForSVGViewer` off, `coordinatePrecision` 2, UTF-8.
