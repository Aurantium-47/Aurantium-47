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
    body += '<g class="spin">'
    body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0b1110" stroke="#59665a"/>'
    for inset in (10, 17, 24, 31):
        body += f'<circle cx="{cx}" cy="{cy}" r="{r-inset}" fill="none" stroke="#303e34" stroke-width=".7"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="{r*.40}" fill="#bfce9f"/>'
    body += text(cx, cy - 4, "OASIS", 14, "#233021", extra='text-anchor="middle" font-weight="bold"')
    body += text(cx, cy + 12, "SIDE A · 1996", 7, "#233021", SANS, 'text-anchor="middle"')
    body += f'<circle cx="{cx}" cy="{cy}" r="3" fill="#141d1b"/></g>'
    if mobile:
        body += text(200, 120, "Don't Look", 25)
        body += text(200, 150, "Back in Anger", 25)
        body += text(202, 180, DATA["record"]["artist"], 17, "#bdcba7")
        body += text(28, 219, "On repeat", 13, "#aab9a6", SANS)
        body += text(137, 219, DATA["on_repeat"]["title"], 16)
        body += '<path d="M25 242H415V296A9 9 0 0 0 415 314V372H25V314A9 9 0 0 0 25 296Z" fill="#e9e4d6"/>'
        body += text(42, 312, DATA["musicals"][0], 46, "#293329")
        body += '<path d="M42 333H398" stroke="#aaa992" stroke-dasharray="3 4"/>'
    else:
        body += text(247, 132, "Don't Look Back", 33)
        body += text(248, 171, "in Anger", 33)
        body += text(250, 206, DATA["record"]["artist"], 18, "#bdcba7")
        body += '<path d="M625 66H890V147A10 10 0 0 0 890 167V233H625V167A10 10 0 0 0 625 147Z" fill="#e9e4d6"/>'
        body += text(647, 154, DATA["musicals"][0], 43, "#293329")
        body += '<path d="M647 194H869" stroke="#aaa992" stroke-dasharray="3 4"/>'
        body += '<path d="M28 251H892" stroke="#37433a"/>'
        body += text(30, 279, "On repeat", 13, "#aab9a6", SANS)
        body += text(149, 280, DATA["on_repeat"]["title"], 18)
    css = f'.spin{{transform-origin:{cx}px {cy}px;animation:turn 28s linear infinite}}@keyframes turn{{to{{transform:rotate(360deg)}}}}'
    description = f'{DATA["record"]["artist"]} — {DATA["record"]["title"]}；最近单曲循环：借过；音乐剧：' + '、'.join(DATA["musicals"])
    return document(w, h, "唱片与票根", description, body, css)


if __name__ == "__main__":
    for mobile in (False, True):
        suffix = '-mobile' if mobile else ''
        svg = record(mobile)
        (HERE/f'records{suffix}.svg').write_text(svg, encoding='utf-8')
        zh = svg.replace('On repeat', '最近在听').replace('Jie Guo', '借过').replace('Hamilton','汉密尔顿').replace('>Oasis<','>绿洲乐队<').replace('SIDE A · 1996','A面 · 1996')
        (HERE/f'records{suffix}-zh.svg').write_text(zh, encoding='utf-8')
