"""Write the Day 12 (Costo Clear) slide files from the old Day 7 deck, same look as Days 1–11.

Content is the old deck's, slide for slide; only the look changes. ভেষজ/Herbal → প্রাকৃতিক.
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
_day9 = (HERE.parent / "day9" / "make_slides.py").read_text(encoding="utf-8")
exec(_day9.split("\nslides = {}")[0])

ROOT = HERE / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 13
LOGO_A = "/_blob/1aa6a8f7c8771c4f5869dddffe7e20fb"
LOGO_I = "/_blob/06d24423ebdd0f7d12ab7d0481e1f283"
PRODUCT = "/_blob/1472fb6254df114ba4b5a6fe4b7d6d87"

slides = {}

cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
for a, b in [
    (LOGO_ALINSAF, LOGO_A),
    (LOGO_INSAFIX, LOGO_I),
    (f'<img src="{U_SET}" alt="হিজামার কাপ ও পাম্প" style="position:absolute;left:1292px;top:190px;width:500px;height:334px;object-fit:cover;',
     f'<img src="{PRODUCT}" alt="Costo Clear (কোষ্ঠক্লিয়ার পাউডার) প্রোডাক্টের ছবি" style="position:absolute;left:1420px;top:90px;width:372px;height:500px;background:#FFFFFF;object-fit:contain;'),
    ('left:1220px;top:440px;width:200px;height:200px;border-radius:50%', 'left:1300px;top:480px;width:200px;height:200px;border-radius:50%'),
    (">DAY 08<", ">DAY 12<"),
    ("হিজামা · প্রথম ক্লাস", "Constipation Problem &amp; Costo Clear"),
    ('<h1 style="{HEAD};font-size:100px;'.replace("{HEAD}", HEAD), f'<h1 style="{HEAD};font-size:88px;'),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'কোষ্ঠকাঠিন্য সমস্যা ও<br><span style="color:#1F8A4C">Costo Clear</span>'),
    (">০৮<", ">১২<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">সমস্যা<br><span style="color:#1F7A42">ও কারণ</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Verified" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">প্রোডাক্ট<br><span style="color:#1F7A42">পরিচিতি</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="Chart" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">আয়ের<br><span style="color:#1F7A42">পথ</span>'),
    ('<b style="color:#B85A0C">খাতা-কলম নিন:</b> আজকের প্রতিটি বিষয় নোট করে রাখুন',
     'আজ এমন একটি সমস্যা নিয়ে কথা বলবো যাকে অনেকে ছোট ভাবেন, অথচ এটি বড় রোগের সূচনা হতে পারে।'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>আজ এমন একটি সমস্যা নিয়ে কথা বলবো যাকে অনেকে ছোট ভাবেন, অথচ এটি বড় রোগের সূচনা হতে পারে: কোষ্ঠকাঠিন্য সমস্যা ও Costo Clear।" + cover[b:]
slides["cover"] = cover


slides["what"] = light("what", "#EEF5EA",
    header("সংজ্ঞা · WHAT IS IT", "কোষ্ঠকাঠিন্য", "(Constipation) কী?")
    + cards([("১", "নিয়মিত পায়খানা না হওয়া", "Irregular"), ("২", "শক্ত মল হওয়া", "Hard stool"),
             ("৩", "পায়খানার সময় কষ্ট হওয়া", "Straining")], icons=False)
    + note_pill("<b>সহজ কথায়:</b> শরীরের বর্জ্য স্বাভাবিকভাবে বের হতে না পারলে তাকে কোষ্ঠকাঠিন্য বলা হয়।"),
    2, "কোষ্ঠকাঠিন্য মানে নিয়মিত পায়খানা না হওয়া, শক্ত মল হওয়া, পায়খানার সময় কষ্ট হওয়া। সহজ কথায়, শরীরের বর্জ্য স্বাভাবিকভাবে বের হতে না পারলে তাকে কোষ্ঠকাঠিন্য বলা হয়।")

slides["causes"] = light("causes", "#F6F7F0",
    header("কারণ · CAUSES", "কোষ্ঠকাঠিন্যের", "কারণ")
    + cards([("Activity", "কম পানি পান", "Low water"), ("Star", "আঁশযুক্ত খাবার কম", "Low fiber"), ("Clock", "অনিয়মিত জীবনযাপন", "Irregular routine"),
             ("Users", "পরিশ্রমের অভাব", "No exercise"), ("Warning", "দীর্ঘদিন ওষুধ সেবন", "Long medication")])
    + note_pill("বর্তমান জীবনযাত্রার কারণে এই সমস্যা দিন দিন বৃদ্ধি পাচ্ছে।"),
    3, "পাঁচটি কারণ: কম পানি পান, আঁশযুক্ত খাবার কম, অনিয়মিত জীবনযাপন, পরিশ্রমের অভাব আর দীর্ঘদিন ওষুধ সেবন।")

comp = "".join(
    '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-left:8px solid #F28C28;border-radius:22px;padding:30px 32px;display:flex;flex-direction:row;gap:18px;align-items:center">'
    f'<x-icon name="Warning" style="color:#B85A0C;width:40px;height:40px"></x-icon><h3 style="font-size:38px;font-weight:700;color:#12352A">{t}</h3></div>\n'
    for t in ["গ্যাস", "বদহজম", "অর্শ (Piles)", "পেট ফাঁপা", "অস্বস্তি", "ক্ষুধামন্দা"]
)
slides["complications"] = light("complications", "#EEF5EA",
    header("জটিলতা · COMPLICATIONS", "কোষ্ঠকাঠিন্য থেকে", "কী কী সমস্যা?")
    + '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px">\n' + comp + "</div>\n"
    + note_pill("অনেক বড় রোগের শুরু হয় দীর্ঘদিনের কোষ্ঠকাঠিন্য থেকে।", dark=True),
    4, "কোষ্ঠকাঠিন্য থেকে ছয়টি সমস্যা: গ্যাস, বদহজম, অর্শ, পেট ফাঁপা, অস্বস্তি আর ক্ষুধামন্দা। অনেক বড় রোগের শুরু হয় দীর্ঘদিনের কোষ্ঠকাঠিন্য থেকে।")

slides["truth"] = statement("truth", "একটি গুরুত্বপূর্ণ বাস্তবতা · KEY TRUTH", "সুস্থ পেট = সুস্থ শরীর", "",
    "শরীরের অনেক সমস্যার সাথে হজম ও পেটের স্বাস্থ্যের গভীর সম্পর্ক রয়েছে।", 5,
    "সুস্থ পেট মানে সুস্থ শরীর। শরীরের অনেক সমস্যার সাথে হজম ও পেটের স্বাস্থ্যের গভীর সম্পর্ক রয়েছে।", dark=False)

slides["product"] = light("product", "#F6F7F0",
    header("প্রোডাক্ট পরিচিতি · PRODUCT", "Costo", "Clear")
    + '<div style="display:flex;flex-direction:row;gap:56px;align-items:center">\n'
      '<div style="flex:1;display:flex;flex-direction:column;gap:24px">\n'
      '<p style="font-size:28px;font-weight:700;letter-spacing:1px;color:#3A1E05;background:#F28C28;border-radius:999px;padding:6px 24px;align-self:start">ন্যাচারাল কোষ্ঠকাঠিন্য কেয়ার</p>\n'
      f'<p style="{HEAD};font-size:46px;font-weight:700;line-height:1.4;color:#12352A">Costo Clear একটি <span style="color:#1F8A4C">ন্যাচারাল ভিত্তিক প্রোডাক্ট,</span> যা কোষ্ঠকাঠিন্য সমস্যার জন্য সহায়ক হিসেবে ব্যবহার করা হয়।</p>\n'
      "</div>\n"
      f'<img src="{PRODUCT}" alt="Costo Clear (কোষ্ঠক্লিয়ার পাউডার) প্রোডাক্টের ছবি" style="width:460px;height:640px;object-fit:contain;border-radius:28px;background:#FFFFFF;border:6px solid #FFFFFF;box-shadow:0 20px 50px rgba(18,53,42,0.18)">\n'
      "</div>\n",
    6, "Costo Clear একটি ন্যাচারাল ভিত্তিক প্রোডাক্ট, যা কোষ্ঠকাঠিন্য সমস্যার জন্য সহায়ক হিসেবে ব্যবহার করা হয়।")

slides["natural"] = light("natural", "#EEF5EA",
    header("Natural Care · প্রাকৃতিক পরিচর্যা", "কেন মানুষ ন্যাচারাল", "সমাধান খুঁজছে?")
    + cards([("Clock", "নিয়মিত ব্যবহার উপযোগী", "Regular use"), ("Lightbulb", "জীবনযাত্রা সচেতনতা", "Lifestyle awareness"),
             ("Star", "খাদ্যাভ্যাসের উন্নতি", "Better diet")])
    + note_pill("বর্তমানে অনেক মানুষ প্রাকৃতিক ও স্বাস্থ্যকর সমাধানের দিকে ঝুঁকছেন।"),
    7, "মানুষ কেন ন্যাচারাল সমাধান খুঁজছে: নিয়মিত ব্যবহার উপযোগী, জীবনযাত্রা সচেতনতা, আর খাদ্যাভ্যাসের উন্নতি।")

slides["making"] = light("making", "#F6F7F0",
    header("Product Making · তৈরির ধারণা", "Costo Clear", "তৈরির ধারণা")
    + cards([("১", "প্রাকৃতিক উপাদান নির্বাচন", "Selection"), ("২", "শুকানো", "Drying"), ("৩", "গুঁড়ো করা", "Grinding"),
             ("৪", "নির্দিষ্ট অনুপাতে মিশ্রণ", "Mixing"), ("৫", "প্যাকেজিং", "Packaging")], icons=False, arrows=True)
    + note_pill("ভালো প্রাকৃতিক প্রোডাক্টের পেছনে সঠিক উপাদান ও সঠিক প্রক্রিয়া গুরুত্বপূর্ণ।"),
    8, "Costo Clear তৈরির পাঁচ ধাপ: প্রাকৃতিক উপাদান নির্বাচন, শুকানো, গুঁড়ো করা, নির্দিষ্ট অনুপাতে মিশ্রণ আর প্যাকেজিং।")

slides["opportunity"] = light("opportunity", "#EEF5EA",
    header("Health Business Opportunity", "মানুষের সমস্যা থেকেই", "সুযোগ")
    + cards([("Warning", "সমস্যা", "Problem"), ("CheckCircle", "সমাধান", "Solution"), ("Chart", "আয়", "Income")], arrows=True)
    + note_pill("আপনি যখন মানুষের একটি বাস্তব সমস্যার সমাধান নিয়ে কাজ করেন, তখন সেখান থেকেই ব্যবসার সুযোগ তৈরি হয়।", dark=True),
    9, "সমস্যা থেকে সমাধান, সমাধান থেকে আয়। মানুষের বাস্তব সমস্যার সমাধান নিয়ে কাজ করলে সেখান থেকেই ব্যবসার সুযোগ তৈরি হয়।")

slides["income"] = light("income", "#F6F7F0",
    header("Income Opportunity · আয়ের পথ", "কীভাবে আয়", "হতে পারে?")
    + cards([("Star", "প্রোডাক্ট বিক্রয়", "Product Selling"), ("Chat", "গ্রাহক সহায়তা", "Customer Support"),
             ("Users", "পুনরায় ক্রেতা", "Repeat Customer"), ("Trust", "বিশ্বাস তৈরি", "Trust Building")])
    + note_pill("স্বাস্থ্য সেক্টরে বিশ্বাসই সবচেয়ে বড় সম্পদ।"),
    10, "আয়ের চারটি পথ: প্রোডাক্ট বিক্রয়, গ্রাহক সহায়তা, পুনরায় ক্রেতা আর বিশ্বাস তৈরি। স্বাস্থ্য সেক্টরে বিশ্বাসই সবচেয়ে বড় সম্পদ।")

slides["mindset"] = statement("mindset", "Entrepreneur Mindset · উদ্যোক্তা মানসিকতা", "পণ্য নয়,", "সমাধান দিন",
    "সফল উদ্যোক্তারা শুধু পণ্য বিক্রি করেন না, তারা মানুষের সমস্যার সমাধান দেন।", 11,
    "সফল উদ্যোক্তারা শুধু পণ্য বিক্রি করেন না, তারা মানুষের সমস্যার সমাধান দেন।")

slides["task"] = light("task", "#EEF5EA",
    header("আজকের টাস্ক · TODAY'S TASK", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Search" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">আপনার পরিচিত কতজন মানুষ গ্যাস, বদহজম বা কোষ্ঠকাঠিন্যে ভুগছেন?</p>\n</div>\n'
    + note_pill("আজ পর্যবেক্ষণ করুন, এই সমস্যাটি আসলে কতটা ব্যাপক।"),
    12, "আজকের Task: আপনার পরিচিত কতজন মানুষ গ্যাস, বদহজম বা কোষ্ঠকাঠিন্যে ভুগছেন? আজ পর্যবেক্ষণ করুন, এই সমস্যাটি আসলে কতটা ব্যাপক।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:96px;font-weight:800;line-height:1.15;text-align:center;color:#FFFFFF">হিজামা: <span style="color:#A6D65A">তৃতীয় ক্লাস</span></h2>
<p style="font-size:36px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">হিজামা সেবার দক্ষতা, দায়িত্ব ও মার্কেটিংয়ের কৌশল</p>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(13)} / {num(TOTAL)}</p>
<aside>আগামীকাল ত্রয়োদশ দিন: হিজামার তৃতীয় ক্লাস। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "what", "causes", "complications", "truth", "product", "natural", "making", "opportunity", "income", "mindset", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-05T10:20:00Z"},
    "lists": "css",
    "title": "দ্বাদশ দিন — Costo Clear",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "কোষ্ঠকাঠিন্য: সংজ্ঞা, কারণ ও জটিলতা", "start": "cover"},
        "s2": {"description": "Costo Clear প্রোডাক্ট ও তৈরির ধারণা", "start": "product"},
        "s3": {"description": "ব্যবসার সুযোগ, আয়ের পথ ও আজকের কাজ", "start": "opportunity"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
