"""Write the Day 10 (Polypus) slide files from the old nasal polyp deck, same look as Days 1–9.

Left out on purpose (offline training only): drug doses by age, the spray/lidocaine
step protocol, the antibiotic protocol and the "permanent cure" claims.
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
P_DIAGRAM = "/_blob/0d69c7a65f41e669315db9fd587ad04f"
P_NOSTRIL = "/_blob/479faad0de56505ad525bd4918260935"
P_SINUS = "/_blob/3ba6b45dd478a13a333c0ccaa8a79177"
P_AIRWAY = "/_blob/9b704aa65a67ca0f95b27cbcdbc33007"
LOGO_A = "/_blob/aff41232c31b700685657584720cf839"
LOGO_I = "/_blob/5c6c34f65f1398a4704cc449300b956f"
COMBO = "/_blob/6c8bc511084357adac7a3b94a6203742"
TOOLS = [
    ("/_blob/1515475ce1a7a749b0bf59b7aee4f340", "নেজাল স্পেকুলাম"),
    ("/_blob/4a3a2938ee52e656453cf25477d942d6", "সার্জিক্যাল গ্লাভস"),
    ("/_blob/7bf6ac2a984b957837d0e950b781bd16", "সার্জিক্যাল মাস্ক"),
    ("/_blob/946b8c1902661b335853a8db134e9420", "লম্বা কটন বাড"),
    ("/_blob/0f8130af0243d95e658c0f8ee6d448e9", "হেডলাইট"),
    ("/_blob/c3f026dc864c59f0b07a919987509877", "আর্টারি ফরসেপস"),
]

slides = {}

cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
for a, b in [
    (LOGO_ALINSAF, LOGO_A),
    (LOGO_INSAFIX, LOGO_I),
    (f'<img src="{U_SET}" alt="হিজামার কাপ ও পাম্প" style="position:absolute;left:1292px;top:190px;width:500px;height:334px;',
     f'<img src="{COMBO}" alt="পলিপা কেয়ার কম্বো প্যাক" style="position:absolute;left:1420px;top:110px;width:372px;height:465px;'),
    ('left:1220px;top:440px;width:200px;height:200px;border-radius:50%', 'left:1300px;top:470px;width:200px;height:200px;border-radius:50%'),
    (">DAY 08<", ">DAY 10<"),
    ("হিজামা · প্রথম ক্লাস", "পলিপাস · হেলথ সেবা"),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'নেসাল পলিপাস:<br><span style="color:#1F8A4C">প্রাথমিক ধারণা</span>'),
    (">০৮<", ">১০<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Search" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">লক্ষণ<br><span style="color:#1F7A42">ও কারণ</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="GraduationCap" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">সেবা ও<br><span style="color:#1F7A42">প্রশিক্ষণ</span>'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>দশম দিন: নেসাল পলিপাস। আজ পলিপাস কী, এর ধরন, লক্ষণ, রোগীর হিস্ট্রি, চিকিৎসা পদ্ধতির তুলনা, খাদ্যাভ্যাস ও সতর্কতা নিয়ে আলোচনা হবে। ক্রিম প্রয়োগের পুরো পদ্ধতি শেখানো হবে অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ।" + cover[b:]
slides["cover"] = cover

def_rows = "".join(
    '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:20px 26px;display:flex;flex-direction:row;gap:20px;align-items:center">'
    f'<div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="{ic}" style="color:#FFFFFF;width:36px;height:36px"></x-icon></div>'
    f'<div style="display:flex;flex-direction:column;gap:4px"><h3 style="font-size:32px;font-weight:700;color:#12352A">{t}</h3><p style="font-size:26px;line-height:1.4;color:#4A6358">{d}</p></div></div>\n'
    for ic, t, d in [("Settings", "পরিষ্কারক", "বাতাসের ধূলিকণা ও জীবাণু নাকের লোম ও মিউকাসে ফিল্টার হয়"),
                     ("Activity", "তাপমাত্রা নিয়ন্ত্রক", "বাইরের শীতল বা উষ্ণ বাতাসকে ফুসফুসের জন্য উষ্ণ ও আর্দ্র করে"),
                     ("Trust", "রক্ষাকবচ", "ঘ্রাণের মাধ্যমে ক্ষতিকর পরিবেশ বা খাবার সম্পর্কে মস্তিষ্ককে সতর্ক করে")]
)
slides["defense"] = light("defense", "#EEF5EA",
    header("ANATOMY · শ্বাসতন্ত্রের প্রবেশদ্বার" + NOTE, "নাকের", "প্রতিরক্ষা ব্যবস্থা")
    + '<div style="display:flex;flex-direction:row;gap:40px;align-items:center">\n'
      f'<img src="{P_AIRWAY}" alt="শ্বাসতন্ত্রের ছবি: নাক থেকে ফুসফুস পর্যন্ত" style="width:470px;height:466px;object-fit:contain;border-radius:24px">\n'
      '<div style="flex:1;display:flex;flex-direction:column;gap:16px">\n' + def_rows
    + '<p style="font-size:27px;line-height:1.45;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:20px;padding:18px 26px">নাক বন্ধ থাকলে মুখ দিয়ে শ্বাস নিতে হয়, যা ফুসফুসকে সরাসরি জীবাণু ও শুষ্ক বাতাসের সম্মুখীন করে</p>\n'
      "</div>\n</div>\n",
    2, "নাক শ্বাসতন্ত্রের প্রবেশদ্বার: পরিষ্কারক, তাপমাত্রা নিয়ন্ত্রক আর রক্ষাকবচ। নাক বন্ধ থাকলে মুখ দিয়ে শ্বাস নিতে হয়, যা ফুসফুসকে সরাসরি জীবাণু ও শুষ্ক বাতাসের সম্মুখীন করে।")

sinus = "".join(
    '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 24px;display:flex;flex-direction:column;gap:4px">'
    f'<h3 style="font-size:32px;font-weight:700;color:#12352A">{bn}</h3><p style="font-size:24px;color:#4A6358">{en}</p></div>\n'
    for bn, en in [("ফ্রন্টাল সাইনাস", "Frontal Sinus"), ("ইথময়ডাল সাইনাস", "Ethmoidal Sinuses"),
                   ("ম্যাক্সিলারী সাইনাস", "Maxillary Sinus"), ("স্ফেনয়ডাল সাইনাস", "Sphenoidal Sinus")]
)
slides["what"] = light("what", "#F6F7F0",
    header("WHAT IS POLYPUS · পলিপাস কী" + NOTE, "পলিপাস", "কী?")
    + '<div style="display:flex;flex-direction:row;gap:48px;align-items:center">\n'
      '<div style="flex:1;background:#1F7A42;border-radius:28px;padding:44px 48px;display:flex;flex-direction:column;gap:20px">'
      f'<p style="{HEAD};font-size:44px;font-weight:700;line-height:1.4;color:#FFFFFF">নাক এবং প্যারানাজাল সাইনাসের মধ্যকার মিউকাস টিস্যুর অতিরিক্ত মাংস বৃদ্ধিই হলো পলিপাস,</p>'
      '<p style="font-size:32px;line-height:1.45;color:#D7F0C2">যা সাইনাসের স্বাভাবিক রস নিঃসরণে বাধা সৃষ্টি করে।</p></div>\n'
      f'<img src="{P_DIAGRAM}" alt="নাকের ভেতরে পলিপাস: স্পেকুলাম দিয়ে দেখা ছবি ও নকশা" style="width:600px;height:608px;object-fit:contain;border-radius:24px;border:6px solid #FFFFFF;box-shadow:0 20px 50px rgba(18,53,42,0.18)">\n'
      "</div>\n",
    3, "নাক এবং প্যারানাজাল সাইনাসের মধ্যকার মিউকাস টিস্যুর অতিরিক্ত মাংস বৃদ্ধিই হলো পলিপাস, যা সাইনাসের স্বাভাবিক রস নিঃসরণে বাধা সৃষ্টি করে। ছবিতে স্পেকুলাম দিয়ে নাকের ভেতরে পলিপাস দেখানো হয়েছে, নিচে তার নকশা।")

slides["sinus"] = light("sinus", "#EEF5EA",
    header("SINUS · প্যারানাজাল সাইনাস" + NOTE, "প্যারানাজাল সাইনাস", "ও পলিপাসের অবস্থান")
    + '<div style="display:flex;flex-direction:row;gap:40px;align-items:center">\n'
      f'<img src="{P_SINUS}" alt="মুখের ভেতরে চারটি সাইনাস ও পলিপাস" style="width:1080px;height:535px;object-fit:contain;border-radius:24px">\n'
      '<div style="flex:1;display:flex;flex-direction:column;gap:14px">\n' + sinus + "</div>\n</div>\n",
    4, "প্যারানাজাল সাইনাস চারটি: ফ্রন্টাল, ইথময়ডাল, ম্যাক্সিলারী আর স্ফেনয়ডাল। ছবিতে নাকের ভেতরের হলুদ অংশগুলো পলিপাস, যা সাইনাসের রস বের হওয়ার পথ বন্ধ করে দেয়।")

slides["types"] = light("types", "#EEF5EA",
    header("TYPES · প্রকারভেদ ও কারণ" + NOTE, "নেসাল পলিপাসের", "প্রকারভেদ ও কারণ")
    + grid_cards([
        ("মিউকাস পলিপাস", "Mucus Polyps · সবচেয়ে সাধারণ ধরন। মূলত এলার্জি এবং কোল্ড এলার্জির কারণে মিউকাস মেমব্রেন ফুলে এই মাংস বৃদ্ধি পায়।"),
        ("ফাংগাল পলিপাস", "Fungal Polyps · সংক্রমণজনিত। ‘রাইনোস্পোরিডিয়াম সিবেরি’ (Rhinosporidium seeberi) নামক একটি বিশেষ ফাঙ্গাল ইনফেকশনের ফলে এটি হয়ে থাকে।"),
        ("নিউপ্লাস্টিক পলিপাস", "Neoplastic Polyps · জটিল প্রকৃতির। নাকের মধ্যে টিউমার বা ক্যান্সারের কারণে তৈরি হতে পারে। (আমাদের চিকিৎসার আওতাভুক্ত নয়)"),
    ], hi_last=True)
    + "<div></div>\n",
    5, "তিন ধরনের পলিপাস: মিউকাস, ফাংগাল আর নিউপ্লাস্টিক। মনে করিয়ে দিন, নিউপ্লাস্টিক পলিপাস আমাদের চিকিৎসার আওতাভুক্ত নয়।")

slides["symptoms"] = light("symptoms", "#F6F7F0",
    header("SYMPTOMS · লক্ষণ ম্যাপিং" + NOTE, "পলিপাসের", "লক্ষণ")
    + '<div style="display:flex;flex-direction:row;gap:32px;align-items:center">\n<div style="flex:1">\n'
    + grid_cards([
        ("নাক", "মাংস বৃদ্ধি পাওয়া, নাক ভরে যাওয়া, নাক বন্ধ হওয়া"),
        ("মাথা", "মাথার সামনের অংশে ভার ভার লাগা, প্রচণ্ড মাথা ব্যথা"),
        ("চোখ ও কান", "চোখে ঝাপসা দেখা, কানে ভোঁ ভোঁ শব্দ হওয়া"),
        ("ঘ্রাণ ও স্বাদ", "ঘ্রাণ নির্ণয়ের ক্ষমতা হারানো, খাবারে স্বাদ না পাওয়া"),
        ("শ্বাসপ্রশ্বাস", "শ্বাস নিতে কষ্ট বা হাঁসফাঁস হওয়া, ঘুমের মধ্যে নাক ডাকা"),
        ("অন্যান্য", "ঠান্ডা-সর্দি, হাঁচি, নাক থেকে রক্ত পড়া, চুলকানো"),
    ], cols=2)
    + "</div>\n"
    + f'<img src="{P_NOSTRIL}" alt="নাকের ছিদ্রে পলিপাস দেখা যাচ্ছে" style="width:600px;height:337px;object-fit:cover;border-radius:24px;border:6px solid #FFFFFF;box-shadow:0 20px 50px rgba(18,53,42,0.18)">\n'
    + "</div>\n",
    6, "পলিপাসের লক্ষণ ছয় জায়গায়: নাক, মাথা, চোখ ও কান, ঘ্রাণ ও স্বাদ, শ্বাসপ্রশ্বাস, আর অন্যান্য। এগুলো দিয়েই সচেতনতামূলক পোস্ট বানানো যায়।")

slides["history"] = light("history", "#EEF5EA",
    header("PATIENT HISTORY · প্রাথমিক রোগ নির্ণয়" + NOTE, "রোগীকে যে", "১১টি প্রশ্ন করতে হয়")
    + rows([
        "আপনার কি মাথা ব্যথা হয়?", "মাথার কোন অংশে ব্যথা করে (সামনে না পিছনে)?", "ঠান্ডা, সর্দি বা হাঁচি কি আছে?",
        "নাক বন্ধ হয় কি না?", "নাকে গন্ধ হয় কি না?", "ঘুমের মধ্যে নাক ডাকা আছে কি না?",
        "চোখে ঝাপসা দেখা হয় কি না?", "মাথার সামনের অংশে ভার ভার লাগে কি না?", "কোনো ড্রপ/স্প্রে ব্যবহার করছেন কি না?",
        "ইতিপূর্বে কখনো শ্বাসকষ্ট হয়েছে কি কখনো?", "কোনো প্রকার ঔষধ নাকে ব্যবহার হয়েছে কি না?",
    ], 1, cols=2, size=26)
    + '<p style="font-size:26px;line-height:1.45;color:#4A6358"><b style="color:#1F7A42">নিশ্চিতকরণের জন্য:</b> X-ray PNS/DNS, Serum IgE total</p>\n',
    7, "রোগীকে প্রথমে নেজাল স্পেকুলাম দিয়ে পরীক্ষা করে এই ১১টি প্রশ্ন করতে হয়। নিশ্চিত হওয়ার জন্য X-ray PNS/DNS আর Serum IgE total পরীক্ষা।")

method_cards = []
for i, (name, en, pts, hi) in enumerate([
    ("এসিড দিয়ে পুড়িয়ে দেওয়া", "Acid", ["নাকের মারাত্মক জ্বালা-যন্ত্রণা হয়", "ইনফেকশন বা ক্যান্সারের ঝুঁকি থাকে", "মানবদেহে ব্যবহার নিষিদ্ধ", "শুধু সামনের অংশ ক্লিয়ার হয়, তাই পুনরায় ফিরে আসে"], False),
    ("সার্জারি", "Surgery", ["খরচ বেশি এবং বিশ্রামের প্রয়োজন", "রক্তপাত হয় এবং ড্রেসিং করতে হয়", "দ্বিতীয়বার পলিপাস হওয়ার সম্ভাবনা থাকে"], False),
    ("ইনজেকশন", "Injections", ["মূলত এসিড ব্যবহার করা হয়", "বারবার ইনজেকশন দিতে হয় এবং এনেসথেসিয়া করতে হয়"], False),
    ("ন্যাচারাল ক্রিম", "Natural", ["কোনো ব্যথা বা জ্বালা-যন্ত্রণা নেই", "কোনো পার্শ্বপ্রতিক্রিয়া বা রক্তপাত হয় না", "১০-১৫ মিনিটে প্রয়োগ", "সাইনাসের রস পুরোপুরি ক্লিয়ার করে", "শিশু-বৃদ্ধ সকলের জন্য নিরাপদ"], True),
]):
    box = "background:#1F7A42" if hi else "background:#FFFFFF;border:1px solid #DCE6D6"
    tc, dc, ec = ("#FFFFFF", "#D7F0C2", "#F6B26B") if hi else ("#12352A", "#4A6358", "#B85A0C")
    items = "".join(f'<li>{p}</li>' for p in pts)
    method_cards.append(
        f'<div style="flex:1;{box};border-radius:24px;padding:28px 26px;display:flex;flex-direction:column;gap:12px">'
        f'<p style="font-size:24px;font-weight:700;letter-spacing:1px;color:{ec}">{en}</p>'
        f'<h3 style="font-size:34px;font-weight:700;line-height:1.2;color:{tc}">{name}</h3>'
        f'<ul style="font-size:25px;line-height:1.45;color:{dc}">{items}</ul></div>'
    )
slides["methods"] = light("methods", "#F6F7F0",
    header("COMPARISON · তুলনামূলক বিশ্লেষণ" + NOTE, "চিকিৎসা পদ্ধতির", "তুলনা")
    + '<div style="display:flex;flex-direction:row;gap:20px;align-items:stretch">\n' + "\n".join(method_cards) + "\n</div>\n<div></div>\n",
    8, "চারটি চিকিৎসা পদ্ধতির তুলনা: এসিড দিয়ে পুড়িয়ে দেওয়া, সার্জারি, ইনজেকশন, আর ন্যাচারাল ক্রিম। ক্রিম প্রয়োগের পদ্ধতি অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ শেখানো হবে।")

food = "".join(
    '<div style="background:#FFFFFF;border:1px solid #DCE6D6;border-top:6px solid #F28C28;border-radius:22px;padding:24px 28px;display:flex;flex-direction:column;gap:8px">'
    f'<p style="font-size:24px;font-weight:700;letter-spacing:1px;color:#B85A0C">{en}</p>'
    f'<h3 style="font-size:34px;font-weight:700;color:#12352A">{bn}</h3>'
    f'<p style="font-size:28px;line-height:1.45;color:#4A6358">{items}</p></div>\n'
    for bn, en, items in [
        ("ঠান্ডা ও দুগ্ধজাত", "COLD & DAIRY", "কলা, শসা, আইসক্রিম, দই, গরুর দুধ"),
        ("ভারী প্রোটিন", "HEAVY PROTEINS", "গরুর গোশত, হাঁসের গোশত, হাঁসের ডিম, সাধারণ ডিম, মসুর ডাল"),
        ("এলার্জিক শাক-সবজি", "ALLERGENIC VEG", "পুঁই শাক, কচু শাক, পাট শাক, বেগুন, কচু, লতি, মিষ্টি কুমড়া"),
        ("নির্দিষ্ট মাছ", "SPECIFIC FISH", "ইলিশ মাছ, চিংড়ি মাছ, পুঁটি মাছ, বোয়াল মাছ"),
    ]
)
slides["food"] = light("food", "#EEF5EA",
    header("DIET · খাদ্যাভ্যাস নির্দেশিকা" + NOTE, "চিকিৎসা পরবর্তী", "নিষিদ্ধ খাবার")
    + '<p style="font-size:30px;line-height:1.45;color:#4A6358">এলার্জি নিয়ন্ত্রণের জন্য নিচের খাবারগুলো বর্জনীয়:</p>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">\n' + food + "</div>\n",
    9, "চিকিৎসা পরবর্তী নিষিদ্ধ খাবার চার ভাগে: ঠান্ডা ও দুগ্ধজাত, ভারী প্রোটিন, এলার্জিক শাক-সবজি, আর নির্দিষ্ট মাছ।")

care_box = (
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:24px;padding:30px 34px;display:flex;flex-direction:column;gap:16px">'
    '<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:{c};border-radius:999px;padding:14px;display:flex"><x-icon name="{ic}" style="color:{fc};width:36px;height:36px"></x-icon></div>'
    '<h3 style="font-size:36px;font-weight:700;color:#12352A">{t}</h3></div>'
    '<ul style="font-size:28px;line-height:1.55;color:#4A6358">{li}</ul></div>'
)
slides["care"] = light("care", "#F6F7F0",
    header("PRECAUTIONS · সতর্কতা" + NOTE, "চিকিৎসা চলাকালীন", "ও প্রাথমিক সতর্কতা")
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n'
    + care_box.format(c="#2E9E5B", fc="#FFFFFF", ic="Warning", t="ঔষধ লাগানো অবস্থায় করণীয়", li="".join(f"<li>{x}</li>" for x in [
        "নাক হাত দিয়ে মোছা যাবে না", "নাক দিয়ে না নিয়ে মুখ দিয়ে শ্বাস নেওয়া ভালো", "হাঁচি আসলে নাকে না দিয়ে মুখ দিয়ে হাঁচি দিতে হবে",
        "মাথা হালকা ম্যাসেজ করা ভালো", "উভয় নাকের চিকিৎসা একসাথে না করে, ২ নাক আলাদা করা ভালো"]))
    + "\n"
    + care_box.format(c="#F28C28", fc="#3A1E05", ic="Clock", t="প্রথম ৩ দিনের বিশেষ পরামর্শ", li="".join(f"<li>{x}</li>" for x in [
        "হালকা তেঁতুল খাবেন", "লেবু খাওয়া সম্পূর্ণ নিষেধ", "নাকে কোনোভাবেই পানি দেওয়া যাবে না", "নাক সবসময় ভালোভাবে পরিষ্কার রাখতে হবে"]))
    + "\n</div>\n<div></div>\n",
    10, "চিকিৎসা চলাকালীন করণীয় আর প্রথম তিন দিনের বিশেষ পরামর্শ। রোগীকে এগুলো আগেই বুঝিয়ে দিতে হয়।")

tiles = "".join(
    f'<img src="{src}" alt="{alt}" style="flex:1;width:252px;height:343px;object-fit:contain;border-radius:16px;background:#FFFFFF;border:1px solid #DCE6D6">\n'
    for src, alt in TOOLS
)
slides["equipment"] = light("equipment", "#EEF5EA",
    header("EQUIPMENT · যন্ত্রপাতি" + NOTE, "পলিপাস চিকিৎসার", "প্রয়োজনীয় যন্ত্রপাতি")
    + '<div style="display:flex;flex-direction:row;gap:16px">\n' + tiles + "</div>\n"
    + note_pill("কোন যন্ত্র কীভাবে ব্যবহার করতে হয়, তা অফলাইন ট্রেনিং-এ হাতে-কলমে শেখানো হবে"),
    11, "পলিপাস চিকিৎসার যন্ত্রপাতি: নেজাল স্পেকুলাম, সার্জিক্যাল গ্লাভস, সার্জিক্যাল মাস্ক, লম্বা কটন বাড, হেডলাইট আর আর্টারি ফরসেপস। ব্যবহার শেখানো হবে অফলাইন ট্রেনিং-এ।")

slides["practical"] = light("practical", "#F6F7F0",
    header("PRACTICAL TRAINING · অফলাইন প্রশিক্ষণ", "অফলাইন ট্রেনিং-এ", "হাতে-কলমে যা শিখবেন")
    + '<div style="display:flex;flex-direction:row;gap:36px;align-items:stretch">\n'
      '<div style="flex:1;display:flex;flex-direction:column;gap:16px">\n'
    + rows([
        "নেজাল স্পেকুলাম দিয়ে রোগী পরীক্ষা",
        "ধাপে ধাপে ন্যাচারাল ক্রিম প্রয়োগ পদ্ধতি",
        "বয়স অনুযায়ী রোগীকে পরামর্শ",
        "যন্ত্রপাতির সঠিক ব্যবহার",
        "পলিপা কেয়ার কম্বো প্যাক দিয়ে সেবা শুরু",
    ], 1, size=29)
    + '<p style="font-size:28px;line-height:1.45;text-align:center;color:#FFFFFF;background:#1F7A42;border-radius:999px;padding:18px 32px">শিখে নিজেই <b>পলিপাস সেবা দিয়ে আয়</b> করার সুযোগ</p>\n'
      '<p style="font-size:26px;line-height:1.45;text-align:center;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:999px;padding:14px 28px">ফি: [ফি] · স্থান: [স্থান] · মেয়াদ: [সময়]</p>\n'
      "</div>\n"
      f'<img src="{COMBO}" alt="পলিপা কেয়ার কম্বো প্যাক: ৮টি আইটেম একসাথে" style="width:520px;height:650px;object-fit:contain;border-radius:20px">\n'
      "</div>\n",
    12, "এগুলো অনলাইনে শেখানো হবে না, শুধু অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ। পলিপা কেয়ার কম্বো প্যাকে একসাথে ৮টি আইটেম থাকে। প্রশিক্ষণ শেষে নিজেই পলিপাস সেবা দিয়ে আয় করার সুযোগ। ফি: [ফি], স্থান: [স্থান], মেয়াদ: [সময়]।")

slides["task"] = light("task", "#EEF5EA",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Book" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:46px;font-weight:800;line-height:1.3;color:#FFFFFF">নির্ভরযোগ্য তথ্যের ভিত্তিতে পলিপাস নিয়ে শিক্ষামূলক কনটেন্ট তৈরি ও প্রচার</p>\n</div>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>পোস্ট ১:</b> <span style="color:#4A6358">পলিপাসের লক্ষণ</span></p>\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>পোস্ট ২:</b> <span style="color:#4A6358">কোন খাবার এড়িয়ে চলবেন</span></p>\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>নোট:</b> <span style="color:#4A6358">আজকের বিষয় খাতায় লিখুন</span></p>\n</div>\n',
    13, "আজকের কাজ: নির্ভরযোগ্য তথ্যের ভিত্তিতে পলিপাস নিয়ে শিক্ষামূলক কনটেন্ট তৈরি ও প্রচার। যেমন লক্ষণ নিয়ে একটি, আর বর্জনীয় খাবার নিয়ে একটি পোস্ট। জমার শেষ সময়: [সময়]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · COMING NEXT</p>
<h2 style="{HEAD};font-size:96px;font-weight:800;line-height:1.15;text-align:center;color:#FFFFFF">একাদশ দিন: <span style="color:#A6D65A">Licuria Safe</span></h2>
<p style="font-size:36px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">প্রোডাক্ট পরিচিতি ও রিসেলিং</p>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(14)} / {num(TOTAL)}</p>
<aside>আগামীকাল একাদশ দিন: Licuria Safe। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "defense", "what", "sinus", "types", "symptoms", "history", "methods", "food", "care", "equipment", "practical", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-02T19:45:00Z"},
    "lists": "css",
    "title": "দশম দিন — পলিপাস",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "নাক, সাইনাস ও পলিপাসের প্রাথমিক ধারণা", "start": "cover"},
        "s2": {"description": "লক্ষণ, রোগীর হিস্ট্রি ও চিকিৎসা পদ্ধতির তুলনা", "start": "symptoms"},
        "s3": {"description": "খাদ্যাভ্যাস, সতর্কতা, যন্ত্রপাতি, প্রশিক্ষণ ও আজকের কাজ", "start": "food"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
