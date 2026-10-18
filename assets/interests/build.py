"""Rebuild the README images after editing interests.json. Python standard library only."""
import json
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "interests.json").read_text(encoding="utf-8"))
SERIF = "Georgia,'Noto Serif SC','Songti SC','SimSun',serif"
SANS = "'Segoe UI','Microsoft YaHei','Noto Sans CJK SC',sans-serif"


def text(x, y, value, size=16, color="#efece4", font=SERIF, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" {extra}>{escape(value)}</text>'


def document(width, height, title, description, body, css):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<style>{css}@media(prefers-reduced-motion:reduce){{.spin,.drift,.ticker{{animation:none!important}}}}</style>
{body}
</svg>\n'''


def record(mobile=False):
    w, h = (440, 397) if mobile else (920, 300)
    cx, cy, r = (102, 127, 73) if mobile else (131, 149, 87)
    body = f'<rect width="{w}" height="{h}" rx="4" fill="#141d1b"/>'
    body += text(28, 30, "唱片与票根", 12, "#afbaae", SANS)
    body += text(w - 65, 30, "47 kΩ", 11, "#afbaae", SANS)
    body += f'<path d="M28 45H{w-28}" stroke="#37433a"/>'
    body += '<g class="spin">'
    body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0b1110" stroke="#59665a"/>'
    for inset in (10, 17, 24, 31):
        body += f'<circle cx="{cx}" cy="{cy}" r="{r-inset}" fill="none" stroke="#303e34" stroke-width=".7"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="{r*.40}" fill="#bfce9f"/>'
    body += text(cx, cy - 4, "OASIS", 14, "#233021", extra='text-anchor="middle" font-weight="bold"')
    body += text(cx, cy + 12, "SIDE A · 1996", 7, "#233021", SANS, 'text-anchor="middle"')
    body += f'<circle cx="{cx}" cy="{cy}" r="3" fill="#141d1b"/></g>'
    if mobile:
        body += text(201, 88, "常常回来听", 11, "#aab9a6", SANS)
        body += text(200, 120, "Don't Look", 25)
        body += text(200, 150, "Back in Anger", 25)
        body += text(202, 180, DATA["record"]["artist"], 17, "#bdcba7")
        body += text(28, 219, "最近单曲循环", 11, "#aab9a6", SANS)
        body += text(137, 219, f'{DATA["on_repeat"]["title"]} / {DATA["on_repeat"]["artist"]}', 16)
        body += '<path d="M25 242H415V296A9 9 0 0 0 415 314V372H25V314A9 9 0 0 0 25 296Z" fill="#e9e4d6"/>'
        body += text(42, 278, DATA["musicals"][0], 26, "#293329")
        body += text(239, 278, DATA["musicals"][1], 25, "#293329")
        body += text(42, 315, DATA["musicals"][2], 24, "#293329")
        body += '<path d="M42 333H398" stroke="#aaa992" stroke-dasharray="3 4"/>'
        body += text(42, 356, "MUSICAL THEATRE", 10, "#64715d", SANS, 'letter-spacing="2"')
    else:
        body += text(249, 89, "常常回来听", 12, "#aab9a6", SANS)
        body += text(247, 132, "Don't Look Back", 33)
        body += text(248, 171, "in Anger", 33)
        body += text(250, 206, DATA["record"]["artist"], 18, "#bdcba7")
        body += '<path d="M625 66H890V147A10 10 0 0 0 890 167V233H625V167A10 10 0 0 0 625 147Z" fill="#e9e4d6"/>'
        body += text(647, 106, DATA["musicals"][0], 31, "#293329")
        body += text(648, 144, DATA["musicals"][1], 26, "#293329")
        body += text(648, 177, DATA["musicals"][2], 19, "#293329")
        body += '<path d="M647 194H869" stroke="#aaa992" stroke-dasharray="3 4"/>'
        body += text(648, 217, "MUSICAL THEATRE", 10, "#64715d", SANS, 'letter-spacing="2"')
        body += '<path d="M28 251H892" stroke="#37433a"/>'
        body += text(30, 279, "最近单曲循环", 12, "#aab9a6", SANS)
        body += text(149, 280, f'{DATA["on_repeat"]["title"]} / {DATA["on_repeat"]["artist"]}', 18)
        body += text(705, 279, "BRITPOP / THEATRE", 11, "#aab9a6", SANS, 'letter-spacing="1.5"')
    css = f'.spin{{transform-origin:{cx}px {cy}px;animation:turn 28s linear infinite}}@keyframes turn{{to{{transform:rotate(360deg)}}}}'
    description = f'{DATA["record"]["artist"]} — {DATA["record"]["title"]}；最近单曲循环：借过 — 印子月；音乐剧：' + '、'.join(DATA["musicals"])
    return document(w, h, "唱片与票根", description, body, css)


def cloud(mobile=False):
    w, h = (440, 603) if mobile else (920, 442)
    key = "mobile" if mobile else "desktop"
    body = f'<rect width="{w}" height="{h}" rx="4" fill="#f2f1eb"/>'
    body += text(28, 33, "最近提到", 13, "#69776a", SANS)
    body += text(w - 28, 33, DATA["note"], 11, "#748170", SANS, 'text-anchor="end"')
    body += f'<path d="M28 49H{w-28}" stroke="#cdd2c6"/>'
    for i, word in enumerate(DATA["words"]):
        x, y, size = word[key]
        color = "#70806b" if word.get("tone") == "quiet" else "#2c3c30"
        extra = 'font-style="italic"' if word.get("italic") else ""
        body += f'<g class="drift" style="animation-duration:{14+i%7*2}s;animation-delay:-{i*1.7}s">'
        body += text(x, y, word["text"], size, color, extra=extra) + '</g>'
    y = h - 27
    lead = DATA["attitude"]["lead"]
    tail = DATA["attitude"]["tail"]
    start = 169 if mobile else 190
    body += f'<path d="M28 {y-25}H{w-28}" stroke="#cdd2c6"/>'
    body += text(28, y, lead, 13, "#506245", SANS)
    body += f'<defs><clipPath id="strip"><rect x="{start}" y="{y-18}" width="{w-start-28}" height="25"/></clipPath></defs>'
    body += '<g clip-path="url(#strip)"><g class="ticker">'
    for offset in (0, 1080):
        body += text(start + offset, y, tail, 12, "#7d8976", SANS, 'textLength="1040" lengthAdjust="spacing"')
    body += '</g></g>'
    css = '''.drift{animation:float 18s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.drift:nth-of-type(3n){animation-name:float2}.drift:nth-of-type(3n+1){animation-name:float3}
@keyframes float{0%,100%{transform:translate(-7px,3px)}50%{transform:translate(8px,-5px)}}
@keyframes float2{0%,100%{transform:translate(5px,-5px)}50%{transform:translate(-6px,6px)}}
@keyframes float3{0%,100%{transform:translate(-4px,-6px)}50%{transform:translate(5px,7px)}}
.ticker{animation:flow 66s linear infinite}@keyframes flow{to{transform:translateX(-1080px)}}'''
    description = DATA["note"] + '：' + '、'.join(x["text"] for x in DATA["words"]) + '。' + lead + tail
    return document(w, h, "最近提到", description, body, css)


if __name__ == "__main__":
    for name, builder in (("records", record), ("words", cloud)):
        for mobile in (False, True):
            filename = f'{name}{"-mobile" if mobile else ""}.svg'
            (HERE / filename).write_text(builder(mobile), encoding="utf-8")
            print(filename)
