# Interest components

Edit `interests.json`, then run `python assets/interests/build.py` from the repository root.

- `record`, `on_repeat`, and `musicals` supply the listening and theatre card.
- `words` supplies the animated index. Each entry has desktop and mobile `[x, baseline, font-size]` coordinates. Add or remove an entry to change the index; adjust its two positions when needed.
- `attitude` supplies the small scrolling line.
- Four self-contained SVGs are generated. They use no scripts, trackers, external fonts, or music-account connections. Motion stops with the browser's reduced-motion preference.

The index records interests mentioned in conversation. Type size is a layout choice, not a proficiency score. AI-assisted maintenance happens when this data is updated; there is no background account synchronization.

The record and ticket illustrations are original vector artwork, not album covers or performance tickets.
