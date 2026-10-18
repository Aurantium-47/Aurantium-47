# Interest components

Install Pillow (`python -m pip install Pillow`). The layout measures Georgia from Windows; on another system set `INTERESTS_FONT` to a compatible serif font file. Edit `interests.json`, then run `python assets/interests/build.py` from the repository root.

- `record`, `on_repeat`, and `musicals` supply the listening and theatre card.
- `words` is the interest inventory; `flow_rows.desktop` and `flow_rows.mobile` control the visible labels and font sizes. Rows travel continuously along wide loops with different phases. Text opacity cycles every six seconds between 0.65 and 1, so words never vanish. Add or remove a label in the inventory and both flow layouts.
- `attitude` supplies the small scrolling line.
- Four self-contained SVGs are generated. They use no scripts, trackers, external fonts, or music-account connections. Motion stops with the browser's reduced-motion preference.

The index records interests mentioned in conversation. Type size is a layout choice, not a proficiency score. AI-assisted maintenance happens when this data is updated; there is no background account synchronization.

The record and ticket illustrations are original vector artwork, not album covers or performance tickets.
