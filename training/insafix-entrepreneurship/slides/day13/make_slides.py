"""Write the Day 13 (Hijama, class 3) slide files, same look as Days 1–12.

Built from the schedule's day 13 topics. Facts come from the offline hijama deck
(Offline_Class.pptx) and Days 8–9; course details are bracketed placeholders.
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
_day9 = (HERE.parent / "day9" / "make_slides.py").read_text(encoding="utf-8")
exec(_day9.split("\nslides = {}")[0])

ROOT = HERE / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 11
LOGO_A = "/_blob/5e8d6a5d75ebe0845c9314a03fbbc0a8"
LOGO_I = "/_blob/93a3921b9d2be50e21fa91fae841a3b7"
FIRE = "/_blob/ba3bfb4308a68a6580aa73aa5f5c4e63"
DRY = "/_blob/e38af9fc20ea1b696686ee9b5224b7a3"

slides = {}

cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
for a, b in [
    (LOGO_ALINSAF, LOGO_A),
    (LOGO_INSAFIX, LOGO_I),
    (U_SET, FIRE),
    ('alt="হিজামার কাপ ও পাম্প"', 'alt="আগুন দিয়ে কাপ বসানো হচ্ছে"'),
    (">DAY 08<", ">DAY 13<"),
    ("হিজামা · প্রথম ক্লাস", "হিজামা · তৃতীয় ক্লাস"),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'হিজামা সেবা:<br><span style="color:#1F8A4C">দক্ষতা থেকে আয়</span>'),
    (">০৮<", ">১৩<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Verified" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">দক্ষতা<br><span style="color:#1F7A42">ও দায়িত্ব</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Users" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">কাস্টমার<br><span style="color:#1F7A42">হ্যান্ডলিং</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="GraduationCap" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরবর্তী<br><span style="color:#1F7A42">ধাপ</span>'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>হিজামার তৃতীয় ও শেষ অনলাইন ক্লাস। আজ হিজামা সেবার দক্ষতা ও দায়িত্ব, কাস্টমার হ্যান্ডলিং, সেবার পরিচিতি, মার্কেটিংয়ের কৌশল আর প্র্যাকটিক্যাল প্রশিক্ষণের পরবর্তী ধাপ নিয়ে কথা হবে।" + cover[b:]
slides["cover"] = cover

slides["skills"] = light("skills", "#EEF5EA",
    header("SKILLS · দক্ষতা" + NOTE, "একজন ভালো হিজামা", "থেরাপিস্টের দক্ষতা")
    + grid_cards([
        ("সঠিক জ্ঞান", "হিজামা কী, হাদিস ও চিকিৎসা বিজ্ঞান অনুযায়ী এর গুরুত্ব বুঝিয়ে বলতে পারা"),
        ("সতর্কতা জানা", "কাদের ও কোথায় হিজামা করানো যাবে না, তা আগে থেকেই জানা"),
        ("পরিচ্ছন্নতা", "মানসম্মত যন্ত্রপাতি, এন্টিসেপটিক ও স্বাস্থ্যবিধি মেনে কাজ করা"),
        ("সঠিক পদ্ধতি", "ধাপে ধাপে হিজামা ও সঠিক স্ক্র্যাচ, যা অফলাইন ট্রেনিং-এ হাতে-কলমে শেখানো হয়"),
        ("সুন্দর আচরণ", "রোগীকে হাসিমুখে বরণ করা, খোলামেলা কথা বলে তার সমস্যা জানা"),
        ("জরুরি অবস্থা সামলানো", "মাথা ঘোরা বা অস্বস্তি হলে কী করতে হয়, তা জানা"),
    ], hi_last=True)
    + "<div></div>\n",
    2, "একজন ভালো হিজামা থেরাপিস্টের ছয়টি দক্ষতা: সঠিক জ্ঞান, সতর্কতা জানা, পরিচ্ছন্নতা, সঠিক পদ্ধতি, সুন্দর আচরণ আর জরুরি অবস্থা সামলানো। পদ্ধতি আর জরুরি অবস্থা সামলানো হাতে-কলমে শেখানো হবে অফলাইন ট্রেনিং-এ।")

slides["duty"] = light("duty", "#F6F7F0",
    header("RESPONSIBILITY · দায়িত্বশীলভাবে কাজ" + NOTE, "প্রশিক্ষণ নিয়ে", "দায়িত্বশীলভাবে কাজ")
    + rows([
        "হিজামার রোগী না হলে সময়ক্ষেপণ না করে যথাযথ চিকিৎসক বা হাসপাতালে পাঠিয়ে দিন",
        "রোগ সেরে যাওয়ার নিশ্চয়তা দেবেন না: হিজামা একটা চিকিৎসা পদ্ধতি, কোনো যাদু নয়",
        "কত সেশন লাগতে পারে আর আজকের খরচ কত, তা আগেই জানিয়ে দিন",
        "রোগীকে একা রেখে হিজামার কক্ষ থেকে বের হবেন না",
        "রোগীকে রক্ত দেখাবেন না, প্রয়োজনে শুইয়ে হিজামা করান",
        "যাদের হিজামা করানো যাবে না, তাদের ক্ষেত্রে কখনো ঝুঁকি নেবেন না",
    ], 1, size=29)
    + "<div></div>\n",
    3, "প্রশিক্ষণ নিয়ে দায়িত্বশীলভাবে কাজ করার ছয়টি নিয়ম। সবগুলো আমাদের অফলাইন ক্লাসের লেখা থেকে নেওয়া।")

flow = [("Home", "রোগী এলেন", "হাসিমুখে বরণ, বিশ্রাম"), ("Chat", "সমস্যা জানা", "কোন রোগের জন্য হিজামা"),
        ("Lightbulb", "পরিষ্কার ধারণা", "সেশন, খরচ, সতর্কতা"), ("Book", "ফর্ম পূরণ", "রোগী রাজি হলে"),
        ("CheckCircle", "পরে করণীয় জানানো", "১-৩ দিনের নিয়ম")]
slides["handling"] = light("handling", "#EEF5EA",
    header("CUSTOMER HANDLING · কাস্টমার হ্যান্ডলিং" + NOTE, "রোগী আসা থেকে", "বিদায় পর্যন্ত")
    + cards(flow, arrows=True)
    + note_pill("প্রথম ধাপের উদ্দেশ্য: রোগীর সাথে খোলামেলা কথা বলে তার সমস্যা জানা, আর ট্রিটমেন্ট প্ল্যান সম্পর্কে তাকে জানানো।"),
    4, "রোগী আসা থেকে বিদায় পর্যন্ত পাঁচটি ধাপ: হাসিমুখে বরণ, সমস্যা জানা, সেশন ও খরচ নিয়ে পরিষ্কার ধারণা দেওয়া, রাজি হলে ফর্ম পূরণ, আর হিজামার পরে ১ থেকে ৩ দিনের করণীয় জানিয়ে দেওয়া।")

slides["inform"] = light("inform", "#F6F7F0",
    header("CUSTOMER HANDLING · আগেই জানিয়ে রাখুন" + NOTE, "হিজামার পরে রোগীর", "সাময়িক কিছু পরিবর্তন")
    + rows([
        "দেহের তাপমাত্রা বেড়ে যাওয়া", "অতিরিক্ত ঘাম হওয়া", "তৃষ্ণা লাগা", "মাথা ঘোরানো বা বমিভাব",
        "শরীর কিছুটা দুর্বল লাগা", "হিজামার স্থানে চুলকানি বেড়ে যাওয়া", "শরীরে বা পেশীতে ব্যথা বেড়ে যাওয়া", "ঘুমের সময়ে পরিবর্তন হতে পারে",
    ], 1, cols=2, size=28)
    + note_pill("খুব কম সংখ্যক রোগীর ক্ষেত্রে এই লক্ষণগুলো প্রকাশ পেতে পারে, এতে ভয়ের কিছু নেই।"),
    5, "হিজামার পরে রোগীর সাময়িক আটটি পরিবর্তন আসতে পারে। এগুলো আগেই জানিয়ে রাখলে রোগী ভয় পান না, আর আপনার ওপর তার বিশ্বাস বাড়ে।")

slides["trust"] = statement("trust", "সেবার মূলমন্ত্র · TRUST", "স্বাস্থ্য সেক্টরে বিশ্বাসই", "সবচেয়ে বড় সম্পদ",
    "সঠিক তথ্য, পরিচ্ছন্ন সেবা আর সৎ পরামর্শ, এই তিনটি থাকলে রোগী নিজেই অন্যদের আপনার কাছে পাঠাবে।", 6,
    "স্বাস্থ্য সেক্টরে বিশ্বাসই সবচেয়ে বড় সম্পদ। সন্তুষ্ট রোগীই সবচেয়ে ভালো বিজ্ঞাপন।")

intro_rows = "".join(
    '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 26px;display:flex;flex-direction:row;gap:18px;align-items:center">'
    f'<x-icon name="{ic}" style="color:#1F7A42;width:36px;height:36px"></x-icon>'
    f'<p style="font-size:29px;line-height:1.35"><b>{k}:</b> <span style="color:#4A6358">{v}</span></p></div>\n'
    for ic, k, v in [("Home", "সেবার নাম ও ঠিকানা", "[নাম] · [ঠিকানা]"), ("Clock", "সেবার সময়", "[দিন ও সময়]"),
                     ("Star", "সেবার খরচ", "[প্রতি সেশন ৳__]"), ("Users", "থেরাপিস্ট", "[পুরুষ / মহিলা থেরাপিস্ট]"),
                     ("Chat", "যোগাযোগ", "[মোবাইল নম্বর]")]
)
slides["service"] = light("service", "#EEF5EA",
    header("SERVICE INTRO · সেবার পরিচিতি" + NOTE, "আপনার হিজামা সেবার", "পরিচিতি কার্ড")
    + '<div style="display:flex;flex-direction:row;gap:40px;align-items:center">\n'
      '<div style="flex:1;display:flex;flex-direction:column;gap:14px">\n' + intro_rows + "</div>\n"
      f'<img src="{DRY}" alt="পাম্প দিয়ে পিঠে কাপ বসানো হচ্ছে" style="width:520px;height:560px;object-fit:cover;border-radius:28px;border:6px solid #FFFFFF;box-shadow:0 20px 50px rgba(18,53,42,0.18)">\n'
      "</div>\n",
    7, "প্রতিটি পোস্ট ও কথাবার্তায় এই পাঁচটি তথ্য পরিষ্কার রাখুন: সেবার নাম ও ঠিকানা, সময়, খরচ, থেরাপিস্ট কে, আর যোগাযোগের নম্বর। প্রশিক্ষণ শেষে প্রত্যেকে নিজের তথ্য বসিয়ে এই কার্ড বানাবেন।")

slides["marketing"] = light("marketing", "#F6F7F0",
    header("MARKETING · মার্কেটিংয়ের কৌশল" + NOTE, "হিজামা মার্কেটিংয়ের", "কৌশল")
    + grid_cards([
        ("সুন্নাহ তারিখের ক্যাম্পেইন", "চন্দ্র মাসের ১৭, ১৯ ও ২১ তারিখের আগে বুকিং নেওয়ার পোস্ট"),
        ("সচেতনতামূলক পোস্ট", "হিজামা কী, হাদিস, কোন রোগে নেওয়া হয়, কাদের করানো যাবে না"),
        ("প্রশ্নোত্তর", "ওষুধ, উত্তম সময়, হিজামার পরে করণীয়, এমন প্রশ্নের উত্তর"),
        ("রোগীর অভিজ্ঞতা", "আগে উপকার পাওয়া রোগীর অভিজ্ঞতা, তার অনুমতি নিয়ে"),
        ("রেফারেল", "সন্তুষ্ট রোগীকে পরিচিতদের কাছে আপনার কথা বলতে অনুরোধ"),
        ("ফলোআপ", "হিজামার পরে খোঁজ নেওয়া, পরের সেশনের তারিখ মনে করিয়ে দেওয়া"),
    ])
    + note_pill("<b>মনে রাখুন:</b> রোগ সেরে যাওয়ার নিশ্চয়তা দেবেন না, আর রোগীর ছবি বা ভিডিও তার অনুমতি ছাড়া দেবেন না"),
    8, "ছয়টি মার্কেটিং কৌশল: সুন্নাহ তারিখের ক্যাম্পেইন, সচেতনতামূলক পোস্ট, প্রশ্নোত্তর, রোগীর অভিজ্ঞতা, রেফারেল আর ফলোআপ।")

steps = [("১", "রেজিস্ট্রেশন", "[কীভাবে ও কোথায়]"), ("২", "অফলাইন ট্রেনিং", "[স্থান · মেয়াদ]"),
         ("৩", "হাতে-কলমে অনুশীলন", "প্রশিক্ষকের তত্ত্বাবধানে"), ("৪", "নিজের সেবা শুরু", "হিজামা সেবা দিয়ে আয়")]
slides["next"] = light("next", "#EEF5EA",
    header("PRACTICAL TRAINING · পরবর্তী ধাপ", "প্র্যাকটিক্যাল প্রশিক্ষণের", "পরবর্তী ধাপ")
    + cards(steps, icons=False, arrows=True)
    + '<div style="display:flex;flex-direction:row;gap:18px">\n'
      '<p style="flex:1;font-size:28px;line-height:1.45;text-align:center;color:#FFFFFF;background:#1F7A42;border-radius:999px;padding:18px 32px">অনলাইনে শিখলেন তত্ত্ব, অফলাইনে শিখবেন <b>হাতে-কলমে পুরো পদ্ধতি</b></p>\n'
      '<p style="font-size:28px;line-height:1.45;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:999px;padding:18px 32px">ফি: [ফি]</p>\n'
      "</div>\n",
    9, "প্র্যাকটিক্যাল প্রশিক্ষণের চার ধাপ: রেজিস্ট্রেশন, অফলাইন ট্রেনিং, প্রশিক্ষকের তত্ত্বাবধানে হাতে-কলমে অনুশীলন, তারপর নিজের হিজামা সেবা শুরু। রেজিস্ট্রেশনের নিয়ম, স্থান, মেয়াদ ও ফি: [বসাতে হবে]।")

slides["task"] = light("task", "#F6F7F0",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Chart" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:46px;font-weight:800;line-height:1.3;color:#FFFFFF">নিজের অগ্রগতি মূল্যায়ন এবং প্র্যাকটিক্যাল প্রশিক্ষণ সম্পর্কে প্রশ্ন প্রস্তুত করা</p>\n</div>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>মূল্যায়ন:</b> <span style="color:#4A6358">৩টি হিজামা ক্লাসে কী কী শিখলেন, লিখুন</span></p>\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>প্রশ্ন:</b> <span style="color:#4A6358">অফলাইন ট্রেনিং নিয়ে আপনার প্রশ্ন গ্রুপে দিন</span></p>\n</div>\n',
    10, "আজকের কাজ: নিজের অগ্রগতি মূল্যায়ন, আর প্র্যাকটিক্যাল প্রশিক্ষণ নিয়ে প্রশ্ন প্রস্তুত করে গ্রুপে জমা দেওয়া। জমার শেষ সময়: [সময়]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:84px;font-weight:800;line-height:1.15;text-align:center;color:#FFFFFF">সেলস রিভিউ, কাস্টমার ফলোআপ<br><span style="color:#A6D65A">ও ব্যবসার হিসাব</span></h2>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(11)} / {num(TOTAL)}</p>
<aside>আগামীকাল চতুর্দশ দিন: সেলস রিভিউ, কাস্টমার ফলোআপ ও ব্যবসার হিসাব। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "skills", "duty", "handling", "inform", "trust", "service", "marketing", "next", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-06T10:00:00Z"},
    "lists": "css",
    "title": "ত্রয়োদশ দিন — হিজামা: তৃতীয় ক্লাস",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "হিজামা সেবার দক্ষতা ও দায়িত্ব", "start": "cover"},
        "s2": {"description": "কাস্টমার হ্যান্ডলিং ও সেবার পরিচিতি", "start": "handling"},
        "s3": {"description": "মার্কেটিং, প্রশিক্ষণের পরবর্তী ধাপ ও আজকের কাজ", "start": "marketing"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
