# Yaru style guide for this theme

How the icons drawn for this project match Ubuntu's Yaru icons. The numbers were measured from Yaru's own sources and from the 256 px Yaru icons already in the theme. The SVG files in `src/` follow every rule here, so they are the working examples.

## Where Yaru's sources are

All in [github.com/ubuntu/yaru](https://github.com/ubuntu/yaru), licensed CC BY-SA 4.0:

| What | Path | Use it for |
|---|---|---|
| Full-color sources | `icons/src/fullcolor/default/<context>/<name>.svg` | The look: shapes, gradients, outlines. Each file holds the 16, 24, 32, 48 and 256 px versions side by side; the 256 px one is the 256×256 square at x 24, y 28. |
| Full-color PNGs | `icons/Yaru/256x256/<context>/<name>.png` | Icons Yaru already has: use them as they are. |
| Symbolic icons | `icons/src/scalable/default/<context>/<name>-symbolic.svg` | The idea, when Yaru has no full-color icon for it (16 px, one color). |
| Old full-color actions | `icons/src/fullcolor/default/legacy/` | Badges and bullets: `list-add`, `list-remove`. |
| Templates and Yaru's rules | `icons/src/fullcolor/README.md`, `icons/CONTRIBUTING.md` | |

Yaru's own rules that matter here: new full-color icons are made from a template or from an existing Yaru icon; names follow the freedesktop icon naming spec; Yaru draws in Inkscape and warns that other editors add their own elements to SVG files, so anything made elsewhere must be saved as plain SVG (see [Working in Illustrator](#working-in-illustrator)).

## Canvas

- One 256×256 image per icon. calibre takes a single image and scales it, so unlike Yaru there are no separate small-size drawings. Draw in `src/<icon-name>.svg` with `viewBox="0 0 256 256"`; `tools\theme.cmd render` makes the PNG.
- Keep the drawing inside 32..224 px. Tall shapes may use 20..234 px, the height Yaru's letters use (Yaru's "B" runs from 21 to 234 with its outline).

## The neutral look (the default)

Most icons are neutral, like Yaru's 256 px text formatting icons.

- **Glyphs and solid shapes**: a linear gradient from #4d4d4d at the top left to #151515 at the bottom right (`x1="1" y1="1" x2="0" y2="0"`: stop 0 #151515, stop 1 #4d4d4d), with a 4 px white outline: draw a white copy of the shape with an 8 px white stroke, round joins, under the shape. The outline is what keeps them readable on dark backgrounds.
- **Text lines** (Yaru's `format-justify-*`): #232629 bars, 8 px high, with a white copy of each bar 8 px below it. In a paragraph they repeat every 24 px; full lines are 192 px long from x 32, shorter ones 160 or 128 px.
- **Light surfaces** (inside of a bucket, an eraser's rubber): a gradient from #f7f7f7 at the top left to #d5d5d5 at the bottom right. Next to white, give them a thin #232629 edge.
- **Letters and digits**: the Ubuntu font, as in Yaru. Ubuntu Bold for letters and digits (heading "H", subscript "x", list numbers). The "A" in text color, background color and font size icons is the Ubuntu Medium "A" from Yaru's `font-color-symbolic.svg`. Letters that stand alone are as tall as Yaru's B, I, U: about 206 px.

## Color

Color is the exception: use it only where it means something, and keep everything else neutral.

| Color | Values | Means | Used in |
|---|---|---|---|
| Yaru blue | gradient #1a7fd4 → #37a6e6 (Yaru's `list-remove` bullets) | the thing the button inserts or moves | list bullets, the "2" in subscript and superscript, the horizontal rule |
| Yaru green | #45a925 (Yaru's `list-add`) | add, more | plus badges |
| Yaru red | #c7162b (Yaru's `list-remove`); as a gradient #a51d2d → #e2364c | remove, less; the text color | minus badges, the text color swatch |

Buttons that are about color in general (background color) or used everywhere (clear) stay neutral.

## Layout of the formatting icons

- Lists: three rows centered at y 52, 124 and 196. The marker column is 32..80 (digits centered in it, bullets are 32 px circles centered at x 56); the text lines run from x 96 to 224. Yaru's `list-remove` puts its bullets at the same rows.
- Badges (plus, minus, color swatch) sit at the bottom right, over the main shape, with the same 4 px white outline so they stand apart from it.

## Ideas and logic

- Keep the idea of calibre's original icon unless Yaru has its own symbol for that action; then follow Yaru (ordered list, font color, clear). If neither fits, use the most common design for that action (a paint bucket for fill color).
- Drawings must make physical sense: a pouring bucket has a level liquid surface that reaches the spout the drop comes from; an eraser touches the line it erases.
- Check every icon on light and dark backgrounds and at 16, 24, 32 and 48 px before calling it done.

## Working in Illustrator

Simple icons (letters, lines, badges, basic shapes) are written as SVG code directly. Icons with detailed artwork are made together with the user in Adobe Illustrator 2025, which is installed and can be driven by scripts through its COM interface (`Illustrator.Application`):

1. Draw a first version as `src/<icon-name>.svg` from Yaru's sources and open it in Illustrator by script, so the user can refine it there. Only touch documents opened this way or that the user points to.
2. When the user is done, export the document by script as plain SVG 1.1: shapes as paths (text converted to outlines), styles as presentation attributes, no Illustrator editing data, no embedded images.
3. Clean the exported file: remove Illustrator's extra elements and metadata, keep the 256×256 `viewBox`, and check the drawing still follows this guide.
4. Render, check and preview as for any other icon (`tools\theme.cmd render`, `check`, `preview`).

Scripts wait while Illustrator has a dialog open. This workflow has not been used for an icon yet, so try it on a copy first.
