"""Write the Day 6 (Lion Man & Sultani Halua) slide files, same look as Day 5."""

import json
from pathlib import Path

# Reuse the Day 5 helpers (header, cards, statement, footer, backgrounds).
_day5 = (Path(__file__).parent.parent / "day5" / "make_slides.py").read_text(encoding="utf-8")
exec(_day5.split("slides = {}")[0])

ROOT = Path(__file__).parent / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 14
LION = "/_blob/687ea13a257fbd0e1ce3ac9aebdd6ef5"
SULTANI = "/_blob/505f4bfc61795fc64b88b29b4208e75b"
LOGO_ALINSAF = "/_blob/7ed2fc99755827fae1f399ea51c5e347"
LOGO_INSAFIX = "/_blob/f59864f5602a23851e6c15e9adb50e47"


def product(sid, img, name, tag, desc, n, notes):
    return f"""<section id="{sid}" data-transition="fade" style="background:#F6F7F0;color:#12352A;{FONT};padding:112px 128px 160px;display:grid;grid-template-columns:640px 984px;gap:40px;align-items:center">
{STRIP}
<div style="width:640px;height:700px;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:32px;box-shadow:0 16px 48px rgba(18,53,42,0.14);display:flex;align-items:center;justify-content:center">
<img src="{img}" alt="{name} পণ্যের ছবি" style="width:600px;height:600px;object-fit:contain;border-radius:20px">
</div>
<div style="display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:14px">
<p style="font-size:24px;font-weight:700;letter-spacing:2px;color:#B85A0C">PRODUCT · প্রোডাক্ট পরিচিতি</p>
<h2 style="{HEAD};font-size:96px;font-weight:800;line-height:1.05;color:#1F8A4C">{name}</h2>
<p style="font-size:38px;font-weight:700;color:#12352A">{tag}</p>
</div>
<p style="font-size:32px;line-height:1.5;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px">{desc}</p>
</div>
{footer(n)}<aside>{notes}</aside>
</section>
"""


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
<p style="{HEAD};font-size:28px;font-weight:800;color:#3A1E05;background:#F28C28;padding:6px 22px;border-radius:999px;letter-spacing:2px">DAY 06</p>
<p style="font-size:28px;font-weight:600;color:#4A6358;letter-spacing:1px">Marital Wellness &amp; Physical Vitality</p>
</div>
<h1 style="{HEAD};font-size:88px;font-weight:800;line-height:1.12;color:#12352A">বৈবাহিক জীবন, শারীরিক সক্ষমতা<br><span style="color:#1F8A4C">ও আত্মবিশ্বাস</span></h1>
<p style="font-size:32px;line-height:1.45;color:#4A6358">আজ এমন একটি বিষয় নিয়ে কথা বলবো, যা অনেকে জানে ও অনুভব করে, কিন্তু খোলাখুলি আলোচনা করতে সংকোচ বোধ করে।</p>
</div>
<div style="display:flex;flex-direction:row;gap:18px;align-items:center;background:#FFFFFF;border:1px solid #CFE0C6;border-radius:999px;padding:14px 32px;width:1120px;box-shadow:0 6px 20px rgba(18,53,42,0.08)">
<x-icon name="Chat" style="color:#2E9E5B;width:36px;height:36px"></x-icon>
<p style="font-size:28px;color:#12352A"><b style="color:#1F7A42">আল ইনসাফ লাইফ কেয়ার</b> · ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি · +880 1332-140494</p>
</div>
<div style="position:absolute;left:1370px;top:260px;width:420px;height:420px;border-radius:50%;border:6px solid #2E9E5B;background:#FFFFFF;box-shadow:0 20px 60px rgba(18,53,42,0.12);display:flex;flex-direction:column;align-items:center;justify-content:center">
<p style="{HEAD};font-size:56px;font-weight:800;letter-spacing:6px;color:#12352A">DAY</p>
<p style="{HEAD};font-size:200px;font-weight:800;line-height:1;color:#1F8A4C">০৬</p>
<p style="font-size:26px;font-weight:600;color:#B85A0C">Lion Man · Sultani Halua</p>
</div>
<aside>আজ এমন একটি বিষয় নিয়ে কথা বলবো, যা অনেকে জানে ও অনুভব করে, কিন্তু খোলাখুলি আলোচনা করতে সংকোচ বোধ করে।</aside>
</section>
"""

slides["foundation"] = light("foundation", "#EEF5EA",
    header("FOUNDATION · সুখী জীবনের ভিত্তি", "একটি সুখী জীবনের", "গুরুত্বপূর্ণ অংশ")
    + cards([("Activity", "সুস্থ শরীর", "Healthy Body"), ("Lightbulb", "সুস্থ মন", "Healthy Mind"), ("Home", "সুস্থ পারিবারিক জীবন", "Healthy Family")])
    + note_pill("ব্যক্তিগত, পারিবারিক ও সামাজিক জীবনের সাথে শারীরিক সুস্থতার গভীর সম্পর্ক রয়েছে।", dark=True),
    2, "সুস্থ শরীর, সুস্থ মন, সুস্থ পারিবারিক জীবন। ব্যক্তিগত, পারিবারিক ও সামাজিক জীবনের সাথে শারীরিক সুস্থতার গভীর সম্পর্ক রয়েছে।")

slides["causes"] = light("causes", "#F6F7F0",
    header("CAUSES · কারণ", "কেন অনেক মানুষ", "দুর্বল বোধ করে?")
    + cards([("Lightning", "মানসিক চাপ", "Stress"), ("Activity", "অপুষ্টি", "Malnutrition"), ("Settings", "অনিয়মিত জীবনযাপন", "Irregular life"),
             ("Clock", "বিশ্রামের অভাব", "Lack of rest"), ("Warning", "শারীরিক দুর্বলতা", "Physical weakness")])
    + note_pill("অনেক সময় মানুষ নিজেকে দুর্বল অনুভব করে, কিন্তু এর পেছনের কারণ খুঁজে দেখে না।"),
    3, "কেন অনেক মানুষ দুর্বল বোধ করে: মানসিক চাপ, অপুষ্টি, অনিয়মিত জীবনযাপন, বিশ্রামের অভাব, শারীরিক দুর্বলতা। অনেক সময় মানুষ নিজেকে দুর্বল অনুভব করে, কিন্তু এর পেছনের কারণ খুঁজে দেখে না।")

slides["confidence"] = statement("confidence", "আত্মবিশ্বাসের গুরুত্ব · CONFIDENCE", "Confidence (আত্মবিশ্বাস)", "জীবনের প্রতিটি ক্ষেত্রে গুরুত্বপূর্ণ",
                                 "যখন একজন মানুষ শারীরিকভাবে সুস্থ থাকে, তখন তার আত্মবিশ্বাসও বৃদ্ধি পায়।", 4,
                                 "আত্মবিশ্বাস জীবনের প্রতিটি ক্ষেত্রে গুরুত্বপূর্ণ। যখন একজন মানুষ শারীরিকভাবে সুস্থ থাকে, তখন তার আত্মবিশ্বাসও বৃদ্ধি পায়।")

slides["lifestyle"] = light("lifestyle", "#EEF5EA",
    header("HEALTHY LIFESTYLE · সুস্থ জীবনযাপন", "সুস্থ জীবনযাপনের", "ভিত্তি")
    + cards([("Home", "পুষ্টিকর খাবার", "Nutritious food"), ("Clock", "পর্যাপ্ত ঘুম", "Enough sleep"), ("Activity", "নিয়মিত ব্যায়াম", "Regular exercise"),
             ("Star", "মানসিক প্রশান্তি", "Peace of mind")])
    + note_pill("দীর্ঘমেয়াদী সুস্থতার জন্য সঠিক জীবনযাপন অত্যন্ত গুরুত্বপূর্ণ।"),
    5, "সুস্থ জীবনযাপনের ভিত্তি: পুষ্টিকর খাবার, পর্যাপ্ত ঘুম, নিয়মিত ব্যায়াম, মানসিক প্রশান্তি। দীর্ঘমেয়াদী সুস্থতার জন্য সঠিক জীবনযাপন অত্যন্ত গুরুত্বপূর্ণ।")

slides["lionman"] = product("lionman", LION, "Lion Man", "প্রাকৃতিক পুষ্টি সহায়ক",
    "Lion Man একটি প্রাকৃতিক উপাদান ভিত্তিক পুষ্টি সহায়ক প্রোডাক্ট, যা শারীরিক শক্তি ও প্রাণশক্তি বৃদ্ধির উদ্দেশ্যে তৈরি করা হয়েছে।", 6,
    "Lion Man একটি প্রাকৃতিক উপাদান ভিত্তিক পুষ্টি সহায়ক প্রোডাক্ট, যা শারীরিক শক্তি ও প্রাণশক্তি বৃদ্ধির উদ্দেশ্যে তৈরি করা হয়েছে।")

slides["sultani"] = product("sultani", SULTANI, "Sultani Halua", "পুষ্টিকর প্রাকৃতিক খাদ্য",
    "Sultani Halua পুষ্টিকর প্রাকৃতিক উপাদানের সমন্বয়ে প্রস্তুত একটি বিশেষ খাদ্য।", 7,
    "Sultani Halua পুষ্টিকর প্রাকৃতিক উপাদানের সমন্বয়ে প্রস্তুত একটি বিশেষ খাদ্য।")

slides["want"] = light("want", "#EEF5EA",
    header("WHAT PEOPLE WANT", "মানুষ", "কী চায়?")
    + cards([("Lightning", "শক্তি", "Strength"), ("Tool", "কর্মক্ষমতা", "Performance"), ("Star", "আত্মবিশ্বাস", "Confidence"), ("Activity", "সুস্থ জীবন", "Healthy life")])
    + note_pill("প্রতিটি মানুষ চায় নিজেকে সুস্থ, কর্মক্ষম ও আত্মবিশ্বাসী রাখতে।"),
    8, "মানুষ কী চায়: শক্তি, কর্মক্ষমতা, আত্মবিশ্বাস, সুস্থ জীবন। প্রতিটি মানুষ চায় নিজেকে সুস্থ, কর্মক্ষম ও আত্মবিশ্বাসী রাখতে।")

slides["making"] = light("making", "#F6F7F0",
    header("PRODUCT MAKING · তৈরির ধারণা", "প্রোডাক্ট", "তৈরির ধারণা")
    + cards([("01", "উপাদান নির্বাচন", "Ingredient Selection"), ("02", "মান নিয়ন্ত্রণ", "Quality Control"),
             ("03", "স্বাস্থ্যসম্মত প্রস্তুতি", "Hygienic Preparation"), ("04", "প্যাকেজিং", "Packaging")], icons=False, arrows=True)
    + note_pill("একটি ভালো প্রাকৃতিক পণ্যের পেছনে সঠিক উপাদান ও সঠিক প্রস্তুত প্রক্রিয়া গুরুত্বপূর্ণ।", dark=True),
    9, "প্রোডাক্ট তৈরির ধারণা: উপাদান নির্বাচন, মান নিয়ন্ত্রণ, স্বাস্থ্যসম্মত প্রস্তুতি, প্যাকেজিং। একটি ভালো প্রাকৃতিক পণ্যের পেছনে সঠিক উপাদান ও সঠিক প্রস্তুত প্রক্রিয়া গুরুত্বপূর্ণ।")

slides["opportunity"] = light("opportunity", "#EEF5EA",
    header("HEALTH BUSINESS OPPORTUNITY", "Need → Solution →", "Business")
    + cards([("Search", "প্রয়োজন", "Need"), ("Lightbulb", "সমাধান", "Solution"), ("Chart", "ব্যবসা", "Business")], arrows=True)
    + note_pill("মানুষের প্রয়োজন যত বেশি, সেই সমস্যার সমাধান নিয়ে কাজ করার সুযোগও তত বেশি।", dark=True),
    10, "প্রয়োজন থেকে সমাধান, সমাধান থেকে ব্যবসা। মানুষের প্রয়োজন যত বেশি, সেই সমস্যার সমাধান নিয়ে কাজ করার সুযোগও তত বেশি।")

slides["vision"] = statement("vision", "একজন উদ্যোক্তার দৃষ্টি · ENTREPRENEUR VISION", "মানুষের প্রয়োজন বুঝুন,", "বিশ্বাস অর্জন করুন",
                             "স্বাস্থ্য সেক্টরে দীর্ঘমেয়াদী সফলতার মূল ভিত্তি হলো বিশ্বাস।", 11,
                             "মানুষের প্রয়োজন বুঝুন, বিশ্বাস অর্জন করুন। স্বাস্থ্য সেক্টরে দীর্ঘমেয়াদী সফলতার মূল ভিত্তি হলো বিশ্বাস।")

slides["task"] = light("task", "#EEF5EA",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Search" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">মানুষ শারীরিক দুর্বলতা দূর করতে কী কী উপায় অনুসরণ করে?</p>\n</div>\n'
    + '<p style="font-size:34px;line-height:1.5;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px">আজ আপনার আশেপাশের মানুষের অভিজ্ঞতা জানার চেষ্টা করুন।</p>\n<div></div>\n',
    12, "মানুষ শারীরিক দুর্বলতা দূর করতে কী কী উপায় অনুসরণ করে? আজ আপনার আশেপাশের মানুষের অভিজ্ঞতা জানার চেষ্টা করুন।")

slides["next"] = f"""<section id="next" data-transition="fade" style="background:#F6F7F0;color:#12352A;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:36px">
{SOFT_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:100px;font-weight:800;line-height:1.15;text-align:center;color:#12352A">বিশেষ সেশন<br><span style="color:#1F8A4C">Special Session</span></h2>
<p style="font-size:34px;line-height:1.5;text-align:center;color:#4A6358;width:1300px">আগামীকাল পুরো যাত্রার একটি গুরুত্বপূর্ণ সংযোগ নিয়ে আলোচনা করবো, যা পরবর্তী ধাপের জন্য আপনাকে প্রস্তুত করবে।</p>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#1F7A42;text-align:right">{num(13)} / {num(TOTAL)}</p>
<aside>আগামীকাল পুরো যাত্রার একটি গুরুত্বপূর্ণ সংযোগ নিয়ে আলোচনা করবো, যা পরবর্তী ধাপের জন্য আপনাকে প্রস্তুত করবে।</aside>
</section>
"""

slides["thanks"] = f"""<section id="thanks" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<h2 style="{HEAD};font-size:120px;font-weight:800;line-height:1;color:#FFFFFF">Thank You</h2>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:48px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<p style="font-size:36px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">আজকের ক্লাস এখানেই শেষ, আগামীকালের বিশেষ সেশন মিস করবেন না।</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(14)} / {num(TOTAL)}</p>
<aside>আজকের ক্লাস এখানেই শেষ, আগামীকালের বিশেষ সেশন মিস করবেন না। যোগাযোগ: +880 1332-140494।</aside>
</section>
"""

order = ["cover", "foundation", "causes", "confidence", "lifestyle", "lionman", "sultani", "want", "making", "opportunity", "vision", "task", "next", "thanks"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-01T17:10:00Z"},
    "lists": "css",
    "title": "ষষ্ঠ দিন — বৈবাহিক জীবন, শারীরিক সক্ষমতা ও আত্মবিশ্বাস",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "সুখী জীবনের ভিত্তি, দুর্বলতার কারণ ও আত্মবিশ্বাস", "start": "cover"},
        "s2": {"description": "Lion Man ও Sultani Halua পরিচিতি", "start": "lionman"},
        "s3": {"description": "ব্যবসার সুযোগ, আজকের কাজ ও পরের ক্লাস", "start": "opportunity"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
