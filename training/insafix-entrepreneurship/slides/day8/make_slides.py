"""Write the Day 8 (Hijama, class 1) slide files from the offline hijama deck, same look as Days 1–7."""

import json
from pathlib import Path

_day5 = (Path(__file__).parent.parent / "day5" / "make_slides.py").read_text(encoding="utf-8")
exec(_day5.split("slides = {}")[0])

ROOT = Path(__file__).parent / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 12
LOGO_ALINSAF = "/_blob/17c0f1127301ef26ac7b47bed5b147f0"
LOGO_INSAFIX = "/_blob/24859317a9d57d42f322d491d77398d4"
NOTE = '<span style="color:#1F7A42"> · নোট করুন</span>'


def quote_card(text, ref):
    return (
        '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:24px;padding:32px 40px;display:flex;flex-direction:column;gap:18px">'
        f'<p style="{HEAD};font-size:80px;font-weight:800;line-height:0.6;color:#F28C28">“</p>'
        f'<p style="font-size:34px;font-weight:700;line-height:1.45;color:#12352A">{text}</p>'
        f'<p style="font-size:26px;line-height:1.4;color:#1F7A42">{ref}</p></div>'
    )


def numbered(items, start):
    parts = ['<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 24px">']
    for i, t in enumerate(items):
        n = str(start + i).translate(BN)
        parts.append(
            '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:16px;padding:14px 22px;display:flex;flex-direction:row;gap:18px;align-items:center">'
            f'<p style="{HEAD};font-size:30px;font-weight:800;color:#FFFFFF;background:#2E9E5B;border-radius:999px;padding:2px 16px">{n}</p>'
            f'<p style="font-size:28px;line-height:1.35">{t}</p></div>'
        )
    parts.append("</div>\n")
    return "\n".join(parts)


slides = {}

slides["cover"] = f"""<section id="cover" data-transition="fade" style="background:#F6F7F0;color:#12352A;{FONT};padding:88px 128px 104px;display:flex;flex-direction:column;justify-content:space-between">
<svg aria-label="" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0;width:1920px;height:1080px"><defs><radialGradient id="glow" cx="78%" cy="38%" r="60%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.55" stop-color="#F6F7F0"/><stop offset="1" stop-color="#E7F0E1"/></radialGradient><linearGradient id="w1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFD3A1" stop-opacity="0"/><stop offset="0.45" stop-color="#F28C28"/><stop offset="1" stop-color="#D9731A"/></linearGradient><linearGradient id="w2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8DC63F" stop-opacity="0"/><stop offset="0.5" stop-color="#8DC63F"/><stop offset="1" stop-color="#2E9E5B"/></linearGradient></defs><rect width="1920" height="1080" fill="url(#glow)"/><path d="M0 930 C 420 820, 760 1040, 1180 930 S 1700 800, 1920 860 L1920 1080 L0 1080 Z" fill="#DCEBD3" opacity="0.8"/><path d="M0 960 C 400 860, 780 1060, 1200 960 S 1720 830, 1920 890" fill="none" stroke="url(#w1)" stroke-width="5"/><path d="M0 1000 C 430 900, 800 1080, 1220 990 S 1730 870, 1920 930" fill="none" stroke="url(#w2)" stroke-width="3" opacity="0.9"/><circle cx="1580" cy="470" r="330" fill="none" stroke="#2E9E5B" stroke-opacity="0.18" stroke-width="2"/><circle cx="1580" cy="470" r="390" fill="none" stroke="#F28C28" stroke-opacity="0.2" stroke-width="2" stroke-dasharray="6 14"/></svg>
<div style="display:flex;flex-direction:row;gap:20px;align-items:center">
<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:10px 22px;display:flex;flex-direction:row;gap:14px;align-items:center;box-shadow:0 6px 20px rgba(18,53,42,0.08)">
<img src="{LOGO_ALINSAF}" alt="আল-ইনসাফ লাইফ কেয়ার লোগো" style="width:62px;height:80px;object-fit:contain">
<p style="font-size:24px;font-weight:700;line-height:1.15;color:#0E3B2C">Al-Insaf<br><span style="color:#C2620A">Life Care</span></p>
</div>
<x-shape kind="line" style="background:#F28C28;width:36px;height:2px"></x-shape>
<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:10px 22px;display:flex;flex-direction:row;gap:14px;align-items:center;box-shadow:0 6px 20px rgba(18,53,42,0.08)">
<img src="{LOGO_INSAFIX}" alt="ইনসাফিক্স একাডেমি লোগো" style="width:80px;height:80px;object-fit:contain">
<p style="font-size:24px;font-weight:700;line-height:1.15;color:#0E3B2C">Insafix<br><span style="color:#1597B8">Academy</span></p>
</div>
</div>
<div style="display:flex;flex-direction:column;gap:28px;width:1120px">
<div style="display:flex;flex-direction:row;gap:16px;align-items:center">
<p style="{HEAD};font-size:28px;font-weight:800;color:#3A1E05;background:#F28C28;padding:6px 22px;border-radius:999px;letter-spacing:2px">DAY 08</p>
<p style="font-size:28px;font-weight:600;color:#4A6358;letter-spacing:1px">হিজামা · প্রথম ক্লাস</p>
</div>
<h1 style="{HEAD};font-size:100px;font-weight:800;line-height:1.1;color:#12352A">হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span></h1>
</div>
<div style="display:flex;flex-direction:row;gap:36px;align-items:center;width:1120px">
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span></p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span></p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">উপকারিতা<br><span style="color:#1F7A42">ও কার্যপদ্ধতি</span></p></div>
</div>
<div style="display:flex;flex-direction:row;gap:18px;align-items:center;background:#FFFFFF;border:1px solid #CFE0C6;border-radius:999px;padding:14px 32px;width:1120px;box-shadow:0 6px 20px rgba(18,53,42,0.08)">
<x-icon name="Book" style="color:#2E9E5B;width:36px;height:36px"></x-icon>
<p style="font-size:28px;color:#12352A"><b style="color:#B85A0C">খাতা-কলম নিন:</b> আজকের প্রতিটি বিষয় নোট করে রাখুন</p>
</div>
<div style="position:absolute;left:1370px;top:260px;width:420px;height:420px;border-radius:50%;border:6px solid #2E9E5B;background:#FFFFFF;box-shadow:0 20px 60px rgba(18,53,42,0.12);display:flex;flex-direction:column;align-items:center;justify-content:center">
<p style="{HEAD};font-size:56px;font-weight:800;letter-spacing:6px;color:#12352A">DAY</p>
<p style="{HEAD};font-size:200px;font-weight:800;line-height:1;color:#1F8A4C">০৮</p>
<p style="font-size:26px;font-weight:600;color:#B85A0C">হিজামা · ক্লাস ১</p>
</div>
<aside>আজ থেকে হিজামার ক্লাস শুরু। এই অনলাইন ক্লাসগুলোতে হিজামার তত্ত্বের অংশ শেখানো হবে, যা অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ আর আলোচনা হবে না। তাই সবাইকে খাতা-কলম নিয়ে প্রতিটি বিষয় নোট করে রাখতে বলুন।</aside>
</section>
"""

slides["what"] = statement("what", "হিজামা ও কাপিং · প্রাথমিক আলোচনা", "হিজামা কী?", "",
    "হিজামা হলো একটি চিকিৎসা পদ্ধতি যেখানে নির্দিষ্ট স্থানে কাপ বসিয়ে হালকা “স্ক্র্যাচ” (আঁচড় দেওয়া) করে রক্ত বের করা হয়।", 2,
    "হিজামা হলো একটি চিকিৎসা পদ্ধতি যেখানে নির্দিষ্ট স্থানে কাপ বসিয়ে হালকা স্ক্র্যাচ বা আঁচড় দিয়ে রক্ত বের করা হয়।")

types = [
    ("Lock", "ড্রাই কাপিং", "ত্বকে শুধু কাপ বসিয়ে ভ্যাকুয়াম তৈরি করা হয়, কোনো আঁচড় দেওয়া হয় না।", False),
    ("Verified", "ওয়েট কাপিং (হিজামা)", "কাপ বসানোর পর ত্বকে হালকা আঁচড় দিয়ে রক্ত বের করা হয়। এটিই প্রকৃত হিজামা।", True),
    ("Lightning", "ফায়ার কাপিং", "কাপের ভেতরে আগুন ব্যবহার করে অক্সিজেন বের করে ভ্যাকুয়াম তৈরি করা হয়।", False),
]
tcards = []
for i, (ic, name, desc, hi) in enumerate(types, 1):
    box = "background:#1F7A42" if hi else "background:#FFFFFF;border:1px solid #DCE6D6"
    tc, dc, cb, cf = ("#FFFFFF", "#D7F0C2", "#FFFFFF", "#1F7A42") if hi else ("#12352A", "#4A6358", "#2E9E5B", "#FFFFFF")
    tcards.append(
        f'<div style="flex:1;{box};border-radius:28px;padding:36px 32px;display:flex;flex-direction:column;gap:18px">'
        f'<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:{cb};border-radius:999px;padding:18px;display:flex"><x-icon name="{ic}" style="color:{cf};width:44px;height:44px"></x-icon></div>'
        f'<p style="{HEAD};font-size:40px;font-weight:800;color:{"#F6B26B" if hi else "#B85A0C"}">{str(i).translate(BN)}</p></div>'
        f'<h3 style="font-size:38px;font-weight:700;color:{tc}">{name}</h3>'
        f'<p style="font-size:29px;line-height:1.5;color:{dc}">{desc}</p></div>'
    )
slides["types"] = light("types", "#EEF5EA",
    header("CUPPING TYPES" + NOTE, "তিন ধরনের কাপিং", "পদ্ধতি প্রচলিত")
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n' + "\n".join(tcards) + "\n</div>\n<div></div>\n",
    3, "তিন ধরনের কাপিং: ড্রাই কাপিং, ওয়েট কাপিং আর ফায়ার কাপিং। ওয়েট কাপিং-ই প্রকৃত হিজামা।")

hist = [
    ("প্রাচীন মিশর", "খ্রিস্টপূর্ব ১৫৫০ সালে লেখা 'এবারস প্যাপিরাস'-এ হিজামার উল্লেখ পাওয়া যায়, যা এর প্রাচীনত্বের প্রমাণ।"),
    ("প্রাচীন চীন", "৩০০০ বছর ধরে ঐতিহ্যবাহী চীনা চিকিৎসায় হিজামা একটি গুরুত্বপূর্ণ অংশ।"),
    ("আরব সভ্যতা", "ইসলামের আগমনের পূর্ব থেকেই আরব উপদ্বীপে এটি ব্যথানাশক এবং আরোগ্যকারী হিসেবে পরিচিত ছিল।"),
    ("ইসলামে হিজামা", "রাসূলুল্লাহ সাল্লাল্লাহু আলাইহি ওয়াসাল্লামের মাধ্যমে এটি একটি সুন্নাহ চিকিৎসা হিসেবে প্রতিষ্ঠিত হয় এবং মুসলিম সমাজে এর প্রচলন বাড়ে।"),
]
hparts = []
for i, (t, d) in enumerate(hist, 1):
    last = i == 4
    box = "background:#1F7A42" if last else "background:#FFFFFF;border:1px solid #DCE6D6"
    hparts.append(
        f'<div style="flex:1;{box};border-radius:24px;padding:28px 28px;display:flex;flex-direction:column;gap:14px">'
        f'<p style="{HEAD};font-size:30px;font-weight:800;color:{"#3A1E05" if last else "#FFFFFF"};background:{"#F28C28" if last else "#2E9E5B"};border-radius:999px;padding:2px 18px;align-self:start">{str(i).translate(BN)}</p>'
        f'<h3 style="font-size:34px;font-weight:700;color:{"#FFFFFF" if last else "#12352A"}">{t}</h3>'
        f'<p style="font-size:26px;line-height:1.5;color:{"#D7F0C2" if last else "#4A6358"}">{d}</p></div>'
    )
    if not last:
        hparts.append('<x-shape kind="arrow-right" style="background:#F28C28;width:36px;height:18px"></x-shape>')
slides["history"] = light("history", "#F6F7F0",
    header("HISTORY · হিজামার সুদীর্ঘ ইতিহাস" + NOTE, "প্রাচীন সভ্যতা থেকে", "সুন্নাহ পর্যন্ত")
    + '<p style="font-size:30px;line-height:1.45;color:#4A6358">হিজামা কোনো নতুন চিকিৎসা পদ্ধতি নয়, বরং এর শিকড় গ্রথিত প্রাচীন সভ্যতার গভীরে।</p>\n'
    + '<div style="display:flex;flex-direction:row;gap:12px;align-items:stretch">\n' + "\n".join(hparts) + "\n</div>\n",
    4, "হিজামার ইতিহাস চার ধাপে: প্রাচীন মিশর, প্রাচীন চীন, আরব সভ্যতা, আর ইসলামে সুন্নাহ চিকিৎসা হিসেবে প্রতিষ্ঠা।")

slides["hadith1"] = light("hadith1", "#EEF5EA",
    header("HADITH · হিজামা সংক্রান্ত গুরুত্বপূর্ণ হাদিস" + NOTE, "হিজামা সংক্রান্ত", "হাদিস (১)")
    + '<p style="font-size:30px;line-height:1.45;color:#4A6358">ইসলামে হিজামার গুরুত্ব অপরিসীম, যা একাধিক হাদিসে বর্ণিত হয়েছে।</p>\n'
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n'
    + quote_card("তোমরা যেসব চিকিৎসা গ্রহণ করে থাকো তার মধ্যে হিজামা হলো সর্বোত্তম চিকিৎসা।", "আবু দাউদঃ ৩৮৫৭ (আবু হুরাইরাহ (রাঃ) থেকে বর্ণিত)")
    + quote_card("মিরাজের রাতে ফেরেশতাদের যে দলের সম্মুখ দিয়েই তিনি যাচ্ছিলেন তারা বলেছেন, আপনার উম্মাতকে হিজামা গ্রহণের নির্দেশ দিন।", "তিরমিযীঃ ২০৫২ (ইবনু মাসউদ রাযি. থেকে বর্ণিত)")
    + "\n</div>\n",
    5, "দুটি হাদিস: আবু দাউদ ৩৮৫৭, আর তিরমিযী ২০৫২। রেফারেন্সসহ নোট করতে বলুন।")

slides["hadith2"] = light("hadith2", "#F6F7F0",
    header("HADITH · হিজামা সংক্রান্ত গুরুত্বপূর্ণ হাদিস" + NOTE, "হিজামা সংক্রান্ত", "হাদিস (২)")
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n'
    + quote_card("আপনি অবশ্যই হিজামা করাবেন।", "তিরমিযীঃ ২০৫৩ (ইকরিমা (রহঃ) বলেন, ইবনু আব্বাস (রাঃ) থেকে বর্ণিত)")
    + quote_card("তিনটি জিনিসের মধ্যে রোগমুক্তি আছে। মধু পান, হিজামা লাগানো এবং আগুন দিয়ে দাগ লাগানো। তবে আমার উম্মতকে আগুন দিয়ে দাগ দিতে নিষেধ করছি।", "বুখারীঃ ৫৬৮০, ৫৬৮১, ৫৬৮৩, মিশকাতঃ ৪৫১৬ (ইবনু আব্বাস রাযি. থেকে বর্ণিত)")
    + "\n</div>\n<div></div>\n",
    6, "আরও দুটি হাদিস: তিরমিযী ২০৫৩, আর বুখারী ৫৬৮০, ৫৬৮১, ৫৬৮৩ ও মিশকাত ৪৫১৬।")

benefits = [
    "মানুষের দেহে রোগ প্রতিরোধ ক্ষমতা বৃদ্ধি করে", "দেহে রক্ত সঞ্চালন বৃদ্ধি করে", "রক্তনালী পরিষ্কার করে এবং রক্ত সঞ্চালন সক্রিয় করে",
    "টিস্যু থেকে বিষ মুক্ত করতে সহায়তা করে", "লিম্ফ্যাটিক সিস্টেম সক্রিয় করে", "শরীরের হরমোন জনিত সমস্যা সমাধান করে",
    "কিডনি ও লিভারকে পরিষ্কার করে", "হজম শক্তি বৃদ্ধি করে", "ত্বক পরিষ্কার করে", "ঘুমের উন্নতি করে",
    "শারীরিক শক্তি বৃদ্ধি করে", "মাথা ব্যথার জন্য বিশেষ উপকারী", "বাত/ব্যথা দূর করে", "গ্যাস্ট্রিক সমস্যা দূর করে",
    "হৃদ রোগের ঝুঁকি কমায় এবং হার্ট সুস্থ রাখে", "অনেক রোগ সৃষ্টিকারী এবং শরীরের জন্য মারাত্মক ক্ষতিকর পদার্থ রক্ত থেকে নিঃসৃত করে",
    "শরীরের ব্যথা/জ্বালাপোড়া হ্রাস করে", "শরীরের জয়েন্টগুলোতে ব্যাথা, ঘাড়, হাঁটু এবং কোমর ব্যথা দূর করতে সাহায্য করে",
    "আমরা যে ওষুধ খাই তার প্রভাবকে আরো কার্যকরী করে",
]
slides["benefits1"] = light("benefits1", "#EEF5EA",
    header("BENEFITS · হিজামার উপকারিতা" + NOTE, "হিজামার অসাধারণ", "উপকারিতা (১)")
    + numbered(benefits[:10], 1) + "<div></div>\n",
    7, "হিজামার উপকারিতা, প্রথম ১০টি।")
slides["benefits2"] = light("benefits2", "#F6F7F0",
    header("BENEFITS · হিজামার উপকারিতা" + NOTE, "হিজামার অসাধারণ", "উপকারিতা (২)")
    + numbered(benefits[10:], 11) + "<div></div>\n",
    8, "হিজামার উপকারিতা, বাকি ৯টি।")

slides["pain"] = light("pain", "#EEF5EA",
    header("HOW IT WORKS" + NOTE, "হিজামা করালে কিভাবে", "ব্যথা কমে?")
    + cards([("১", "রক্ত জমে চাপ", "ব্যথার জায়গায় সাধারণত রক্ত জমে চাপ তৈরি হয়"), ("২", "চাপযুক্ত রক্ত বের হয়", "হিজামার মাধ্যমে সেই রক্ত বের হয়ে যায়"),
             ("৩", "নার্ভের চাপ কমে", "রক্ত চলাচল ভালো হয়"), ("৪", "ব্যথা হালকা লাগে", "এ কারণেই হিজামার পর")], icons=False, arrows=True)
    + "<div></div>\n",
    9, "ব্যথার জায়গায় সাধারণত রক্ত জমে চাপ তৈরি হয়। হিজামার মাধ্যমে সেই চাপযুক্ত রক্ত বের হয়ে যায়। এর ফলে নার্ভের উপর চাপ কমে এবং রক্ত চলাচল ভালো হয়। এ কারণেই হিজামার পর ব্যথা হালকা লাগে।")

slides["blood"] = light("blood", "#F6F7F0",
    header("BLOOD SOURCE" + NOTE, "হিজামায় রক্ত আসে", "কোথা থেকে?")
    + cards([("Warning", "শিরা কাটা হয় না", "হিজামায় শিরা বা ভেইন কাটা হয় না"), ("Search", "চামড়ার উপরের স্তর", "সেখান থেকে রক্ত বের হয়"),
             ("Activity", "জমে থাকা রক্ত", "অক্সিজেন কম থাকা রক্ত"), ("Verified", "নিরাপদ পদ্ধতি", "তাই নিরাপদ হিসেবে গণ্য হয়")])
    + "<div></div>\n",
    10, "হিজামায় শিরা বা ভেইন কাটা হয় না। চামড়ার উপরের স্তর থেকে রক্ত বের হয়। এটি মূলত জমে থাকা, অক্সিজেন কম থাকা রক্ত। তাই হিজামা নিরাপদ পদ্ধতি হিসেবে গণ্য হয়।")

slides["task"] = light("task", "#EEF5EA",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Book" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">হিজামা সম্পর্কে শিক্ষামূলক কনটেন্ট তৈরি ও প্রচার</p>\n</div>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">\n'
      '<p style="font-size:30px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px"><b>নোট:</b> <span style="color:#4A6358">আজকের সব বিষয় খাতায় গুছিয়ে লিখুন</span></p>\n'
      '<p style="font-size:30px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px"><b>পোস্ট:</b> <span style="color:#4A6358">হিজামা কী ও এর ইতিহাস নিয়ে ১টি পোস্ট</span></p>\n</div>\n',
    11, "আজকের কাজ: হিজামা সম্পর্কে শিক্ষামূলক কনটেন্ট তৈরি ও প্রচার। আর আজকের সব বিষয় খাতায় গুছিয়ে নোট করা। রিপোর্ট জমার শেষ সময়: [সময়]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:96px;font-weight:800;line-height:1.15;text-align:center;color:#FFFFFF">হিজামা: <span style="color:#A6D65A">দ্বিতীয় ক্লাস</span></h2>
<p style="font-size:36px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">হাতে-কলমে পুরো পদ্ধতি শেখানো হবে অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ।</p>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(12)} / {num(TOTAL)}</p>
<aside>আগামীকাল হিজামার দ্বিতীয় ক্লাস। মনে করিয়ে দিন, হাতে-কলমে পুরো পদ্ধতি শেখানো হবে অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "what", "types", "history", "hadith1", "hadith2", "benefits1", "benefits2", "pain", "blood", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-02T10:00:00Z"},
    "lists": "css",
    "title": "অষ্টম দিন — হিজামা: প্রথম ক্লাস",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "হিজামা কী, কাপিং-এর ধরন ও ইতিহাস", "start": "cover"},
        "s2": {"description": "হাদিস ও উপকারিতা", "start": "hadith1"},
        "s3": {"description": "কার্যপদ্ধতি, আজকের কাজ ও পরের ক্লাস", "start": "pain"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
