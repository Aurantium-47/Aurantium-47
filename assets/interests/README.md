# Interest components

The sphere motion is baked from cong-min/TagCloud (MIT). The upstream library and license are preserved in vendor/. No JavaScript runs inside the published SVG.

Edit interests.json. Each word has an English label, a Chinese label and a size. sphere controls the loop length, minimum opacity and spread for each display size.

Rebuild with:

    python assets/interests/build.py
    node assets/interests/build-sphere.cjs

The Python script generates the record/ticket artwork. The Node script executes TagCloud against a minimal DOM adapter and samples one exact full rotation; it exports desktop/mobile SVGs in both languages. No package installation is needed. Reduced-motion preferences stop the animation.

The title song and Komm, süsser Tod retain their original names; natural Chinese names are used in the Chinese images. The index records conversation interests, not proficiency. Maintenance is AI-assisted, without automatic account synchronization.

Upstream: https://github.com/cong-min/TagCloud
