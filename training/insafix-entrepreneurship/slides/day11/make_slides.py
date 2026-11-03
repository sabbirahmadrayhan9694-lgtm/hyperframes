"""Write the Day 11 (Leucorrhea Safe) slide files from the old Day 10 deck, same look as Days 1–10.

Content is the old deck's, slide for slide; only the look changes. ভেষজ → প্রাকৃতিক.
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
_day9 = (HERE.parent / "day9" / "make_slides.py").read_text(encoding="utf-8")
exec(_day9.split("\nslides = {}")[0])

ROOT = HERE / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 14
LOGO_A = "/_blob/24317032705d0f7ede9c9c99571acbea"
LOGO_I = "/_blob/5ac39d557d0b30a819e30b4f929ab6f4"
PRODUCT = "/_blob/f80fdc387a874ef39eaad933c9086977"

slides = {}

cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
for a, b in [
    (LOGO_ALINSAF, LOGO_A),
    (LOGO_INSAFIX, LOGO_I),
    (f'<img src="{U_SET}" alt="হিজামার কাপ ও পাম্প" style="position:absolute;left:1292px;top:190px;width:500px;height:334px;',
     f'<img src="{PRODUCT}" alt="Leucorrhea Safe প্রোডাক্টের ছবি" style="position:absolute;left:1340px;top:110px;width:452px;height:452px;'),
    ('left:1220px;top:440px;width:200px;height:200px;border-radius:50%', 'left:1250px;top:470px;width:200px;height:200px;border-radius:50%'),
    (">DAY 08<", ">DAY 11<"),
    ("হিজামা · প্রথম ক্লাস", "Leucorrhea Problem &amp; Leucorrhea Safe"),
    ('<h1 style="{HEAD};font-size:100px;'.replace("{HEAD}", HEAD), f'<h1 style="{HEAD};font-size:88px;'),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'নারীদের সাদা স্রাব সমস্যা ও<br><span style="color:#1F8A4C">Leucorrhea Safe</span>'),
    (">০৮<", ">১১<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Users" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">নারী<br><span style="color:#1F7A42">স্বাস্থ্য</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Warning" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">লক্ষণ<br><span style="color:#1F7A42">ও কারণ</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="Verified" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">প্রোডাক্ট<br><span style="color:#1F7A42">ও সচেতনতা</span>'),
    ('<b style="color:#B85A0C">খাতা-কলম নিন:</b> আজকের প্রতিটি বিষয় নোট করে রাখুন',
     'আজ এমন একটি বিষয় নিয়ে কথা বলবো, যা অনেক নারীর জন্য সাধারণ কিন্তু গুরুত্বপূর্ণ একটি স্বাস্থ্য বিষয়।'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>আজ এমন একটি বিষয় নিয়ে কথা বলবো, যা অনেক নারীর জন্য সাধারণ কিন্তু গুরুত্বপূর্ণ একটি স্বাস্থ্য বিষয়: নারীদের সাদা স্রাব সমস্যা ও Leucorrhea Safe।" + cover[b:]
slides["cover"] = cover

slides["family"] = statement("family", "পরিবারে নারীর সুস্থতা · FAMILY HEALTH", "সুস্থ নারী = সুস্থ পরিবার", "",
    "একজন মা, বোন বা স্ত্রীর সুস্থতা পুরো পরিবারের উপর প্রভাব ফেলে, তাই নারীস্বাস্থ্য সচেতনতা অত্যন্ত গুরুত্বপূর্ণ।", 2,
    "সুস্থ নারী মানে সুস্থ পরিবার। একজন মা, বোন বা স্ত্রীর সুস্থতা পুরো পরিবারের উপর প্রভাব ফেলে।", dark=False)

slides["what"] = light("what", "#EEF5EA",
    header("সংজ্ঞা · WHAT IS IT", "সাদা স্রাব", "(Leucorrhea) কী?")
    + cards([("১", "সাধারণ স্বাস্থ্য বিষয়", "নারীদের একটি সাধারণ স্বাস্থ্য বিষয়"),
             ("২", "বিভিন্ন কারণ", "বিভিন্ন কারণে হতে পারে"),
             ("৩", "স্বাভাবিক নাকি চিকিৎসা", "কিছু ক্ষেত্রে স্বাভাবিক, কিছু ক্ষেত্রে চিকিৎসা প্রয়োজন")], icons=False)
    + note_pill("<b>মনে রাখুন:</b> সাদা স্রাব সবসময় রোগের লক্ষণ নয়, তবে অস্বাভাবিক হলে গুরুত্ব দেওয়া প্রয়োজন।"),
    3, "সাদা স্রাব নারীদের একটি সাধারণ স্বাস্থ্য বিষয়, বিভিন্ন কারণে হতে পারে। কিছু ক্ষেত্রে স্বাভাবিক, কিছু ক্ষেত্রে চিকিৎসা প্রয়োজন। সাদা স্রাব সবসময় রোগের লক্ষণ নয়, তবে অস্বাভাবিক হলে গুরুত্ব দেওয়া প্রয়োজন।")

slides["signs"] = light("signs", "#F6F7F0",
    header("সতর্কতার লক্ষণ · WARNING SIGNS", "কখন সচেতন", "হওয়া দরকার?")
    + cards([("Warning", "অতিরিক্ত স্রাব", "Excess"), ("Cloud", "দুর্গন্ধ", "Odor"), ("Activity", "চুলকানি", "Itching"),
             ("Lightning", "জ্বালাপোড়া", "Burning"), ("Users", "শারীরিক অস্বস্তি", "Discomfort")])
    + note_pill("এ ধরনের লক্ষণ দেখা দিলে বিশেষজ্ঞ চিকিৎসকের পরামর্শ নেওয়া গুরুত্বপূর্ণ।"),
    4, "পাঁচটি সতর্কতার লক্ষণ: অতিরিক্ত স্রাব, দুর্গন্ধ, চুলকানি, জ্বালাপোড়া আর শারীরিক অস্বস্তি। এ ধরনের লক্ষণ দেখা দিলে বিশেষজ্ঞ চিকিৎসকের পরামর্শ নেওয়া গুরুত্বপূর্ণ।")

slides["causes"] = light("causes", "#EEF5EA",
    header("সম্ভাব্য কারণ · POSSIBLE CAUSES", "সম্ভাব্য", "কারণ")
    + cards([("Search", "ব্যক্তিগত পরিচ্ছন্নতার অভাব", "Hygiene"), ("Warning", "সংক্রমণ", "Infection"),
             ("Settings", "হরমোনজনিত পরিবর্তন", "Hormonal change"), ("Activity", "শারীরিক দুর্বলতা", "Weakness")])
    + note_pill("সঠিক কারণ নির্ণয়ের জন্য স্বাস্থ্য সচেতনতা ও প্রয়োজনে চিকিৎসা পরামর্শ জরুরি।"),
    5, "সম্ভাব্য চারটি কারণ: ব্যক্তিগত পরিচ্ছন্নতার অভাব, সংক্রমণ, হরমোনজনিত পরিবর্তন আর শারীরিক দুর্বলতা।")

slides["silent"] = statement("silent", "একটি বাস্তব সমস্যা · A REAL ISSUE", "অনেক নারী নীরবে", "কষ্ট সহ্য করেন",
    "লজ্জা বা সংকোচের কারণে অনেকে সমস্যাটি নিয়ে খোলাখুলি কথা বলেন না, সচেতনতাই প্রথম পদক্ষেপ।", 6,
    "লজ্জা বা সংকোচের কারণে অনেকে সমস্যাটি নিয়ে খোলাখুলি কথা বলেন না। সচেতনতাই প্রথম পদক্ষেপ।")

slides["product"] = light("product", "#F6F7F0",
    header("প্রোডাক্ট পরিচিতি · PRODUCT", "Leucorrhea", "Safe")
    + '<div style="display:flex;flex-direction:row;gap:56px;align-items:center">\n'
      '<div style="flex:1;display:flex;flex-direction:column;gap:24px">\n'
      '<p style="font-size:28px;font-weight:700;letter-spacing:1px;color:#3A1E05;background:#F28C28;border-radius:999px;padding:6px 24px;align-self:start">প্রাকৃতিক স্বাস্থ্য সহায়ক প্রোডাক্ট</p>\n'
      f'<p style="{HEAD};font-size:46px;font-weight:700;line-height:1.4;color:#12352A">Leucorrhea Safe নারীদের স্বাস্থ্য সচেতনতার অংশ হিসেবে ব্যবহৃত একটি <span style="color:#1F8A4C">প্রাকৃতিক সহায়ক প্রোডাক্ট।</span></p>\n'
      "</div>\n"
      f'<img src="{PRODUCT}" alt="Leucorrhea Safe প্রোডাক্টের ছবি" style="width:620px;height:620px;object-fit:cover;border-radius:28px;border:6px solid #FFFFFF;box-shadow:0 20px 50px rgba(18,53,42,0.18)">\n'
      "</div>\n",
    7, "Leucorrhea Safe নারীদের স্বাস্থ্য সচেতনতার অংশ হিসেবে ব্যবহৃত একটি প্রাকৃতিক সহায়ক প্রোডাক্ট।")

slides["making"] = light("making", "#EEF5EA",
    header("Product Making · তৈরির ধারণা", "প্রোডাক্ট", "তৈরির ধারণা")
    + cards([("১", "প্রাকৃতিক উপাদান নির্বাচন", "Selection"), ("২", "সঠিক প্রস্তুতি", "Preparation"),
             ("৩", "মান নিয়ন্ত্রণ", "Quality control"), ("৪", "স্বাস্থ্যসম্মত প্যাকেজিং", "Packaging")], icons=False, arrows=True)
    + note_pill("একটি মানসম্মত প্রাকৃতিক প্রোডাক্ট তৈরিতে সঠিক উপাদান ও সঠিক প্রক্রিয়া গুরুত্বপূর্ণ।"),
    8, "প্রোডাক্ট তৈরির চার ধাপ: প্রাকৃতিক উপাদান নির্বাচন, সঠিক প্রস্তুতি, মান নিয়ন্ত্রণ আর স্বাস্থ্যসম্মত প্যাকেজিং।")

slides["awareness"] = light("awareness", "#F6F7F0",
    header("Health Awareness · স্বাস্থ্য সচেতনতা", "স্বাস্থ্য", "সচেতনতা")
    + cards([("Search", "পরিচ্ছন্নতা", "Hygiene"), ("Star", "সুষম খাদ্য", "Balanced diet"),
             ("Activity", "পর্যাপ্ত পানি পান", "Hydration"), ("Clock", "নিয়মিত স্বাস্থ্য সচেতনতা", "Regular care")])
    + note_pill("স্বাস্থ্য সচেতনতা অনেক সমস্যাকে শুরুতেই নিয়ন্ত্রণে রাখতে সাহায্য করে।"),
    9, "চারটি অভ্যাস: পরিচ্ছন্নতা, সুষম খাদ্য, পর্যাপ্ত পানি পান আর নিয়মিত স্বাস্থ্য সচেতনতা।")

slides["business"] = light("business", "#EEF5EA",
    header("Health Business Opportunity", "Problem → Awareness →", "Solution")
    + cards([("Warning", "সমস্যা", "Problem"), ("Lightbulb", "সচেতনতা", "Awareness"), ("CheckCircle", "সমাধান", "Solution")], arrows=True)
    + note_pill("যখন মানুষ একটি সমস্যা সম্পর্কে সচেতন হয়, তখন সমাধানের পথও সহজ হয়।", dark=True),
    10, "সমস্যা থেকে সচেতনতা, সচেতনতা থেকে সমাধান। যখন মানুষ একটি সমস্যা সম্পর্কে সচেতন হয়, তখন সমাধানের পথও সহজ হয়।")

slides["responsibility"] = statement("responsibility", "উদ্যোক্তার দায়িত্ব · RESPONSIBILITY", "শুধু বিক্রয় নয়,", "সচেতনতা তৈরি করুন",
    "একজন সফল স্বাস্থ্য উদ্যোক্তা শুধু পণ্য পরিচয় করিয়ে দেন না, মানুষের মধ্যে সচেতনতা তৈরি করেন।", 11,
    "একজন সফল স্বাস্থ্য উদ্যোক্তা শুধু পণ্য পরিচয় করিয়ে দেন না, মানুষের মধ্যে সচেতনতা তৈরি করেন।")

slides["task"] = light("task", "#F6F7F0",
    header("আজকের টাস্ক · TODAY'S TASK", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Lightbulb" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">নারীদের স্বাস্থ্য সচেতনতা বৃদ্ধির জন্য কী করা যায়?</p>\n</div>\n'
    + note_pill("আজ ভাবুন, কীভাবে পরিবার ও সমাজে স্বাস্থ্য সচেতনতা বাড়ানো যায়।"),
    12, "আজকের Task: নারীদের স্বাস্থ্য সচেতনতা বৃদ্ধির জন্য কী করা যায়? আজ ভাবুন, কীভাবে পরিবার ও সমাজে স্বাস্থ্য সচেতনতা বাড়ানো যায়।")

recap = "".join(
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:28px;padding:36px 28px;display:flex;flex-direction:column;align-items:center;gap:8px">'
    f'<p style="{HEAD};font-size:120px;font-weight:800;line-height:1;color:{c}">{n}</p>'
    f'<h3 style="font-size:36px;font-weight:700;text-align:center">{bn}</h3><p style="font-size:26px;color:#4A6358">{en}</p></div>\n'
    for n, bn, en, c in [("৫টি", "স্বাস্থ্য সমস্যা", "Health Problems", "#1F8A4C"), ("৫টি", "সমাধানের ধারণা", "Solution Ideas", "#1F8A4C"),
                         ("১টি", "বড় সুযোগ সামনে", "Big Opportunity", "#B85A0C")]
)
slides["recap"] = light("recap", "#EEF5EA",
    header("যাত্রার সারসংক্ষেপ · RECAP", "এখন সামনে", "আরও বড় সুযোগ")
    + '<div style="display:flex;flex-direction:row;gap:24px">\n' + recap + "</div>\n"
    + note_pill("এবার এই জ্ঞানকে বাস্তব কাজ ও আয়ের সুযোগের সাথে সংযুক্ত করার পালা।", dark=True),
    13, "সারসংক্ষেপ: ৫টি স্বাস্থ্য সমস্যা, ৫টি সমাধানের ধারণা, আর সামনে ১টি বড় সুযোগ। এবার এই জ্ঞানকে বাস্তব কাজ ও আয়ের সুযোগের সাথে সংযুক্ত করার পালা।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:30px">
{DARK_BG}
<h2 style="{HEAD};font-size:110px;font-weight:800;line-height:1.1;text-align:center;color:#FFFFFF">Thank <span style="color:#A6D65A">You</span></h2>
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<p style="font-size:30px;font-weight:600;letter-spacing:1px;color:#F6B26B">ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি</p>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="font-size:34px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">আজকের ক্লাস এখানেই শেষ, আগামী ক্লাস থেকে আরও গুরুত্বপূর্ণ বাস্তব বিষয় নিয়ে আলোচনা করবো।</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(14)} / {num(TOTAL)}</p>
<aside>আজকের ক্লাস এখানেই শেষ। আগামীকাল দ্বাদশ দিন: Gastro Safe। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "family", "what", "signs", "causes", "silent", "product", "making", "awareness", "business", "responsibility", "task", "recap", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-03T00:20:00Z"},
    "lists": "css",
    "title": "একাদশ দিন — Leucorrhea Safe",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "নারীস্বাস্থ্য, সাদা স্রাব, লক্ষণ ও কারণ", "start": "cover"},
        "s2": {"description": "Leucorrhea Safe প্রোডাক্ট ও স্বাস্থ্য সচেতনতা", "start": "product"},
        "s3": {"description": "উদ্যোক্তার দায়িত্ব, আজকের কাজ ও সারসংক্ষেপ", "start": "business"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
