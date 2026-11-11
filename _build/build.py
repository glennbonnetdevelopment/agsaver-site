#!/usr/bin/env python3
"""Builds the agsaver.ca pages. Run from the repo root: python3 _build/build.py

Every page shares the header, footer and CTA defined here, so edit content in this
file and re-run rather than editing the generated .html files by hand.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_STORE = "https://apps.apple.com/ca/app/agsaver/id6827369143"
SITE = "https://agsaver.ca"
EMAIL = "info@glennbonnet.com"

# ---------- Icons (24px line icons) ----------
def ico(paths):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')

I = {
    "clock": ico('<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9.5 2.5h5M12 2.5V5"/>'),
    "route": ico('<circle cx="6" cy="19" r="2.2"/><circle cx="18" cy="5" r="2.2"/><path d="M8.2 19H15a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h6.8"/>'),
    "field": ico('<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5l9 4.5 9-4.5M12 12v9"/>'),
    "sprout": ico('<path d="M12 21v-9"/><path d="M12 12C12 7 8.5 4.5 4 4.5c0 4.5 3 7.5 8 7.5z"/><path d="M12 14c0-4 3-6.5 8-6.5 0 4-3 6.5-8 6.5z"/>'),
    "tractor": ico('<circle cx="7" cy="16" r="4"/><circle cx="18" cy="17.5" r="2.5"/><path d="M5 12V6h6l1.5 6M11 12h7.5a1.5 1.5 0 0 1 1.5 1.5V15M15.5 12V8M3 12h9"/>'),
    "chart": ico('<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'),
    "users": ico('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.6 3.2-5.5 6.5-5.5s5.9 1.9 6.5 5.5"/><circle cx="17" cy="9" r="2.6"/><path d="M17 14.3c2.5.2 4 1.8 4.5 4.7"/>'),
    "shield": ico('<path d="M12 3 4.5 6v5.5c0 4.6 3.1 8.2 7.5 9.5 4.4-1.3 7.5-4.9 7.5-9.5V6z"/><path d="m9 12 2 2 4-4"/>'),
    "watch": ico('<rect x="6" y="6" width="12" height="12" rx="3.5"/><path d="M9 6l.6-3h4.8l.6 3M9 18l.6 3h4.8l.6-3M12 9.5V12l1.5 1.5"/>'),
    "pause": ico('<circle cx="12" cy="12" r="9"/><path d="M10 9v6M14 9v6"/>'),
    "weather": ico('<path d="M7 18h10a4 4 0 0 0 .5-8 6 6 0 0 0-11.4 1.5A3.3 3.3 0 0 0 7 18z"/><path d="M8 21h0M12 21h0M16 21h0"/>'),
    "wind": ico('<path d="M3 8h11a3 3 0 1 0-3-3M3 12h16a3 3 0 1 1-3 3M3 16h7"/>'),
    "lines": ico('<path d="M5 21 9 3M12 21l1-18M19 21 17 3"/><circle cx="11" cy="13" r="1.6" fill="currentColor"/>'),
    "laps": ico('<rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M11 11h2v2h-2z"/>'),
    "map": ico('<path d="M9 4 3 6.5v13.5l6-2.5 6 2.5 6-2.5V4l-6 2.5z"/><path d="M9 4v13.5M15 6.5V20"/>'),
    "pin": ico('<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'),
    "import": ico('<path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 17v2.5A1.5 1.5 0 0 0 5.5 21h13a1.5 1.5 0 0 0 1.5-1.5V17"/>'),
    "export": ico('<path d="M12 15V3M7 8l5-5 5 5"/><path d="M4 17v2.5A1.5 1.5 0 0 0 5.5 21h13a1.5 1.5 0 0 0 1.5-1.5V17"/>'),
    "folder": ico('<path d="M3 6.5A1.5 1.5 0 0 1 4.5 5H9l2 2.5h8.5A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/>'),
    "drop": ico('<path d="M12 3s-6 6.6-6 11a6 6 0 0 0 12 0c0-4.4-6-11-6-11z"/>'),
    "dollar": ico('<circle cx="12" cy="12" r="9"/><path d="M15 9.2c-.5-1-1.6-1.6-3-1.6-1.8 0-3 .9-3 2.2 0 3 6 1.6 6 4.5 0 1.3-1.3 2.2-3 2.2-1.5 0-2.7-.7-3.1-1.8M12 6v1.6M12 16.5V18"/>'),
    "history": ico('<path d="M3.5 12a8.5 8.5 0 1 0 2.5-6L3.5 8.5"/><path d="M3.5 4v4.5H8M12 8v4l3 2"/>'),
    "wrench": ico('<path d="M14.5 6.5a4 4 0 0 0 5 5L21 13l-8 8-3.5-3.5 8-8M14.5 6.5 13 5l-8 8 1.5 1.5"/><path d="M14.7 6.3a4 4 0 0 1 5-3.3l-2.4 2.4.5 2.3 2.3.5L22.5 6a4 4 0 0 1-3.3 5"/>'),
    "bell": ico('<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>'),
    "gear": ico('<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/>'),
    "fuel": ico('<path d="M4 21V5a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v16M3 21h13M4 10h11"/><path d="M15 8h2a2 2 0 0 1 2 2v6.5a1.5 1.5 0 0 0 3 0V8l-3-3"/>'),
    "receipt": ico('<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6M9 16h3"/>'),
    "link": ico('<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>'),
    "sync": ico('<path d="M20 11a8 8 0 0 0-14.3-4.3L4 9M4 4v5h5M4 13a8 8 0 0 0 14.3 4.3L20 15M20 20v-5h-5"/>'),
    "doc": ico('<path d="M14 3H6.5A1.5 1.5 0 0 0 5 4.5v15A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5V8z"/><path d="M14 3v5h5M8.5 13h7M8.5 17h5"/>'),
    "cloud": ico('<path d="M7 19h10a4.5 4.5 0 0 0 .6-9A6 6 0 0 0 6 11.5 3.8 3.8 0 0 0 7 19z"/>'),
    "phone": ico('<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>'),
    "gauge": ico('<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/><path d="M4 17h2M18 17h2M12 9V7"/>'),
    "parts": ico('<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5l2 2.6 3.2-.5.7 3.2 2.9 1.5-1.3 3 1.3 3-2.9 1.5-.7 3.2-3.2-.5-2 2.6-2-2.6-3.2.5-.7-3.2-2.9-1.5 1.3-3-1.3-3 2.9-1.5.7-3.2 3.2.5z"/>'),
    "menu": ico('<path d="M4 7h16M4 12h16M4 17h16"/>'),
    "mail": ico('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/>'),
}

APPLE = ('<svg viewBox="0 0 384 512" aria-hidden="true"><path fill="currentColor" d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>')

def appstore(small=False):
    cls = "appstore sm" if small else "appstore"
    return (f'<a class="{cls}" href="{APP_STORE}" target="_blank" rel="noopener">{APPLE}'
            '<span><small>Download on the</small><strong>App Store</strong></span></a>')

ZOOM = {"zoom-hourmeter": 366, "zoom-guidance": 510, "zoom-machine": 360, "zoom-crop": 222, "zoom-sprays": 759}

def phone(src, alt, extra=""):
    if src in ZOOM:  # a close-up of part of a screen, shown as a card
        return (f'<div class="zoom"><img src="img/shots/{src}.webp" alt="{html.escape(alt)}" '
                f'width="720" height="{ZOOM[src]}" loading="lazy" decoding="async"></div>')
    w, h = (416, 496) if "watch" in src else (640, 1387)
    cls = "phone watch" if "watch" in src else "phone"
    return (f'<div class="{cls}{extra}"><img src="img/shots/{src}.webp" alt="{html.escape(alt)}" '
            f'width="{w}" height="{h}" loading="lazy" decoding="async"></div>')

# ---------- Feature sets ----------
SETS = [
    dict(slug="work", icon="clock", nav="Hour meter & work sessions", short="Hours & work",
         title="Hour meter & work sessions",
         blurb="Every machine gets a live hour meter. Start work with one tap on iPhone or Apple Watch and the hours add themselves.",
         bullets=["One-tap start, pause and stop", "Auto pause when the machine sits idle", "Apple Watch work timer"],
         shot="dashboard"),
    dict(slug="maps", icon="route", nav="Work maps & guidance", short="Maps & guidance",
         title="Work maps & guidance",
         blurb="See every pass on a satellite map, track how many acres are left in the field, and follow A–B lines at your implement's width.",
         bullets=["Path drawn at working width", "Acres remaining, lap by lap", "A–B guidance lines"],
         shot="liveguidance"),
    dict(slug="fields", icon="field", nav="Fields & boundaries", short="Fields",
         title="Fields & boundaries",
         blurb="Outline your fields by tapping corners or driving the edge, or bring them in from Operations Center, FieldView or Google Earth.",
         bullets=["Import shapefile, KML, KMZ or GeoJSON", "Group fields by farm", "Acres worked matched automatically"],
         shot="myfields"),
    dict(slug="crops", icon="sprout", nav="Crops, sprays & profit", short="Crops & sprays",
         title="Crops, sprays & profit",
         blurb="Record crops, sprays and inputs field by field, check the spray window, and see yield, revenue and profit per acre.",
         bullets=["Spray records with weather filled in", "Hour-by-hour spray window", "Yield and profit per field"],
         shot="yieldprofit"),
    dict(slug="machines", icon="tractor", nav="Machines, service & fuel", short="Machines & service",
         title="Machines, service & fuel",
         blurb="Keep tractors, combines, sprayers and implements in one place, with service intervals, reminders, parts, fuel and costs.",
         bullets=["Service bars from green to red", "Reminders by hours or date", "Fuel use in L/hr and cost per acre"],
         shot="farm"),
    dict(slug="reports", icon="chart", nav="Reports, crew & your data", short="Reports & crew",
         title="Reports, crew & your data",
         blurb="Farm and field reports, a live crew map, one-file sync for everyone who runs your machines, and full exports of your data.",
         bullets=["Cost of ownership and fuel reports", "Live crew map and sync files", "Export everything to a zip"],
         shot="fieldsreport"),
]
BY = {s["slug"]: s for s in SETS}

# ---------- Shared chrome ----------
def head(title, desc, path):
    url = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#1b5e28">
<meta name="apple-itunes-app" content="app-id=6827369143">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AgSaver">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="img/emblem.svg" type="image/svg+xml">
<link rel="icon" href="img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v=1">
</head>
<body>
"""

def header(active=""):
    sub = "".join(f'<li><a href="{s["slug"]}.html"{" class=\"active\"" if s["slug"]==active else ""}>{I[s["icon"]]}{s["nav"]}</a></li>' for s in SETS)
    return f"""<header class="site-header" id="top">
  <div class="wrap">
    <a href="index.html" class="brand" aria-label="AgSaver home"><img src="img/emblem.svg" alt="" width="38" height="38"><span><span class="ag">Ag</span><span class="sv">Saver</span></span></a>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false">{I["menu"]}</button>
    <ul class="menu">
      <li class="has-sub"><a href="index.html#features"{" class=\"active\"" if active in BY else ""}>Features</a>
        <ul class="sub">{sub}</ul>
      </li>
      <li><a href="index.html#screens">Screenshots</a></li>
      <li><a href="support.html"{" class=\"active\"" if active=="support" else ""}>Support</a></li>
      <li>{appstore(True).replace('class="appstore sm"', 'class="appstore sm header-cta"')}</li>
    </ul>
  </div>
</header>
"""

def cta(title="Put every hour and every acre to work.", text="AgSaver runs on iPhone, iPad and Apple Watch. Your records stay on your devices and your own iCloud."):
    return f"""<section class="cta">
  <div class="wrap">
    <div>
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="btns">{appstore()}<a href="support.html" class="btn btn-ghost-light">Questions? Get support</a></div>
    </div>
    <div class="qr"><img src="img/qr.svg" alt="QR code to AgSaver on the App Store" width="150" height="150">Scan to download</div>
  </div>
</section>
"""

def footer():
    feats = "".join(f'<li><a href="{s["slug"]}.html">{s["nav"]}</a></li>' for s in SETS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a href="index.html" class="brand"><img src="img/emblem.svg" alt="" width="38" height="38"><span><span class="ag">Ag</span><span class="sv">Saver</span></span></a>
        <p>Farm machine records for hours, work, fields, sprays, service and costs. Made by Glenn Bonnet.</p>
        <p style="margin-top:18px">{appstore(True)}</p>
      </div>
      <div><h4>Features</h4><ul>{feats}</ul></div>
      <div><h4>Help</h4><ul>
        <li><a href="support.html">Support &amp; FAQ</a></li>
        <li><a href="privacy.html">Privacy policy</a></li>
        <li><a href="mailto:{EMAIL}">Email {EMAIL}</a></li>
        <li><a href="https://glennbonnet.com" rel="noopener">More apps by Glenn Bonnet</a></li>
      </ul></div>
    </div>
    <div class="legal"><span>© <span class="yr">2026</span> Glenn Bonnet. All rights reserved.</span><span>Apple, iPhone, iPad, Apple Watch and App Store are trademarks of Apple Inc.</span></div>
  </div>
</footer>
<script>
document.querySelectorAll('.yr').forEach(e => e.textContent = new Date().getFullYear());
const h = document.querySelector('.site-header'), t = h.querySelector('.menu-toggle');
t.addEventListener('click', () => {{ const o = h.classList.toggle('open'); t.setAttribute('aria-expanded', o); }});
h.querySelectorAll('.menu a').forEach(a => a.addEventListener('click', () => {{ h.classList.remove('open'); t.setAttribute('aria-expanded', false); }}));
</script>
</body>
</html>
"""

def others(current):
    items = "".join(
        f'<a class="other" href="{s["slug"]}.html"><span class="ic">{I[s["icon"]]}</span><div>{s["title"]}<span>{s["bullets"][0]}</span></div></a>'
        for s in SETS if s["slug"] != current)
    return f"""<section class="tight alt">
  <div class="wrap">
    <div class="eyebrow">Keep exploring</div>
    <h2 style="font-size:1.6rem;margin-bottom:22px">More of what AgSaver does</h2>
    <div class="others">{items}</div>
  </div>
</section>
"""

def row(eyebrow, title, paras, ticks, shots, flip=False, id_=None, note=None):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    tk = ('<ul class="ticks">' + "".join(f"<li>{t}</li>" for t in ticks) + "</ul>") if ticks else ""
    nt = f'<div class="note">{note}</div>' if note else ""
    media = "".join(phone(s, a) for s, a in shots)
    idattr = f' id="{id_}"' if id_ else ""
    return f"""<div class="row{' flip' if flip else ''}"{idattr}>
      <div>
        <div class="eyebrow">{eyebrow}</div>
        <h3>{title}</h3>
        {ps}{tk}{nt}
      </div>
      <div class="row-media">{media}</div>
    </div>
"""

def details(items):
    return '<div class="details">' + "".join(
        f'<div class="detail"><div class="ic">{I[i]}</div><h3>{t}</h3><p>{p}</p></div>' for i, t, p in items) + "</div>"

def feature_page(slug, desc, lead, hero_shot, jumps, rows, extra_title, extra_lead, extra_items):
    s = BY[slug]
    jl = "".join(f'<a href="#{j}">{n}</a>' for j, n in jumps)
    body = "".join(row(**r) for r in rows)
    return (head(f'{s["title"]} — AgSaver', desc, f"{slug}.html") + header(slug) + f"""<main>
<section class="page-hero" style="padding:0">
  <div class="wrap">
    <div class="copy">
      <div class="crumbs"><a href="index.html">AgSaver</a> &nbsp;/&nbsp; <a href="index.html#features">Features</a></div>
      <div class="eyebrow">{s["short"]}</div>
      <h1>{s["title"]}</h1>
      <p class="lead">{lead}</p>
      <div class="jump">{jl}</div>
    </div>
    <div class="media">{phone(hero_shot[0], hero_shot[1])}</div>
  </div>
</section>
<section>
  <div class="wrap">
    {body}
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">The details</div><h2>{extra_title}</h2><p class="lead">{extra_lead}</p></div>
    {details(extra_items)}
  </div>
</section>
""" + others(slug).replace('class="tight alt"', 'class="tight"') + cta() + "</main>\n" + footer())

PAGES = {}

# ---------- Home ----------
def home():
    sets = "".join(f"""<a class="set" href="{s['slug']}.html">
        <div class="set-img"><img src="img/shots/{s['shot']}.webp" alt="" width="640" height="1387" loading="lazy" decoding="async"></div>
        <div class="set-body"><div class="ic">{I[s['icon']]}</div><h3>{s['title']}</h3><p>{s['blurb']}</p>
          <ul>{''.join(f'<li>{b}</li>' for b in s['bullets'])}</ul><span class="more">Explore {s['short'].lower()} →</span></div>
      </a>""" for s in SETS)
    gallery = [
        ("dashboard", "Hour meter, service countdowns and work in progress"),
        ("liveguidance", "Live guidance with acres left in the field"),
        ("farmmap", "Every field and this year's work on one map"),
        ("fieldmap", "Field details on satellite imagery"),
        ("yieldprofit", "Yield, revenue and profit per acre"),
        ("fieldinputs", "Crop, sprays and inputs for each field"),
        ("sprayrecords", "Spray records for the whole farm"),
        ("farm", "Machines and implements with service bars"),
        ("myfields", "Fields sorted into groups"),
        ("fieldsreport", "Field reports on satellite imagery"),
    ]
    gal = "".join(f'<figure>{phone(s, c)}<figcaption>{c}</figcaption></figure>' for s, c in gallery)
    gal += f'<figure style="flex-basis:200px;align-self:center">{phone("watch", "A work session on Apple Watch")}<figcaption>Start and stop work from your wrist</figcaption></figure>'
    desc = ("AgSaver is the farm machine app for iPhone, iPad and Apple Watch: hour meters, work sessions, GPS work maps, "
            "A–B guidance, fields, spray records, yield and profit, service reminders, fuel and costs.")
    return head("AgSaver — Farm machine records for iPhone, iPad and Apple Watch", desc, "index.html") + header() + f"""<main>
<section class="hero" style="padding:0">
  <div class="wrap">
    <div class="hero-copy">
      <div class="kicker">{I['tractor'].replace('<svg', '<svg width="16" height="16"')} Farm machine records</div>
      <h1>Every hour.<br>Every pass.<br><em>Every field.</em></h1>
      <p class="sub">AgSaver keeps track of the hours, work, servicing and costs of your tractors, combines and implements, and maps your fields, sprays, crops and yields, so you always know what each machine and each field is doing and what it costs.</p>
      <div class="btns">{appstore()}<a href="#features" class="btn btn-ghost-light">See the features</a></div>
      <div class="platforms"><span>iPhone</span><span>iPad</span><span>Apple Watch</span></div>
    </div>
    <div class="hero-phones">
      {phone("liveguidance", "Live guidance while working a field")}
      {phone("dashboard", "AgSaver dashboard with the hour meter and a work session in progress")}
    </div>
  </div>
</section>

<div class="strip">
  <div class="wrap">
    <div>{I['phone']}<p>iPhone, iPad &amp; Watch<span>Start work from your wrist</span></p></div>
    <div>{I['cloud']}<p>Private iCloud sync<span>No account to create</span></p></div>
    <div>{I['map']}<p>GPS work maps<span>Acres worked, pass by pass</span></p></div>
    <div>{I['users']}<p>Built for crews<span>Share hours and work in one file</span></p></div>
  </div>
</div>

<section id="features">
  <div class="wrap">
    <div class="section-head center">
      <div class="eyebrow">Features</div>
      <h2>One app for the machines and the fields</h2>
      <p class="lead">AgSaver started as an hour meter and service log. It now covers the whole season, from the first pass to the yield and profit on each field.</p>
    </div>
    <div class="sets">{sets}</div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    {row("Hour meter", "Know exactly how many hours are on every machine",
         ["The dashboard shows a live hour meter for the machine you're on, read to the tenth of an hour, with a bar for every service that's coming due. When something is overdue, it turns red and says so."],
         ["<strong>Start, pause and stop</strong> work with one tap, on your phone or your Watch",
          "<strong>Hours add themselves</strong> to the machine and the implement on it",
          "<strong>Auto pause</strong> stops the clock while the machine sits idle"],
         [("dashboard", "Dashboard with hour meter"), ("watch", "Work timer on Apple Watch")])}
    {row("In the field", "See where you've been and what's left to do",
         ["AgSaver records the path you drive and draws it at the working width of your implement. Once you've driven a lap, it tells you how many acres are still left inside, and A–B lines show which pass you're on."],
         ["<strong>Acres worked</strong> are matched to your fields automatically",
          "<strong>Satellite farm map</strong> with this year's and last year's work",
          "<strong>Live crew map</strong> shows where everyone is working"],
         [("liveguidance", "Live guidance"), ("farmmap", "Farm map")], flip=True)}
    {row("At the end of the year", "Turn records into yield, cost and profit",
         ["Log each field's crop, sprays, fertilizer and seed as you go. At harvest, add the bushels and AgSaver works out revenue, input costs, fuel, other costs and profit, per field and per acre."],
         ["<strong>Spray records</strong> with wind and temperature filled in from Apple Weather",
          "<strong>Crop history</strong> for every field, year after year",
          "<strong>PDF reports</strong> to share with your agronomist or landlord"],
         [("yieldprofit", "Yield and profit"), ("sprayrecords", "Spray records")])}
  </div>
</section>

<section id="screens">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Screenshots</div><h2>Take a look</h2><p class="lead">Swipe through the app. Big numbers and big buttons, made to use in the cab.</p></div>
    <div class="gallery">{gal}</div>
  </div>
</section>

<section class="tight alt">
  <div class="wrap">
    <div class="privacy">
      <div class="shield">{I['shield']}</div>
      <div><h3>Your farm data stays yours</h3><p>Records are stored on your devices and sync through your own private iCloud. They are never sent to me. Location is used only while a work session is running, and crew sharing is off unless you turn it on.</p></div>
      <a href="privacy.html" class="btn btn-ghost">Privacy policy</a>
    </div>
  </div>
</section>
""" + cta() + "</main>\n" + footer()

PAGES["index.html"] = home

# ---------- Feature pages ----------
PAGES["work.html"] = lambda: feature_page(
    "work",
    "AgSaver's live hour meter and one-tap work sessions on iPhone and Apple Watch: timed jobs, GPS paths, auto pause, implement hours and weather saved with every session.",
    "Every machine gets a live hour meter. Start a work session with one tap, and AgSaver times the job, records where you drove and adds the hours to the machine and the implement on it.",
    ("dashboard", "AgSaver dashboard"),
    [("hour-meter", "Hour meter"), ("sessions", "Work sessions"), ("auto-pause", "Auto pause"), ("watch", "Apple Watch")],
    [
        dict(id_="hour-meter", eyebrow="Hour meter", title="A live hour meter for every machine",
             paras=["The dashboard shows the hour meter for the machine you're running, read to the tenth of an hour, just like the one in the cab. Under it, a bar for the machine and one for the implement on it count down the hours to the next service."],
             ticks=["Bars shift from green through yellow to red as service comes due",
                    "A red <strong>Service Required</strong> tag shows on the dashboard and the Farm screen when anything is overdue",
                    "Fix a reading any time to match the machine's own meter",
                    "Switch machines from the dashboard in one tap"],
             shots=[("zoom-hourmeter", "Hour meter and service countdowns")]),
        dict(id_="sessions", eyebrow="Work sessions", title="Start work with one tap", flip=True,
             paras=["Pick the machine, check which implement is on it and tap <strong>Start Work</strong>. AgSaver runs the clock and records your GPS path and distance. Tap <strong>Stop</strong> and the hours go on the machine's hour meter and the implement's own hours."],
             ticks=["<strong>Pause</strong> for lunch or a fill-up, and paused time isn't counted",
                    "Throw away a session started by mistake without touching the hour meter",
                    "See the time, distance and hours added while you work",
                    "Every finished session keeps its path, hours, fields and acres"],
             shots=[("startwork", "Start a work session"), ("work-sessions", "Work session history")]),
        dict(id_="auto-pause", eyebrow="Auto pause", title="Idle time doesn't count as work",
             paras=["Turn on auto pause in Settings and choose how many minutes the machine can stand still. When it stops moving for that long, AgSaver pauses the work clock from the moment it last moved, so the idle minutes never reach the hour meter. Drive off and it starts again by itself."],
             ticks=["Choose the idle time, or turn auto pause off",
                    "GPS keeps watching so work resumes on its own"],
             shots=[("liveguidance", "Work in progress with pause and stop")]),
        dict(id_="watch", eyebrow="Apple Watch", title="Run the clock from your wrist", flip=True,
             paras=["The AgSaver Watch app shows each machine and its hours. Start or stop a work session without taking your phone out, and add a fuel fill-up from the Watch while you're at the tank."],
             ticks=["Start and stop work on any machine",
                    "Live work timer on the Watch face",
                    "Add fuel from your wrist"],
             shots=[("watch", "AgSaver on Apple Watch")]),
    ],
    "Built around how a working day really goes", "The small things that keep the hours honest.",
    [("pin", "Sessions matched to fields", "When a session ends, AgSaver works out which of your fields it was in and how many acres you covered in each."),
     ("weather", "Weather saved with the work", "Each finished session looks up the weather from Apple Weather for where and when the work was done, halfway through the job."),
     ("tractor", "Implement hours", "Implements keep their own hours, so a seeder moved between tractors still knows how long it has run."),
     ("history", "Full session history", "Filter sessions by machine, implement or date, and open any one to see its path on the map."),
     ("gear", "Litres or US gallons", "Choose your fuel units and currency once in Settings, and every screen and report follows."),
     ("bell", "Service alerts", "Turn on maintenance alerts and AgSaver lets you know when a machine passes its service interval.")],
)

PAGES["maps.html"] = lambda: feature_page(
    "maps",
    "AgSaver records every pass on a satellite map at your implement's working width, shows acres remaining lap by lap, and gives you A–B guidance lines on iPhone and iPad.",
    "AgSaver draws where you've been at the width of your implement, keeps count of the acres left inside the field as you go, and shows A–B lines with the pass you're on.",
    ("farmmap", "Farm map with fields and work"),
    [("work-map", "Live work map"), ("laps", "Acres remaining"), ("ab-lines", "A–B lines"), ("farm-map", "Farm map")],
    [
        dict(id_="work-map", eyebrow="Live work map", title="Watch the field fill in as you work",
             paras=["Open the map during a work session and your path is drawn on satellite imagery at the working width of the implement you're pulling, so you can see what's covered and what you missed."],
             ticks=["Satellite or standard map",
                    "Path drawn at the implement's working width",
                    "Your fields outlined underneath, with acres worked in each",
                    "Time, distance and recording status at a glance"],
             shots=[("work-sessions", "Work sessions on the map")]),
        dict(id_="laps", eyebrow="Acres remaining", title="Know how much is left in the field", flip=True,
             paras=["Working around a field? When you come back to where a lap started, AgSaver closes the lap and tells you the acres inside it and how many are still unworked. Every pass after that, back and forth or around, is counted off as you drive."],
             ticks=["Updated after every lap, working in or out",
                    "Ground already worked isn't counted twice",
                    "Headland turns are left out of the count",
                    "Field progress shown as acres worked of the field total"],
             shots=[("zoom-guidance", "Lap closed with acres remaining and pass number")]),
        dict(id_="ab-lines", eyebrow="A–B guidance", title="Straight passes with A–B lines",
             paras=["Mark point A at one end of the field and point B at the other. AgSaver repeats the line every working width across the field and shows which pass you're on, numbered left and right of the A–B line, and how far you are from the centre of it."],
             ticks=["Lines spaced by your implement's working width",
                    "Pass number and distance off line while you drive",
                    "Set the lines once for the session"],
             shots=[("liveguidance", "A–B guidance lines on the live map")],
             note="<strong>Good to know:</strong> AgSaver's guidance uses your iPhone or iPad GPS and is a visual guide on screen. It doesn't steer the machine and isn't a replacement for RTK autosteer."),
        dict(id_="farm-map", eyebrow="Farm map", title="The whole farm on one map", flip=True,
             paras=["The farm map shows every field with its name and acres, and the work done on it. Turn this year's and last year's work sessions on and off to compare, and see your crew's machines where they're working right now."],
             ticks=["Every field outlined and labelled with its acres",
                    "Toggle this year's and last year's work",
                    "Crew machines and paths shown live",
                    "Also on the dashboard, with a pause button for the running session"],
             shots=[("fieldsreport", "All fields on satellite imagery")]),
    ],
    "More about mapping", "Everything here works from the GPS in your iPhone or iPad.",
    [("route", "Paths you can revisit", "Every session keeps its GPS path. Open any one later to see exactly where the machine went."),
     ("field", "Driving the edge", "Drive around a field during a session and turn that lap into the field's boundary."),
     ("users", "Crew on the map", "In a crew, everyone's machines and current paths show on your map, updated about every 30 seconds."),
     ("export", "GPX export", "Every GPS path goes into the Export Everything zip as a GPX file for mapping software."),
     ("doc", "Field PDFs with work", "Share a field on satellite imagery with its boundary and the work done on it."),
     ("pause", "Pauses aren't work", "Paused time isn't added to the hour meter, so a lunch break never counts as hours on the machine.")],
)

PAGES["fields.html"] = lambda: feature_page(
    "fields",
    "Outline your fields in AgSaver by tapping corners or driving the edge, or import boundaries from John Deere Operations Center, Climate FieldView or Google Earth as shapefile, KML, KMZ or GeoJSON.",
    "My Fields holds every field you farm, owned or rented. Draw them, drive them or import them, sort them into groups, and AgSaver matches your work to them automatically.",
    ("myfields", "My Fields"),
    [("outline", "Outline fields"), ("import", "Import boundaries"), ("groups", "Groups"), ("field-page", "Field details")],
    [
        dict(id_="outline", eyebrow="Outline fields", title="Tap the corners or drive the edge",
             paras=["Add a field by tapping its corners on the satellite map, or drive around it during a work session and turn that lap into the boundary. AgSaver tidies a driven boundary down to its corners and works out the acres."],
             ticks=["Up to 100 corners per field",
                    "Move a corner by dragging it",
                    "Acres calculated from the outline",
                    "Name each field the way your farm does"],
             shots=[("fieldmap", "Field outline on satellite imagery")]),
        dict(id_="import", eyebrow="Import", title="Bring your boundaries with you", flip=True,
             paras=["Already have your fields mapped? Export them from John Deere Operations Center, Climate FieldView, Google Earth or another mapping tool and open the file in AgSaver. It lists every boundary it finds so you can pick which ones to bring in."],
             ticks=["<strong>Shapefile</strong> (zipped), <strong>KML</strong>, <strong>KMZ</strong> and <strong>GeoJSON</strong>",
                    "Keeps farm or folder names from the file as groups",
                    "Choose which fields to import",
                    "Imported fields are added to the ones you already have"],
             shots=[("fieldsreport", "Imported field boundaries")]),
        dict(id_="groups", eyebrow="Groups", title="Sort fields by farm, quarter or landlord",
             paras=["Put fields into groups like Home Farm, North Farm or Rented Land. Each group shows its field count and total acres, and you can filter the map and reports by group."],
             ticks=["Collapse groups you're not working in",
                    "Total acres per group",
                    "Show or hide each field on the work map"],
             shots=[("farmmap", "All fields on the farm map")]),
        dict(id_="field-page", eyebrow="Field details", title="Everything about a field on one page", flip=True,
             paras=["Open a field to see it on satellite imagery with its area and corners, this year's crop, every work session that touched it, its sprays and inputs, yield and profit, and its crop history."],
             ticks=["Filter the field's work by year",
                    "Acres worked in each session",
                    "Share the field as a PDF and KML",
                    "Edit the boundary any time"],
             shots=[("fieldinputs", "Field page with crop and sprays")]),
    ],
    "Fields that do the bookkeeping for you", "Once your fields are in, the rest of AgSaver uses them.",
    [("pin", "Automatic matching", "Work sessions are matched to the fields they ran in, with the acres covered in each, without you picking a field."),
     ("doc", "Field reports", "Make a PDF of one field or all of them on satellite imagery, with KML boundaries to load into other mapping software."),
     ("sprout", "Crop records per field", "Each field carries its crops, sprays, inputs, yield and profit year by year."),
     ("chart", "My Fields report", "Acres, crops and work across all your fields, filtered by group or year."),
     ("sync", "Syncs with everything else", "Fields are included in backups, exports and iCloud sync between your devices."),
     ("import", "Many formats", "Shapefile bundles, KML and KMZ from Google Earth, and GeoJSON are all read straight from the Files app.")],
)

PAGES["crops.html"] = lambda: feature_page(
    "crops",
    "Record crops, sprays, fertilizer and seed by field in AgSaver, fill in spray conditions from Apple Weather, check the hourly spray window and see yield, revenue and profit per acre.",
    "Keep each field's crop, sprays and inputs as you go. AgSaver fills in the weather for spray records, shows you the spray window, and works out yield and profit at harvest.",
    ("fieldinputs", "Crop, sprays and inputs"),
    [("crop-year", "Crop year"), ("sprays", "Sprays & inputs"), ("spray-window", "Spray window"), ("profit", "Yield & profit")],
    [
        dict(id_="crop-year", eyebrow="Crop year", title="What each field grew, every year",
             paras=["For every field and year, record the crop and variety, seeding and harvest dates, bushels harvested and other costs such as land rent, crop insurance or custom work. The field keeps a crop history you can look back on."],
             ticks=["Crop, variety, seeding and harvest dates",
                    "Bushels for the whole field, shown as bu/ac",
                    "Other costs for the whole field",
                    "Crop history with past yields"],
             shots=[("zoom-crop", "Crop, variety, dates and bushels")]),
        dict(id_="sprays", eyebrow="Sprays & inputs", title="Spray records that fill themselves in", flip=True,
             paras=["Log each spray, fertilizer, seed or other product with its rate, acres and cost. Spray records usually need the wind speed, direction and temperature at the time of application, so tap <strong>Fill from Weather</strong> and AgSaver gets them from Apple Weather for that field at that date and time."],
             ticks=["Rate per acre, total product used and cost",
                    "Wind speed, direction and temperature",
                    "Spray Records report for the whole farm, by year and type",
                    "Share the year's spray records as a PDF"],
             shots=[("sprayrecords", "Spray records report")]),
        dict(id_="spray-window", eyebrow="Weather", title="An hour-by-hour spray window",
             paras=["The weather card on the dashboard shows conditions now and for the next 12 hours, with wind and temperature for each hour and a simple spray-window check from wind, temperature, humidity and rain."],
             ticks=["Wind speed, gusts and direction",
                    "Next 12 hours at a glance",
                    "Uses your location, or your first field when location is off",
                    "Turn the weather card on or off in Settings"],
             shots=[("zoom-sprays", "Spray records with wind and temperature")]),
        dict(id_="profit", eyebrow="Yield & profit", title="Profit per field and per acre", flip=True,
             paras=["Add the price and bushels at harvest and AgSaver shows the field's yield, revenue, inputs, fuel, other costs and profit, as totals and per acre. Fuel is estimated from the work sessions in that field."],
             ticks=["Yield in bu/ac",
                    "Revenue, inputs, fuel and other costs",
                    "Profit per field and per acre",
                    "Compare years in the crop history"],
             shots=[("yieldprofit", "Yield and profit for a field")],
             note="<strong>Good to know:</strong> profit per field leaves out machine ownership and repairs, which are covered in the machine cost reports instead."),
    ],
    "Records you can hand to anyone", "Clean records for your agronomist, crop insurance, landlord or your own planning.",
    [("doc", "Spray records PDF", "One PDF with every spray and input for the year, filtered by type, with conditions for each application."),
     ("wind", "Conditions on record", "Wind speed, direction and temperature saved with each spray, filled in from Apple Weather or typed in."),
     ("dollar", "Your currency", "Costs and revenue in the currency you choose in Settings."),
     ("history", "Crop history", "Every year's crop, variety and yield stays with the field."),
     ("field", "Applied acres", "Each record keeps the acres it covered, with totals for the farm."),
     ("drop", "Any product", "Herbicide, fungicide, fertilizer, seed or anything else you put on a field.")],
)

PAGES["machines.html"] = lambda: feature_page(
    "machines",
    "Track tractors, combines, sprayers and implements in AgSaver: service intervals by hours, reminders by hours or date, parts and filters, fuel consumption in L/hr and every running cost.",
    "The Farm screen keeps every machine and implement in one list with its hours and service bars. Behind each one is its service history, reminders, parts, fuel and costs.",
    ("farm", "Farm screen with machines"),
    [("farm", "Machines & implements"), ("service", "Service & reminders"), ("fuel", "Fuel"), ("costs", "Costs & parts")],
    [
        dict(id_="farm", eyebrow="Machines & implements", title="Every machine, with its hours and what's due",
             paras=["Add tractors, combines, sprayers, loaders and trucks with their make, model, year, photo and purchase price. Implements are kept separately and move between machines, keeping their own hours, working width and life expectancy."],
             ticks=["Hours and service bars on every card",
                    "See which implement is on which machine",
                    "Implement hours and percent of life remaining",
                    "Working width used for maps and acres"],
             shots=[("zoom-machine", "A machine with its implement and service bars")]),
        dict(id_="service", eyebrow="Service & reminders", title="Never miss a service", flip=True,
             paras=["Give each machine and implement a maintenance interval in hours. When it's due, AgSaver shows <strong>Service Required</strong>, and <strong>Mark Maintenance Done</strong> resets the count and opens a service record for the details. Add reminders for anything else, by hours or by date."],
             ticks=["Reminders that repeat every so many hours, or every year",
                    "Notifications when something comes due",
                    "Service records with date, hour reading, cost and notes",
                    "Full service history per machine"],
             shots=[("reminders", "Service reminders")]),
        dict(id_="fuel", eyebrow="Fuel", title="Fuel use you can actually trust",
             paras=["Log each fill-up with litres or gallons, price and hour meter reading. AgSaver works out consumption from full tank to full tank, counting partial fills in between, so the L/hr figure stays accurate."],
             ticks=["Litres per hour and fuel cost per acre",
                    "Fuel report by machine and by fill-up",
                    "Add fuel from Apple Watch",
                    "Litres or US gallons"],
             shots=[("startwork", "Quick entry for fuel, service and expenses")]),
        dict(id_="costs", eyebrow="Costs & parts", title="What each machine really costs to run", flip=True,
             paras=["Record parts, repairs, insurance and other expenses with a photo of the receipt. Keep part numbers for filters and belts on every machine so you have them at the dealer. The total cost of ownership report brings it all together."],
             ticks=["Expenses with receipt photos",
                    "Parts and filters list per machine and implement",
                    "Purchase price included in ownership cost",
                    "Ownership cost broken down into fuel, service and expenses"],
             shots=[("reports", "Machine reports")]),
    ],
    "The paperwork, handled", "Quick entry buttons on the dashboard mean the record gets made while you're still at the machine.",
    [("fuel", "Quick fuel entry", "Add fuel, service or an expense straight from the dashboard in a couple of taps."),
     ("receipt", "Receipt photos", "Snap the receipt and it stays with the expense, and goes into your full export."),
     ("parts", "Parts at hand", "Filter numbers, belts and other parts listed for every machine and implement."),
     ("bell", "Notifications", "Choose which reminders notify you and when."),
     ("history", "Service history report", "Every service record and its cost, filtered by machine and date."),
     ("gauge", "Life expectancy", "Set an implement's expected life in hours and see how much is left.")],
)

PAGES["reports.html"] = lambda: feature_page(
    "reports",
    "AgSaver reports for work, fuel, service, implements, cost of ownership, fields and sprays, plus live crew sharing, one-file sync for your crew, private iCloud sync and full data export.",
    "Reports for the whole farm, a way to keep your crew's hours and work together, and your data in formats you can open anywhere.",
    ("fieldsreport", "Field report"),
    [("reports-list", "Reports"), ("crew-sync", "Crew sync"), ("live-crew", "Live crew map"), ("export", "Your data")],
    [
        dict(id_="reports-list", eyebrow="Reports", title="Reports for the whole farm",
             paras=["Pick a report, filter it by machine, implement, field or dates, and share it as a PDF. Every report is built from the records you already keep."],
             ticks=["<strong>Work sessions</strong> by machine or implement",
                    "<strong>Total cost of ownership</strong> with a breakdown chart",
                    "<strong>Fuel consumption</strong> and fuel cost",
                    "<strong>Service history</strong>, <strong>implements</strong>, <strong>My Fields</strong> and <strong>spray records</strong>"],
             shots=[("reports", "Reports"), ("sprayrecords", "Spray records report")]),
        dict(id_="crew-sync", eyebrow="Crew sync", title="Keep everyone's hours in one place", flip=True,
             paras=["Send a sync file by Messages, AirDrop or email to everyone who runs your machines. When they open it, AgSaver adds any work sessions, service records and implements they don't have yet, and brings hour meters, implement hours and where each implement is installed up to date."],
             ticks=["One file, any way you like to send it",
                    "Opening the same file twice never adds anything twice",
                    "Works without anyone joining an account"],
             shots=[("crew-sync", "Sync all work sessions")]),
        dict(id_="live-crew", eyebrow="Live crew map", title="See where everyone is working",
             paras=["Start a crew and send the code to the people who run your machines. While anyone in the crew is running a work session, their machine and the path they're working show on your work map and dashboard map, updated about every 30 seconds."],
             ticks=["Positions are only sent while a work session runs",
                    "Only people with your crew code can see them",
                    "Leave the crew any time to stop sharing"],
             shots=[("farmmap", "Crew machines on the farm map")]),
        dict(id_="export", eyebrow="Your data", title="Your records, in files you can open anywhere", flip=True,
             paras=["AgSaver syncs through your own private iCloud between your iPhone and iPad. Whenever you want a copy, export it: CSV for Excel or Numbers, or one zip with everything."],
             ticks=["<strong>Export Everything</strong>: database, machine photos, receipts, GPS paths as GPX and a spreadsheet",
                    "<strong>Export Records</strong>: fuel, service and expenses as CSV",
                    "<strong>Import</strong> a zip, backup or CSV, added to what you have",
                    "Moving to a new phone? iCloud brings it all with you"],
             shots=[("myfields", "My Fields with share buttons")]),
    ],
    "Share what you need, keep the rest private", "Nothing leaves your devices unless you send it.",
    [("cloud", "Private iCloud sync", "Your data syncs through your own iCloud, which only you can access. No AgSaver account needed."),
     ("sync", "Restore anywhere", "Set up a new device and AgSaver finds your existing data, or import a backup or sync file."),
     ("doc", "PDF reports", "Work, fuel, service, field and spray reports share as PDFs from the share sheet."),
     ("map", "KML and GPX", "Field boundaries export as KML and work paths as GPX for other mapping software."),
     ("shield", "Crew sharing is opt-in", "Crew positions are off unless you start or join a crew, and stop when work stops."),
     ("export", "CSV for spreadsheets", "Fuel, service and expense records open straight in Excel or Numbers.")],
)

# ---------- Support ----------
FAQ = [
    ("Getting started", [
        ("What devices does AgSaver run on?", "AgSaver runs on iPhone and iPad, with a companion app for Apple Watch. Your data syncs between them through your own iCloud."),
        ("Do I need to create an account?", "No. AgSaver uses the Apple ID you're already signed in with. If iCloud is turned on, your records sync between your devices automatically."),
        ("I already use AgSaver on another device. How do I set up a new one?", "Sign in to the same Apple ID with iCloud Drive turned on, then open AgSaver. It looks for your existing data before setting anything up. You can also import a backup (.json), a CSV file, an Export Everything zip or a crew sync file (.agsync) from the welcome screen or Settings."),
        ("Can I track more than one machine?", "Yes. Add as many machines and implements as you like. Each keeps its own hours, service history, fuel, expenses and work records."),
    ]),
    ("Work sessions and maps", [
        ("Why does AgSaver ask for my location?", "Location is used while a work session is running, to record the path your machine travels, match the work to your fields and count acres. It's also used to look up the weather for your farm. If you declined earlier, turn it back on in Settings → Privacy &amp; Security → Location Services → AgSaver."),
        ("How does auto pause work?", "In AgSaver's Settings, choose how many minutes the machine can stand still. When it stops moving for that long, the work clock pauses from when it last moved, so the idle time isn't added to the hour meter. It starts again when the machine drives off."),
        ("Does the guidance steer my tractor?", "No. A–B lines and acres remaining are a visual guide using your iPhone or iPad GPS. They don't control the machine and aren't a replacement for RTK autosteer."),
        ("How accurate are the acres?", "Acres come from your device's GPS and the working width set on the implement. Phone GPS is usually within a few metres, which is close for field totals but not survey-grade."),
    ]),
    ("Fields, crops and sprays", [
        ("Which field boundary files can I import?", "Zipped shapefiles, KML, KMZ and GeoJSON, including exports from John Deere Operations Center, Climate FieldView and Google Earth. Open the file from the Files app or choose Import in My Fields."),
        ("Where does the spray weather come from?", "Fill from Weather asks Apple Weather for the conditions at that field at the date and time of the application. You can also type the wind and temperature in yourself."),
        ("What's included in profit per field?", "Revenue from the harvest, minus inputs, fuel estimated from work sessions in that field, and the other costs you enter for the field. Machine ownership and repairs are reported separately."),
    ]),
    ("Service, crew and data", [
        ("How do I keep on top of servicing?", "Set a maintenance interval for each machine and implement. AgSaver shows the hours left on a bar that turns red when service is due, and Mark Maintenance Done resets it and opens a service record. Add reminders by hours or by date for everything else."),
        ("How do I share hours and work with my crew?", "In Settings, use Send Sync File to send one file by Messages, AirDrop or email. When someone opens it, AgSaver adds the work sessions, service records and implements they're missing and updates hour meters. For a live view, Start a Crew and share the code."),
        ("How do I get my data out?", "Settings → Export Everything makes one zip with the complete database, photos, receipts, GPS paths as GPX and a spreadsheet. Export Records saves fuel, service and expense records as CSV."),
        ("I found a bug or have an idea.", f'I\'d love to hear it. Email <a href="mailto:{EMAIL}">{EMAIL}</a> with what happened, and a screenshot if you can.'),
    ]),
]

def support():
    blocks = ""
    for sec, qs in FAQ:
        blocks += f"<h2>{sec}</h2>" + "".join(
            f'<details class="faq"><summary>{q}</summary><div class="a"><p>{a}</p></div></details>' for q, a in qs)
    return head("Support — AgSaver", "Help and frequently asked questions for AgSaver, the farm machine app for iPhone, iPad and Apple Watch.", "support.html") + header("support") + f"""<main>
<div class="wrap doc">
  <div class="eyebrow">Support</div>
  <h1>How can I help?</h1>
  <p class="lead">Answers to the most common questions about AgSaver. If you don't find what you need, send me an email and I'll get back to you.</p>
  <div class="contact-card"><div><h2>Email support</h2><p>{EMAIL}</p></div><a class="btn btn-green" href="mailto:{EMAIL}?subject=AgSaver%20support">{I['mail'].replace('<svg', '<svg width="18" height="18"')} Email me</a></div>
  {blocks}
  <h2>Purchases</h2>
  <details class="faq"><summary>How do I restore a purchase?</summary><div class="a"><p>Sign in with the same Apple ID you used to buy AgSaver, then download it again from the App Store. Purchases are tied to your Apple ID.</p></div></details>
  <details class="faq"><summary>How is my data handled?</summary><div class="a"><p>See the <a href="privacy.html">privacy policy</a> for full details.</p></div></details>
</div>
""" + cta() + "</main>\n" + footer()

PAGES["support.html"] = support

# ---------- Privacy (same wording as glennbonnet.com/privacy-agsaver.html) ----------
def privacy():
    return head("Privacy Policy — AgSaver", "How AgSaver handles your information.", "privacy.html") + header("privacy") + f"""<main>
<div class="wrap doc">
  <div class="eyebrow">Legal</div>
  <h1>AgSaver Privacy Policy</h1>
  <p class="updated">Effective date: 10 November 2026</p>
  <p>This Privacy Policy explains how Glenn Bonnet ("I", "me", "my") handles information when you use AgSaver (the "App"). It applies only to AgSaver.</p>
  <p><strong>Your privacy matters. I collect as little information as possible, and I never sell your personal information.</strong></p>

  <h2>1. Information you enter in the App</h2>
  <p>AgSaver lets you record information for your own use, such as agricultural equipment details, service records, parts, expenses, work sessions and hour logs, fuel, field boundaries, crop, yield, spray and input records, photos and notes.</p>
  <p>This information is stored on your device and, if you are signed in to iCloud, synced through your own private iCloud database, which only you can access. Optional crew sharing is the one exception, described below. I do not have access to the content you enter. Backups, sync files, spreadsheets and reports are created only when you ask, and go wherever you choose to save or share them.</p>

  <h2>2. Permissions</h2>
  <p>AgSaver may ask for access to your camera, photo library or notifications, for example to add a photo of a machine or receipt, or to alert you when maintenance is due. This access is only used for the feature you choose.</p>
  <p><strong>Location:</strong> AgSaver uses your location while a work session is running, to record the path your machine travels so you can see where you worked on a map, which fields you worked in and how many acres you covered. You can also record a field boundary by driving around it. Routes and field boundaries are saved with your own data and are not sent to me.</p>
  <p><strong>Weather:</strong> to show the weather and spray window, and to fill in conditions for work sessions and spray records, AgSaver asks Apple Weather for the forecast at your current location, or at a saved field or work path. These requests are handled by Apple under its privacy policy and are not sent to me.</p>
  <p><strong>Crew sharing:</strong> if you start or join a crew, then while a work session is running AgSaver shares the name you choose, your machine's position and recent work path, the machine and implement names, and whether you are working or paused. This is stored in AgSaver's iCloud public database under your crew code, and only people who have the code can look it up. Positions are not sent when no work session is running, and leaving the crew removes your entry. Crew sharing is off unless you turn it on.</p>
  <p>You can change any permission at any time in your device settings.</p>

  <h2>3. Information collected automatically</h2>
  <p>The App may collect limited, non-identifying technical information, such as crash reports and basic usage statistics, to help fix bugs and improve it. This information is not used to identify you personally.</p>

  <h2>4. Purchases and subscriptions</h2>
  <p>If you make an in-app purchase or subscribe, payment is handled entirely by the Apple App Store. I never receive or store your payment card details.</p>

  <h2>5. How information is used</h2>
  <p>Any information I do receive is used only to:</p>
  <ul><li>provide, maintain and improve the App;</li><li>fix bugs and resolve technical problems;</li><li>reply to you when you contact me for support.</li></ul>

  <h2>6. Sharing of information</h2>
  <p>I do not sell, rent or trade your personal information. Information is only shared with service providers needed to run the App (such as the App Store), or where required by law.</p>

  <h2>7. When you contact me</h2>
  <p>If you email me, I will receive your email address and anything you include in your message. I use this only to respond to you, and I do not add you to any mailing list without your permission.</p>

  <h2>8. Data retention and deletion</h2>
  <p>Because your data is stored on your device, you can delete it at any time within the App or by uninstalling the App. Data stored in your own iCloud can be managed through your device or iCloud settings. If you have emailed me and would like that correspondence deleted, just ask.</p>

  <h2>9. Children's privacy</h2>
  <p>The App is not directed at children under 13, and I do not knowingly collect personal information from children.</p>

  <h2>10. Your rights</h2>
  <p>Depending on where you live, you may have the right to access, correct or delete personal information held about you, or to object to how it is used. To make a request, contact me using the details below.</p>

  <h2>11. Changes to this policy</h2>
  <p>I may update this policy from time to time. Changes will be posted on this page with a new effective date.</p>

  <h2>12. Contact</h2>
  <p>If you have any questions about this Privacy Policy, please email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
</main>
""" + footer()

PAGES["privacy.html"] = privacy

def notfound():
    # 404 is served from any path, so use absolute links.
    return (head("Page not found — AgSaver", "This page doesn't exist.", "404.html") + header() + f"""<main>
<div class="wrap notfound"><h1>404</h1><p>That page isn't here. It may have moved.</p>
<div class="btns"><a href="index.html" class="btn btn-green">Go to the home page</a>{appstore()}</div></div>
</main>
""" + footer()).replace('href="index.html', 'href="/index.html').replace('href="support.html', 'href="/support.html') \
        .replace('href="privacy.html', 'href="/privacy.html').replace('src="img/', 'src="/img/').replace('href="img/', 'href="/img/') \
        .replace('href="style.css', 'href="/style.css')

def fix404(s):
    for sl in BY:
        s = s.replace(f'href="{sl}.html', f'href="/{sl}.html')
    return s

PAGES["404.html"] = lambda: fix404(notfound())

if __name__ == "__main__":
    for name, fn in PAGES.items():
        with open(os.path.join(ROOT, name), "w") as f:
            f.write(fn())
        print("wrote", name)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for name in PAGES:
            if name == "404.html":
                continue
            loc = SITE + "/" + ("" if name == "index.html" else name)
            f.write(f"  <url><loc>{loc}</loc></url>\n")
        f.write("</urlset>\n")
    print("wrote sitemap.xml")
