"""Write the Day 5 (Smart Body Halua) slide files, same look as Day 4."""

import json
from pathlib import Path

ROOT = Path(__file__).parent / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)

PRODUCT = "/_blob/4b96641fe86b3568bdefbc18fdb64f6c"
LOGO_ALINSAF = "/_blob/3bd78f22f71164d56d200dd7ff45a51d"
LOGO_INSAFIX = "/_blob/75d5722fd5410b4f4396c8d177112232"
TOTAL = 13
BN = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
FONT = "font-family:'Hind Siliguri', Arial, sans-serif"
HEAD = "font-family:'Baloo Da 2', 'Hind Siliguri', sans-serif"

STRIP = '<svg aria-label="" width="1920" height="60" viewBox="0 0 1920 60" style="position:absolute;left:0;top:1020px;width:1920px;height:60px"><path d="M0 30 C 480 0, 960 60, 1440 25 S 1800 10, 1920 22" fill="none" stroke="#F28C28" stroke-width="3" opacity="0.6"/><path d="M0 45 C 480 15, 960 75, 1440 40 S 1800 25, 1920 37" fill="none" stroke="#8DC63F" stroke-width="2" opacity="0.6"/></svg>'
DARK_BG = '<svg aria-label="" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0;width:1920px;height:1080px"><defs><radialGradient id="dg" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#1F6B45"/><stop offset="0.6" stop-color="#12352A"/><stop offset="1" stop-color="#0C261D"/></radialGradient><linearGradient id="dw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFD3A1" stop-opacity="0"/><stop offset="0.45" stop-color="#F28C28"/><stop offset="1" stop-color="#D9731A"/></linearGradient></defs><rect width="1920" height="1080" fill="url(#dg)"/><path d="M0 990 C 400 910, 780 1070, 1200 995 S 1720 890, 1920 930" fill="none" stroke="url(#dw)" stroke-width="4"/></svg>'
SOFT_BG = '<svg aria-label="" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0;width:1920px;height:1080px"><defs><radialGradient id="sg" cx="50%" cy="40%" r="65%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.6" stop-color="#F6F7F0"/><stop offset="1" stop-color="#E7F0E1"/></radialGradient><linearGradient id="s1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFD3A1" stop-opacity="0"/><stop offset="0.45" stop-color="#F28C28"/><stop offset="1" stop-color="#D9731A"/></linearGradient><linearGradient id="s2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8DC63F" stop-opacity="0"/><stop offset="0.5" stop-color="#8DC63F"/><stop offset="1" stop-color="#2E9E5B"/></linearGradient></defs><rect width="1920" height="1080" fill="url(#sg)"/><path d="M0 960 C 400 860, 780 1060, 1200 960 S 1720 830, 1920 890" fill="none" stroke="url(#s1)" stroke-width="5"/><path d="M0 1000 C 430 900, 800 1080, 1220 990 S 1730 870, 1920 930" fill="none" stroke="url(#s2)" stroke-width="3" opacity="0.9"/></svg>'


def num(n):
    return f"{n:02d}".translate(BN)


def footer(n, dark=False):
    out = ""
    if not dark:
        out += '<p style="position:absolute;left:128px;bottom:64px;width:900px;font-size:24px;font-weight:600;color:#4A6358">Al-Insaf Life Care · ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি</p>\n'
    color = "#9DB8AA" if dark else "#1F7A42"
    out += f'<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:{color};text-align:right">{num(n)} / {num(TOTAL)}</p>\n'
    return out


def header(eyebrow, a, b):
    return (
        '<div style="display:flex;flex-direction:column;gap:14px">\n'
        f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;color:#B85A0C">{eyebrow}</p>\n'
        f'<h2 style="{HEAD};font-size:72px;font-weight:800;line-height:1.15;color:#12352A">{a} <span style="color:#1F8A4C">{b}</span></h2>\n'
        "</div>\n"
    )


def light(sid, bg, body, n, notes, justify="space-between"):
    return (
        f'<section id="{sid}" data-transition="fade" style="background:{bg};color:#12352A;{FONT};padding:112px 128px 160px;display:flex;flex-direction:column;justify-content:{justify}">\n'
        f"{STRIP}\n{body}{footer(n)}<aside>{notes}</aside>\n</section>\n"
    )


def note_pill(text, dark=False):
    if dark:
        return f'<p style="font-size:32px;line-height:1.5;text-align:center;color:#FFFFFF;background:#1F7A42;border-radius:999px;padding:20px 48px">{text}</p>\n'
    return f'<p style="font-size:32px;line-height:1.5;text-align:center;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:999px;padding:20px 48px">{text}</p>\n'


def cards(items, icons=True, arrows=False):
    """items: (icon-or-number, bangla, english). Last card is highlighted."""
    parts = []
    for i, (mark, bn, en) in enumerate(items):
        last = i == len(items) - 1
        box = "background:#FFF1E0;border:2px solid #F28C28" if last else "background:#FFFFFF;border:1px solid #DCE6D6"
        if icons:
            circ = "#F28C28" if last else "#2E9E5B"
            ic = "#3A1E05" if last else "#FFFFFF"
            top = f'<div style="background:{circ};border-radius:999px;padding:24px;display:flex"><x-icon name="{mark}" style="color:{ic};width:56px;height:56px"></x-icon></div>'
        else:
            col = "#B85A0C" if last else "#1F8A4C"
            top = f'<p style="{HEAD};font-size:72px;font-weight:800;line-height:1;color:{col}">{mark}</p>'
        sub = "#5A3510" if last else "#4A6358"
        parts.append(
            f'<div style="flex:1;{box};border-radius:24px;padding:36px 20px;display:flex;flex-direction:column;gap:16px;align-items:center">{top}'
            f'<h3 style="font-size:32px;font-weight:700;text-align:center">{bn}</h3><p style="font-size:26px;text-align:center;color:{sub}">{en}</p></div>'
        )
        if arrows and not last:
            parts.append('<x-shape kind="arrow-right" style="background:#F28C28;width:44px;height:22px"></x-shape>')
    return '<div style="display:flex;flex-direction:row;gap:20px;align-items:center">\n' + "\n".join(parts) + "\n</div>\n"


def statement(sid, label, big, sub, text, n, notes, dark=True):
    bgsvg, bg, txt, lab = (DARK_BG, "#12352A", "#FFFFFF", "#F6B26B") if dark else (SOFT_BG, "#F6F7F0", "#12352A", "#B85A0C")
    subc = "#A6D65A" if dark else "#1F8A4C"
    bodyc = "#D7E8DD" if dark else "#4A6358"
    sub_html = f'<p style="{HEAD};font-size:56px;font-weight:700;line-height:1.2;text-align:center;color:{subc}">{sub}</p>\n' if sub else ""
    return (
        f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{txt};{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:36px">\n'
        f"{bgsvg}\n"
        f'<p style="font-size:34px;font-weight:600;letter-spacing:2px;color:{lab}">{label}</p>\n'
        f'<h2 style="{HEAD};font-size:100px;font-weight:800;line-height:1.15;text-align:center;color:{txt}">{big}</h2>\n'
        f"{sub_html}"
        '<hr style="border-top:3px solid #F28C28;width:160px">\n'
        f'<p style="font-size:38px;line-height:1.45;text-align:center;color:{bodyc};width:1400px">{text}</p>\n'
        f"{footer(n, dark=True) if dark else footer(n).split(chr(10), 1)[1]}<aside>{notes}</aside>\n</section>\n"
    )


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
<p style="{HEAD};font-size:28px;font-weight:800;color:#3A1E05;background:#F28C28;padding:6px 22px;border-radius:999px;letter-spacing:2px">DAY 05</p>
<p style="font-size:28px;font-weight:600;color:#4A6358;letter-spacing:1px">Healthy Weight &amp; Smart Body Halua</p>
</div>
<h1 style="{HEAD};font-size:96px;font-weight:800;line-height:1.1;color:#12352A">হেংলা-পাতলা শরীর ও<br><span style="color:#1F8A4C">Smart Body Halua</span></h1>
<p style="font-size:32px;line-height:1.45;color:#4A6358">আজ এমন একটি বিষয় নিয়ে কথা বলবো যা অনেক তরুণ, যুবক এমনকি বিবাহিত মানুষেরও সাধারণ সমস্যা।</p>
</div>
<div style="display:flex;flex-direction:row;gap:18px;align-items:center;background:#FFFFFF;border:1px solid #CFE0C6;border-radius:999px;padding:14px 32px;width:1120px;box-shadow:0 6px 20px rgba(18,53,42,0.08)">
<x-icon name="Chat" style="color:#2E9E5B;width:36px;height:36px"></x-icon>
<p style="font-size:28px;color:#12352A"><b style="color:#1F7A42">আল ইনসাফ লাইফ কেয়ার</b> · ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি · +880 1332-140494</p>
</div>
<div style="position:absolute;left:1370px;top:260px;width:420px;height:420px;border-radius:50%;border:6px solid #2E9E5B;background:#FFFFFF;box-shadow:0 20px 60px rgba(18,53,42,0.12);display:flex;flex-direction:column;align-items:center;justify-content:center">
<p style="{HEAD};font-size:56px;font-weight:800;letter-spacing:6px;color:#12352A">DAY</p>
<p style="{HEAD};font-size:200px;font-weight:800;line-height:1;color:#1F8A4C">০৫</p>
<p style="font-size:26px;font-weight:600;color:#B85A0C">Smart Body Halua</p>
</div>
<aside>আজ এমন একটি বিষয় নিয়ে কথা বলবো যা অনেক তরুণ, যুবক এমনকি বিবাহিত মানুষেরও সাধারণ সমস্যা।</aside>
</section>
"""

slides["goal"] = statement("goal", "আমাদের লক্ষ্য · OUR GOAL", "লক্ষ্য মোটা হওয়া নয়", "লক্ষ্য সুস্থ ও স্মার্ট হওয়া",
                           "আমাদের লক্ষ্য অস্বাভাবিকভাবে মোটা হওয়া নয়, একটি সুস্থ, শক্তিশালী ও স্মার্ট শরীর গঠন করা।", 2,
                           "লক্ষ্য মোটা হওয়া নয়, লক্ষ্য সুস্থ ও স্মার্ট হওয়া। আমাদের লক্ষ্য অস্বাভাবিকভাবে মোটা হওয়া নয়, একটি সুস্থ, শক্তিশালী ও স্মার্ট শরীর গঠন করা।")

slides["causes"] = light("causes", "#F6F7F0",
    header("CAUSES · কারণ", "ওজন কম", "কেন হয়?")
    + cards([("Activity", "অপুষ্টি", "Malnutrition"), ("Clock", "কম খাওয়া", "Low intake"), ("Warning", "হজম সমস্যা", "Poor digestion"),
             ("Lightning", "অতিরিক্ত মানসিক চাপ", "Stress"), ("Settings", "অনিয়মিত জীবনযাপন", "Irregular routine")])
    + note_pill("অনেক মানুষ বেশি খাওয়ার পরও ওজন বাড়াতে পারে না, এর পেছনে নানা কারণ থাকতে পারে।"),
    3, "ওজন কম হওয়ার ৫টি কারণ: অপুষ্টি, কম খাওয়া, হজম সমস্যা, অতিরিক্ত মানসিক চাপ, অনিয়মিত জীবনযাপন। অনেক মানুষ বেশি খাওয়ার পরও ওজন বাড়াতে পারে না, এর পেছনে নানা কারণ থাকতে পারে।")

slides["effects"] = light("effects", "#EEF5EA",
    header("EFFECTS · প্রভাব", "হেংলা-পাতলা শরীরের", "প্রভাব")
    + cards([("১", "দুর্বলতা", "Weakness"), ("২", "আত্মবিশ্বাস কমে যাওয়া", "Low confidence"), ("৩", "দ্রুত ক্লান্ত হয়ে যাওয়া", "Quick fatigue"),
             ("৪", "কর্মক্ষমতা কমে যাওয়া", "Reduced performance")], icons=False)
    + note_pill("অনেকেই শারীরিক দুর্বলতার কারণে নিজের পূর্ণ সম্ভাবনা কাজে লাগাতে পারেন না।", dark=True),
    4, "হেংলা-পাতলা শরীরের প্রভাব: দুর্বলতা, আত্মবিশ্বাস কমে যাওয়া, দ্রুত ক্লান্ত হয়ে যাওয়া, কর্মক্ষমতা কমে যাওয়া। অনেকেই শারীরিক দুর্বলতার কারণে নিজের পূর্ণ সম্ভাবনা কাজে লাগাতে পারেন না।")

slides["question"] = statement("question", "একটি গুরুত্বপূর্ণ প্রশ্ন · KEY QUESTION", "শরীর কি পর্যাপ্ত পুষ্টি পাচ্ছে?", "",
                               "শুধু বেশি খাওয়াই সমাধান নয়, শরীর সঠিক পুষ্টি পাচ্ছে কিনা সেটাও সমান গুরুত্বপূর্ণ।", 5,
                               "শরীর কি পর্যাপ্ত পুষ্টি পাচ্ছে? শুধু বেশি খাওয়াই সমাধান নয়, শরীর সঠিক পুষ্টি পাচ্ছে কিনা সেটাও সমান গুরুত্বপূর্ণ।")

slides["product"] = f"""<section id="product" data-transition="fade" style="background:#F6F7F0;color:#12352A;{FONT};padding:112px 128px 160px;display:grid;grid-template-columns:640px 984px;gap:40px;align-items:center">
{STRIP}
<div style="width:640px;height:700px;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:32px;box-shadow:0 16px 48px rgba(18,53,42,0.14);display:flex;align-items:center;justify-content:center">
<img src="{PRODUCT}" alt="Smart Body Halua পণ্যের ছবি" style="width:600px;height:600px;object-fit:contain;border-radius:20px">
</div>
<div style="display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:14px">
<p style="font-size:24px;font-weight:700;letter-spacing:2px;color:#B85A0C">PRODUCT · প্রোডাক্ট পরিচিতি</p>
<h2 style="{HEAD};font-size:96px;font-weight:800;line-height:1.05;color:#1F8A4C">Smart Body Halua</h2>
<p style="font-size:38px;font-weight:700;color:#12352A">পুষ্টি সহায়ক প্রাকৃতিক খাবার</p>
</div>
<p style="font-size:32px;line-height:1.5;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px">Smart Body Halua এমনভাবে তৈরি করা হয়েছে, যাতে শরীরের পুষ্টির ঘাটতি পূরণে সহায়ক ভূমিকা রাখতে পারে।</p>
</div>
{footer(6)}<aside>Smart Body Halua: পুষ্টি সহায়ক প্রাকৃতিক খাবার। Smart Body Halua এমনভাবে তৈরি করা হয়েছে, যাতে শরীরের পুষ্টির ঘাটতি পূরণে সহায়ক ভূমিকা রাখতে পারে।</aside>
</section>
"""

slides["want"] = light("want", "#EEF5EA",
    header("WHAT PEOPLE WANT", "মানুষ আসলে", "কী চায়?")
    + cards([("Activity", "Healthy Body", "সুস্থ শরীর"), ("Star", "Smart Look", "স্মার্ট গঠন"), ("Lightning", "Good Energy", "ভালো শক্তি")])
    + note_pill("মানুষ শুধু ওজন বাড়াতে চায় না, চায় সুস্থ ও আকর্ষণীয় শারীরিক গঠন।"),
    7, "মানুষ আসলে কী চায়: সুস্থ শরীর, স্মার্ট গঠন, ভালো শক্তি। মানুষ শুধু ওজন বাড়াতে চায় না, চায় সুস্থ ও আকর্ষণীয় শারীরিক গঠন।")

slides["making"] = light("making", "#F6F7F0",
    header("PRODUCT MAKING · তৈরির ধারণা", "Smart Body Halua", "তৈরির ধারণা")
    + cards([("01", "মানসম্মত উপাদান", "Quality Ingredients"), ("02", "প্রাকৃতিক উপাদানের সমন্বয়", "Natural Blend"),
             ("03", "স্বাস্থ্যসম্মত প্রস্তুতি", "Hygienic Preparation"), ("04", "সঠিক প্যাকেজিং", "Proper Packaging")], icons=False, arrows=True)
    + note_pill("একটি ভালো প্রোডাক্টের পেছনে সঠিক উপাদান ও সঠিক প্রস্তুত প্রক্রিয়া কাজ করে।", dark=True),
    8, "Smart Body Halua তৈরির ধারণা: মানসম্মত উপাদান, প্রাকৃতিক উপাদানের সমন্বয়, স্বাস্থ্যসম্মত প্রস্তুতি, সঠিক প্যাকেজিং। একটি ভালো প্রোডাক্টের পেছনে সঠিক উপাদান ও সঠিক প্রস্তুত প্রক্রিয়া কাজ করে।")

slides["market"] = light("market", "#EEF5EA",
    header("A REAL MARKET · একটি বাস্তব বাজার", "অনেক মানুষ এই সমস্যায়", "ভুগছেন")
    + cards([("GraduationCap", "ছাত্র", "Students"), ("Users", "যুবক", "Youth"), ("Tool", "চাকরিজীবী", "Job holders"), ("Home", "বিবাহিত ব্যক্তি", "Married")])
    + note_pill("ওজন কম হওয়া ও শারীরিক দুর্বলতা একটি খুবই সাধারণ সমস্যা।"),
    9, "অনেক মানুষ এই সমস্যায় ভুগছেন: ছাত্র, যুবক, চাকরিজীবী, বিবাহিত ব্যক্তি। ওজন কম হওয়া ও শারীরিক দুর্বলতা একটি খুবই সাধারণ সমস্যা।")

slides["opportunity"] = light("opportunity", "#F6F7F0",
    header("BUSINESS OPPORTUNITY · ব্যবসার সুযোগ", "Problem → Solution →", "Income")
    + cards([("Warning", "সমস্যা", "Problem"), ("Lightbulb", "সমাধান", "Solution"), ("Chart", "আয়", "Income")], arrows=True)
    + note_pill("যখন একটি সমস্যার কার্যকর সমাধান মানুষের কাছে পৌঁছে দেওয়া যায়, তখন সেখান থেকেই ব্যবসার সুযোগ তৈরি হয়।", dark=True),
    10, "সমস্যা থেকে সমাধান, সমাধান থেকে আয়। যখন একটি সমস্যার কার্যকর সমাধান মানুষের কাছে পৌঁছে দেওয়া যায়, তখন সেখান থেকেই ব্যবসার সুযোগ তৈরি হয়।")

slides["vision"] = statement("vision", "একজন উদ্যোক্তার দৃষ্টি · ENTREPRENEUR VISION", "মানুষের কষ্ট বুঝুন,", "সমাধান পৌঁছে দিন",
                             "সফল উদ্যোক্তা মানুষের প্রয়োজনকে বুঝে কাজ করেন।", 11,
                             "মানুষের কষ্ট বুঝুন, সমাধান পৌঁছে দিন। সফল উদ্যোক্তা মানুষের প্রয়োজনকে বুঝে কাজ করেন।")

slides["task"] = light("task", "#EEF5EA",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Search" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">আপনার পরিচিত কতজন মানুষ ওজন কম বা শারীরিক দুর্বলতার সমস্যায় ভুগছেন?</p>\n</div>\n'
    + '<p style="font-size:34px;line-height:1.5;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px">আজ আশেপাশের মানুষের মধ্যে এই সমস্যাটি কতটা রয়েছে, সেটি পর্যবেক্ষণ করুন।</p>\n<div></div>\n',
    12, "আপনার পরিচিত কতজন মানুষ ওজন কম বা শারীরিক দুর্বলতার সমস্যায় ভুগছেন? আজ আশেপাশের মানুষের মধ্যে এই সমস্যাটি কতটা রয়েছে, সেটি পর্যবেক্ষণ করুন।")

slides["next"] = f"""<section id="next" data-transition="fade" style="background:#F6F7F0;color:#12352A;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:36px">
{SOFT_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:84px;font-weight:800;line-height:1.15;text-align:center;color:#12352A">আরও একটি গুরুত্বপূর্ণ<br><span style="color:#1F8A4C">স্বাস্থ্য সমস্যা ও সমাধান</span></h2>
<p style="font-size:34px;line-height:1.5;text-align:center;color:#4A6358;width:1300px">আগামীকালের ক্লাসে আরও একটি বাস্তব স্বাস্থ্য সমস্যা নিয়ে আলোচনা করবো, দেখবো কীভাবে সেই সমাধান মানুষের জীবনে পরিবর্তন আনে।</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:#1F7A42;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:32px;font-weight:700;color:#FFFFFF">আল ইনসাফ লাইফ কেয়ার · +880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#1F7A42;text-align:right">{num(13)} / {num(TOTAL)}</p>
<aside>আগামীকালের ক্লাসে আরও একটি বাস্তব স্বাস্থ্য সমস্যা নিয়ে আলোচনা করবো, দেখবো কীভাবে সেই সমাধান মানুষের জীবনে পরিবর্তন আনে।</aside>
</section>
"""

order = ["cover", "goal", "causes", "effects", "question", "product", "want", "making", "market", "opportunity", "vision", "task", "next"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-01T09:20:00Z"},
    "lists": "css",
    "title": "পঞ্চম দিন — হেংলা-পাতলা শরীর ও Smart Body Halua",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "ওজন কম হওয়ার কারণ ও প্রভাব", "start": "cover"},
        "s2": {"description": "Smart Body Halua পরিচিতি ও তৈরির ধারণা", "start": "question"},
        "s3": {"description": "বাজার, ব্যবসার সুযোগ ও আজকের কাজ", "start": "market"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
