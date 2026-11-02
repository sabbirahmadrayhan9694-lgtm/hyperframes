"""Write the Day 9 (Hijama, class 2) slide files from the offline hijama deck, same look as Days 1–8."""

import json
from pathlib import Path

HERE = Path(__file__).parent
_day8 = (HERE.parent / "day8" / "make_slides.py").read_text(encoding="utf-8")
exec(_day8.split("\nslides = {}")[0])

ROOT = HERE / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 13
LOGO_ALINSAF_9 = "/_blob/5f39a663896aefac7759c81662778a22"
LOGO_INSAFIX_9 = "/_blob/d9311d4b000d918b3a1a28c241dc4efb"
U_DRY_9 = "/_blob/e76fef60c9559ea57964bd68161adc41"
EQ = {
    "cup": "/_blob/31e61e22483685c1e48a15c0cf486804",
    "pump": "/_blob/a70c0a86f5031e96297fdd0b6989a6ed",
    "blade": "/_blob/7c7d758532339c0aa030210c7f9830e4",
    "antiseptic": "/_blob/e826ad8a89db440036e94f0a1c97f682",
    "oil": "/_blob/b0dc5dbfc3ef1f6f647f57784b522f92",
    "tissue": "/_blob/01ca70c23829f6abf6e07f12a9d7f5bb",
}


def rows(items, start, cols=1, size=30):
    parts = [f'<div style="display:grid;grid-template-columns:{" ".join(["1fr"] * cols)};gap:14px 24px">']
    for i, t in enumerate(items):
        n = str(start + i).translate(BN)
        parts.append(
            '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:16px;padding:16px 24px;display:flex;flex-direction:row;gap:20px;align-items:center">'
            f'<p style="{HEAD};font-size:30px;font-weight:800;color:#FFFFFF;background:#2E9E5B;border-radius:999px;padding:2px 16px">{n}</p>'
            f'<p style="font-size:{size}px;line-height:1.4">{t}</p></div>'
        )
    parts.append("</div>\n")
    return "\n".join(parts)


def grid_cards(items, cols=3, hi_last=False):
    """items: (title, text)."""
    parts = [f'<div style="display:grid;grid-template-columns:{" ".join(["1fr"] * cols)};gap:22px">']
    for i, (t, d) in enumerate(items, 1):
        last = hi_last and i == len(items)
        box = "background:#1F7A42" if last else "background:#FFFFFF;border:1px solid #DCE6D6;border-left:8px solid #2E9E5B"
        tc, dc = ("#FFFFFF", "#D7F0C2") if last else ("#12352A", "#4A6358")
        badge = "color:#3A1E05;background:#F28C28" if last else "color:#FFFFFF;background:#2E9E5B"
        parts.append(
            f'<div style="{box};border-radius:22px;padding:26px 30px;display:flex;flex-direction:column;gap:12px">'
            f'<div style="display:flex;flex-direction:row;gap:14px;align-items:center"><p style="{HEAD};font-size:28px;font-weight:800;{badge};border-radius:999px;padding:2px 16px">{str(i).translate(BN)}</p>'
            f'<h3 style="font-size:34px;font-weight:700;color:{tc}">{t}</h3></div>'
            f'<p style="font-size:27px;line-height:1.5;color:{dc}">{d}</p></div>'
        )
    parts.append("</div>\n")
    return "\n".join(parts)


slides = {}

# Cover: same markup as Day 8's cover, with this day's text and photo.
cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
for a, b in [
    (LOGO_ALINSAF, LOGO_ALINSAF_9),
    (LOGO_INSAFIX, LOGO_INSAFIX_9),
    (U_SET, U_DRY_9),
    ('alt="হিজামার কাপ ও পাম্প"', 'alt="পাম্প দিয়ে পিঠে কাপ বসানো হচ্ছে"'),
    (">DAY 08<", ">DAY 09<"),
    ("হিজামা · প্রথম ক্লাস", "হিজামা · দ্বিতীয় ক্লাস"),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'হিজামা: নিরাপত্তা,<br><span style="color:#1F8A4C">দায়িত্ব ও সেবা</span>'),
    (">০৮<", ">০৯<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Warning" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">নিরাপত্তা<br><span style="color:#1F7A42">ও দায়িত্ব</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Chat" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">সাধারণ<br><span style="color:#1F7A42">প্রশ্নোত্তর</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="GraduationCap" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">সেবা ও<br><span style="color:#1F7A42">প্রশিক্ষণ</span>'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>হিজামার দ্বিতীয় ক্লাস। আজ নিরাপত্তা, থেরাপিস্টের পেশাগত দায়িত্ব, সেবা গ্রহণকারীর সাধারণ প্রশ্ন, যন্ত্রপাতি আর প্র্যাকটিক্যাল ট্রেনিং নিয়ে কথা হবে। আগের মতোই সবাইকে খাতায় নোট করতে বলুন।" + cover[b:]
slides["cover"] = cover

slides["nogo1"] = light("nogo1", "#EEF5EA",
    header("SAFETY · নিরাপত্তা" + NOTE, "যাদের হিজামা", "করানো যাবে না (১)")
    + '<p style="font-size:30px;line-height:1.45;color:#4A6358">হিজামা সর্বশ্রেষ্ঠ চিকিৎসা, তবে ঢালাওভাবে সকল রোগীকে হিজামা করানো যাবে না। অনেক রোগীর ক্ষেত্রে হিজামা করানো নিষেধও বটে।</p>\n'
    + rows([
        "হিমোফিলিয়া রোগীদের হিজামা করানো যাবে না।",
        "শরীরের কোনো অংশে বাইরের কোনো ডিভাইস (রিং, পেসমেকার, স্টেন্ট, রড ইত্যাদি) লাগানো থাকলে সেই অংশের চামড়ায় কাপ বসানো যাবে না।",
        "যদি কোনো রোগীর শরীরে IVC Filter (লাং-এর জন্য রক্তনালীতে বসানো একটি ডিভাইস) থাকে, তাদের হিজামা করানো যাবে না।",
        "যদি কোনো রোগীর শরীরে স্টেন্ট বসানো থাকে, তাদের হিজামা করানো যাবে না।",
        "যাদের হৃদপিণ্ডে পেসমেকার বা রিং বসানো আছে, তাদের হৃদপিণ্ডের অংশে (সামনে এবং পেছন দিকে) হিজামা করানো যাবে না।",
    ], 1),
    2, "যাদের হিজামা করানো যাবে না, প্রথম পাঁচটি: হিমোফিলিয়া রোগী, শরীরে বাইরের ডিভাইস লাগানো অংশ, IVC Filter, স্টেন্ট, আর হৃদপিণ্ডে পেসমেকার বা রিং থাকলে হৃদপিণ্ডের অংশে।")

slides["nogo2"] = light("nogo2", "#F6F7F0",
    header("SAFETY · নিরাপত্তা" + NOTE, "যাদের হিজামা", "করানো যাবে না (২)")
    + rows([
        "গর্ভবতী মহিলাদের হিজামা করা যাবে না। একান্ত প্রয়োজন হলে কোমরে হালকা সাকশনে ড্রাই বা ম্যাসাজ কাপিং করানো যেতে পারে।",
        "ঠিক ক্ষতস্থানে হিজামা করা যাবে না।",
        "চোখ, মুখ, কান, লজ্জাস্থানে হিজামা করা যাবে না।",
        "সরাসরি শিরা বা ধমনীর উপরে স্ক্র্যাচ করা যাবে না।",
        "রক্তচাপ খুব বেশি অথবা খুব কম থাকা অবস্থায় হিজামা করা যাবে না।",
        "সরাসরি টিউমারের উপর স্ক্র্যাচ করা যাবে না।",
        "ডায়াবেটিস রোগীদের শক্ত চামড়ায়, টাখনুর নিচে স্ক্র্যাচ করা যাবে না। এতে ক্ষতস্থান শুকাতে দেরি হওয়া, এমনকি ডায়াবেটিক ফুট ইত্যাদির আশঙ্কা থাকে।",
    ], 6, size=28),
    3, "আরও সাতটি সতর্কতা: গর্ভবতী মহিলা, ক্ষতস্থান, চোখ-মুখ-কান-লজ্জাস্থান, শিরা বা ধমনীর উপর, খুব বেশি বা খুব কম রক্তচাপ, টিউমারের উপর, আর ডায়াবেটিস রোগীর শক্ত চামড়া ও টাখনুর নিচে।")

slides["duty"] = light("duty", "#EEF5EA",
    header("PROFESSIONAL DUTY · পেশাগত দায়িত্ব" + NOTE, "রোগী আসার পর", "থেরাপিস্টের দায়িত্ব")
    + grid_cards([
        ("হিজামার রোগী কিনা", "হিজামার রোগী না হলে সময়ক্ষেপণ না করে যথাযথ চিকিৎসক বা হাসপাতালে পাঠিয়ে দিতে হবে।"),
        ("হাসিমুখে বরণ", "উপযুক্ত বিশ্রাম ও টয়লেট দেখিয়ে দেওয়া, তারপর কনসালটেন্সি কক্ষে নেওয়া।"),
        ("সমস্যা জেনে নেওয়া", "কোন রোগের জন্য হিজামা করাতে চান, তা রোগীর কাছ থেকে জেনে নেওয়া।"),
        ("হিজামা সম্পর্কে বলা", "হাদিস ও চিকিৎসা বিজ্ঞান অনুযায়ী হিজামার গুরুত্ব সংক্ষেপে তুলে ধরা।"),
        ("সেশন ও খরচ আগে জানানো", "আনুমানিক কত সেশন লাগতে পারে এবং আজকের সেশনে কত টাকা খরচ হবে, তা আগেই জানানো।"),
        ("ফর্ম পূরণ", "রোগী বিস্তারিত শুনে চিকিৎসা করাতে রাজি হলে ফর্ম পূরণ করা।"),
    ], hi_last=True)
    + "<div></div>\n",
    4, "রোগী আসার পর থেরাপিস্টের ছয়টি দায়িত্ব। মূল উদ্দেশ্য: রোগীর সাথে খোলামেলা কথা বলে তার সমস্যা জানা, আর হিজামা ও ট্রিটমেন্ট প্ল্যান সম্পর্কে রোগীকে জানানো।")

slides["nomagic"] = statement("nomagic", "PROFESSIONAL DUTY · রোগীকে পরিষ্কার ধারণা দিন", "হিজামা একটা চিকিৎসা পদ্ধতি,", "কোনো যাদু নয়",
    "একবার হিজামা নিলাম আর রোগ তৎক্ষণাৎ সেরে যাবে, এমন নয়। এ ব্যাপারে রোগীকে পরিষ্কার ধারণা দেওয়া থেরাপিস্টের দায়িত্ব।", 5,
    "হিজামা একটা চিকিৎসা পদ্ধতি, কোনো যাদু নয় যে একবার হিজামা নিলাম আর রোগ তৎক্ষণাৎ সেরে যাবে। রোগীকে এ ব্যাপারে পরিষ্কার ধারণা দেওয়া জরুরি।")

slides["faq_med"] = light("faq_med", "#F6F7F0",
    header("FAQ · সাধারণ প্রশ্ন ১" + NOTE, "হিজামা করালে কি অন্য", "ঔষধ চালিয়ে যাওয়া যায়?")
    + cards([("CheckCircle", "নিয়মিত ওষুধ", "সাধারণত চলতে পারে"), ("Book", "ওষুধের ইতিহাস", "থেরাপিস্টকে অবশ্যই জানতে হবে"),
             ("Warning", "বিশেষ রোগে", "সতর্কতা প্রয়োজন"), ("Lock", "নিজের ইচ্ছায়", "ওষুধ বন্ধ করা যাবে না")])
    + "<div></div>\n",
    6, "সাধারণত নিয়মিত ওষুধ চলতে পারে। তবে থেরাপিস্টকে অবশ্যই রোগীর ওষুধের ইতিহাস জানতে হবে। কিছু বিশেষ রোগে সতর্কতা প্রয়োজন। নিজের ইচ্ছায় ওষুধ বন্ধ করা যাবে না।")

date_cards = "".join(
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:24px;padding:26px 20px;display:flex;flex-direction:column;align-items:center;gap:4px">'
    f'<p style="{HEAD};font-size:120px;font-weight:800;line-height:1;color:#1F8A4C">{d}</p>'
    '<p style="font-size:26px;color:#4A6358">চন্দ্র মাসের তারিখ</p></div>\n'
    for d in ("১৭", "১৯", "২১")
)
slides["faq_date"] = light("faq_date", "#EEF5EA",
    header("FAQ · সাধারণ প্রশ্ন ২" + NOTE, "হিজামার", "উত্তম তারিখ ও সময়")
    + '<div style="display:flex;flex-direction:row;gap:22px;align-items:stretch">\n' + date_cards
    + '<div style="flex:1.4;background:#1F7A42;border-radius:24px;padding:30px 32px;display:flex;flex-direction:column;justify-content:center;gap:12px">'
      '<x-icon name="Clock" style="color:#A6D65A;width:52px;height:52px"></x-icon>'
      f'<h3 style="{HEAD};font-size:40px;font-weight:800;color:#FFFFFF">খুব সকালে</h3>'
      '<p style="font-size:26px;line-height:1.45;color:#D7F0C2">রাতে পর্যাপ্ত ঘুম ও বিশ্রামের ফলে রক্তপ্রবাহ স্থিতিশীল থাকে</p></div>\n</div>\n'
    + '<p style="font-size:28px;line-height:1.5;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 30px"><b style="color:#B85A0C">চাঁদের সাথে সম্পর্ক:</b> চন্দ্র মাসের ১৭ থেকে ২৭ তারিখ পর্যন্ত রক্তের দূষিত উপাদানগুলো শরীরের তুলনামূলক শান্ত স্থানে, যেমন দুই স্ক্যাপুলার মধ্যবর্তী অংশে জমতে শুরু করে।</p>\n',
    7, "চন্দ্র মাসের ১৭, ১৯ ও ২১ তারিখ হিজামার জন্য সর্বোত্তম। খুব সকালে হিজামা করা ভালো, কারণ রাতে পর্যাপ্ত ঘুম ও বিশ্রামের ফলে রক্তপ্রবাহ স্থিতিশীল থাকে। চন্দ্র মাসের প্রথম ১৫ দিনে রক্তের প্রবাহ বাড়তে থাকে, আর ১৭ থেকে ২৭ তারিখ পর্যন্ত রক্তের দূষিত উপাদানগুলো দুই স্ক্যাপুলার মধ্যবর্তী অংশের মতো শান্ত স্থানে জমতে শুরু করে।")

slides["faq_after"] = light("faq_after", "#F6F7F0",
    header("FAQ · সাধারণ প্রশ্ন ৩" + NOTE, "হিজামার পরে", "রোগীর করণীয়")
    + rows([
        "হিজামার পরপরই ঘুমিয়ে না গিয়ে কিছুক্ষণ হাঁটাচলা করুন",
        "শরীর থেকে কোনো তরল পদার্থ বের হচ্ছে কিনা খেয়াল রাখুন",
        "কুসুম গরম পানিতে গোসল করে শরীরে অলিভ অয়েল ব্যবহার করুন",
        "একদিন পরিপূর্ণ বিশ্রাম উত্তম, তবে সম্পূর্ণ বেডরেস্টের প্রয়োজন নেই",
        "ভিটামিন সি সমৃদ্ধ খাবার ও প্রচুর পানি পান করুন",
        "প্রোটিন সমৃদ্ধ খাবার, ডেইরি প্রোডাক্ট ও এলার্জিযুক্ত খাবার পরিহার করুন",
        "হিজামার স্থানে চুলকানি হলে অলিভ অয়েল ব্যবহার করুন",
        "শারীরিক ব্যায়াম, কঠোর পরিশ্রম ও লম্বা জার্নি পরিহার করুন",
    ], 1, cols=2, size=27)
    + note_pill("এই নিয়মাবলী <b>১-৩ দিন</b> অনুসরণ করা যেতে পারে"),
    8, "হিজামার পরে রোগীর আটটি করণীয়। এই নিয়মাবলী ১ থেকে ৩ দিন অনুসরণ করা যেতে পারে।")

eq_tiles = "".join(
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:22px;padding:16px;display:flex;flex-direction:column;align-items:center;gap:10px">'
    f'<img src="{EQ[k]}" alt="{label}" style="width:220px;height:190px;object-fit:contain">'
    f'<p style="font-size:26px;font-weight:700;text-align:center">{label}</p></div>\n'
    for k, label in [("cup", "হিজামা কাপ"), ("pump", "সাকশন গান"), ("blade", "সার্জিক্যাল ব্লেড"),
                     ("antiseptic", "এন্টিসেপটিক"), ("oil", "ম্যাসেজিং তেল"), ("tissue", "টিস্যু")]
)
slides["equipment"] = light("equipment", "#EEF5EA",
    header("EQUIPMENT · যন্ত্রপাতি" + NOTE, "হিজামার", "প্রয়োজনীয় যন্ত্রপাতি")
    + '<div style="display:flex;flex-direction:row;gap:18px">\n' + eq_tiles + "</div>\n"
    + '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px">\n'
      '<p style="font-size:25px;line-height:1.45;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 22px"><b style="color:#1F7A42">মূল সরঞ্জাম:</b> হিজামা কাপ, সাকশন গান/মেশিন, সার্জিক্যাল ব্লেড, বেড, চেয়ার, বেড টিস্যু।</p>\n'
      '<p style="font-size:25px;line-height:1.45;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 22px"><b style="color:#1F7A42">পরিষ্কারক ও এন্টিসেপটিক:</b> হেক্সিসল, হাইড্রোজেন পার অক্সাইড, নরমাল স্যালাইন, ভায়োডিন, নেবানল পাউডার, ব্যাক্ট্রোসিন অয়েন্টমেন্ট, তুলা।</p>\n'
      '<p style="font-size:25px;line-height:1.45;color:#4A6358;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 22px"><b style="color:#1F7A42">অন্যান্য:</b> হেয়ার ড্রায়ার, ম্যাসেজিং তেল (অলিভ, কালিজিরা, সরিষা, নারিকেল), রক্ত রাখার পাত্র, ফেসিয়াল টিস্যু, ডাস্টবিন।</p>\n'
      "</div>\n",
    9, "সফল ও স্বাস্থ্যসম্মত হিজামার জন্য সঠিক ও মানসম্মত যন্ত্রপাতি জরুরি। তিন ভাগে: মূল সরঞ্জাম, পরিষ্কারক ও এন্টিসেপটিক, আর অন্যান্য প্রয়োজনীয় সামগ্রী। কীভাবে ব্যবহার করতে হয়, তা অফলাইন ট্রেনিং-এ হাতে-কলমে শেখানো হবে।")

slides["practical"] = light("practical", "#F6F7F0",
    header("PRACTICAL TRAINING · অফলাইন প্রশিক্ষণ", "অফলাইন ট্রেনিং-এ", "হাতে-কলমে যা শিখবেন")
    + grid_cards([
        ("থেরাপিস্টের প্রস্তুতি", "সুরক্ষামূলক পোশাক, আত্মিক প্রস্তুতি ও চোখের সুরক্ষা"),
        ("রোগীর প্রস্তুতি", "হিজামার আগে রোগীকে কীভাবে প্রস্তুত করতে হয়"),
        ("ধাপে ধাপে হিজামা", "ম্যাসেজ, কাপ বসানো থেকে শেষ পর্যন্ত পুরো পদ্ধতি"),
        ("সঠিক স্ক্র্যাচের নিয়ম", "কতটুকু গভীর, কতটুকু লম্বা, কোন দিকে"),
        ("অপ্রত্যাশিত অবস্থা ও সমাধান", "মাথা ঘোরা, ফোসকা পড়া, রক্ত কম বের হওয়া"),
        ("সুন্নাহ পয়েন্ট", "কোন সমস্যায় শরীরের কোথায় কাপ বসাতে হয়"),
    ], hi_last=True)
    + '<div style="display:flex;flex-direction:row;gap:18px">\n'
      '<p style="flex:1;font-size:28px;line-height:1.45;text-align:center;color:#FFFFFF;background:#1F7A42;border-radius:999px;padding:18px 32px">শিখে নিজেই <b>হিজামা সেবা দিয়ে আয়</b> করার সুযোগ</p>\n'
      '<p style="font-size:28px;line-height:1.45;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:999px;padding:18px 32px">ফি: [ফি] · স্থান: [স্থান] · মেয়াদ: [সময়]</p>\n'
      "</div>\n",
    10, "এই অংশগুলো অনলাইনে শেখানো হবে না, শুধু অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ হাতে-কলমে শেখানো হবে। প্রশিক্ষণ শেষে নিজেই হিজামা সেবা দিয়ে আয় করার সুযোগ তৈরি হয়। ফি: [ফি], স্থান: [স্থান], মেয়াদ: [সময়]।")

slides["marketing"] = light("marketing", "#EEF5EA",
    header("MARKETING · সেবার পরিচিতি", "হিজামা সেবার", "পরিচিতি ও মার্কেটিং")
    + grid_cards([
        ("সচেতনতামূলক পোস্ট", "হিজামা কী, হাদিস, কাদের হিজামা করানো যাবে না"),
        ("প্রশ্নোত্তর পোস্ট", "ওষুধ, উত্তম তারিখ, হিজামার পরে করণীয়"),
        ("সুন্নাহ তারিখের রিমাইন্ডার", "চন্দ্র মাসের ১৭, ১৯ ও ২১ তারিখের আগে পোস্ট দিন"),
        ("রোগীর অভিজ্ঞতা", "আগে উপকার পাওয়া রোগীর অভিজ্ঞতা, তার অনুমতি নিয়ে"),
    ], cols=2)
    + note_pill("<b>মনে রাখুন:</b> রোগ সেরে যাওয়ার নিশ্চয়তা দেবেন না, হিজামা চিকিৎসা পদ্ধতি, যাদু নয়"),
    11, "আজকের শেখা বিষয়গুলোই মার্কেটিং কনটেন্ট: সচেতনতামূলক পোস্ট, প্রশ্নোত্তর পোস্ট, সুন্নাহ তারিখের আগে রিমাইন্ডার, আর রোগীর অনুমতি নিয়ে তার অভিজ্ঞতা। রোগ সেরে যাওয়ার নিশ্চয়তা কখনো দেবেন না।")

slides["task"] = light("task", "#F6F7F0",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Chat" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:46px;font-weight:800;line-height:1.3;color:#FFFFFF">হিজামা সম্পর্কে সচেতনতামূলক কনটেন্ট প্রচার ও আগ্রহী ব্যক্তির প্রশ্ন সংগ্রহ</p>\n</div>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">\n'
      '<p style="font-size:30px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px"><b>নোট:</b> <span style="color:#4A6358">আজকের সব বিষয় খাতায় গুছিয়ে লিখুন</span></p>\n'
      '<p style="font-size:30px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:24px 32px"><b>প্রশ্ন:</b> <span style="color:#4A6358">আগ্রহীদের প্রশ্নগুলো লিখে গ্রুপে জমা দিন</span></p>\n</div>\n',
    12, "আজকের কাজ: হিজামা সম্পর্কে সচেতনতামূলক কনটেন্ট প্রচার, আর আগ্রহী ব্যক্তিদের প্রশ্ন সংগ্রহ করে গ্রুপে জমা দেওয়া। জমার শেষ সময়: [সময়]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:96px;font-weight:800;line-height:1.15;text-align:center;color:#FFFFFF">দশম দিন: <span style="color:#A6D65A">পলিপাস</span></h2>
<p style="font-size:36px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">হিজামার তৃতীয় ক্লাস হবে ১৩তম দিনে।</p>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(13)} / {num(TOTAL)}</p>
<aside>আগামীকাল দশম দিন: পলিপাস। হিজামার তৃতীয় ক্লাস হবে ১৩তম দিনে। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "nogo1", "nogo2", "duty", "nomagic", "faq_med", "faq_date", "faq_after", "equipment", "practical", "marketing", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-02T14:20:00Z"},
    "lists": "css",
    "title": "নবম দিন — হিজামা: দ্বিতীয় ক্লাস",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "নিরাপত্তা ও থেরাপিস্টের পেশাগত দায়িত্ব", "start": "cover"},
        "s2": {"description": "সেবা গ্রহণকারীর সাধারণ প্রশ্ন", "start": "faq_med"},
        "s3": {"description": "যন্ত্রপাতি, প্র্যাকটিক্যাল ট্রেনিং, মার্কেটিং ও আজকের কাজ", "start": "equipment"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
