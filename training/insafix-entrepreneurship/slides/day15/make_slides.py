"""Write the Day 15 (results review and future plan) slide files, same look as Days 1–14.

Built from the schedule's day 15 topics, its "১৫ দিনের মূল লক্ষ্য" and its closing
principle; there is no old deck for this day. Figures are bracketed placeholders.
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
_day14 = (HERE.parent / "day14" / "make_slides.py").read_text(encoding="utf-8")
exec(_day14.split("\nslides = {}")[0])

ROOT = HERE / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 11
LOGO_A = "/_blob/a508ca32b7af7a4ad8c253ab126d6ff1"
LOGO_I = "/_blob/64607c05f909b6a29a49729c54b97ca4"
ALLERGY = "/_blob/1cf5ec0a5717c83cdeb3a414eb14eca7"
COSTO = "/_blob/206ab300423f46681f934b5c8a571e90"
HIJAMA = "/_blob/5b0f68115f515110b54542e52801f9f6"
POLYP = "/_blob/351d1885dd2b976cb04861fc326eb6df"

slides = {}

cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
grid = (
    '<div style="position:absolute;left:1290px;top:100px;width:502px;display:grid;grid-template-columns:1fr 1fr;gap:14px">'
    + "".join(
        f'<img src="{src}" alt="{alt}" style="width:244px;height:244px;object-fit:cover;border-radius:20px;border:4px solid #FFFFFF;box-shadow:0 12px 30px rgba(18,53,42,0.16)">'
        for src, alt in [(ALLERGY, "Allergy Clean প্রোডাক্টের ছবি"), (HIJAMA, "পিঠে কাপ বসিয়ে হিজামা"),
                         (POLYP, "পলিপা কেয়ার কম্বো প্যাক"), (COSTO, "Costo Clear প্রোডাক্টের ছবি")]
    )
    + "</div>"
)
img_start = cover.index(f'<img src="{U_SET}"')
img_end = cover.index(">", img_start) + 1
cover = cover[:img_start] + grid + cover[img_end:]
for a, b in [
    (LOGO_ALINSAF, LOGO_A),
    (LOGO_INSAFIX, LOGO_I),
    ("left:1220px;top:440px;width:200px;height:200px;border-radius:50%", "left:1180px;top:500px;width:200px;height:200px;border-radius:50%"),
    (">DAY 08<", ">DAY 15<"),
    ("হিজামা · প্রথম ক্লাস", "শেষ ক্লাস · Final Review"),
    ('<h1 style="{HEAD};font-size:100px;'.replace("{HEAD}", HEAD), f'<h1 style="{HEAD};font-size:84px;'),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'ফলাফল পর্যালোচনা ও<br><span style="color:#1F8A4C">ভবিষ্যৎ পরিকল্পনা</span>'),
    (">০৮<", ">১৫<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Chart" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ফলাফল<br><span style="color:#1F7A42">মূল্যায়ন</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Star" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ভবিষ্যৎ<br><span style="color:#1F7A42">লক্ষ্য</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="Trust" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">একসাথে<br><span style="color:#1F7A42">পথচলা</span>'),
    ('<b style="color:#B85A0C">খাতা-কলম নিন:</b> আজকের প্রতিটি বিষয় নোট করে রাখুন',
     '<b style="color:#B85A0C">সাথে রাখুন:</b> গতকালের রিপোর্ট ও ৩০ দিনের পরিকল্পনা'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>১৫ দিনের প্রশিক্ষণের শেষ ক্লাস। আজ ১৫ দিনের কাজ ও দক্ষতার মূল্যায়ন, মার্কেটিং ও রিসেলিংয়ের অগ্রগতি, ভবিষ্যৎ লক্ষ্য, প্র্যাকটিক্যাল প্রশিক্ষণ আর Al-Insaf Life Care-এর সঙ্গে সামনে কাজ করার সুযোগ নিয়ে কথা হবে।" + cover[b:]
slides["cover"] = cover

days = [
    ("১", "Al-Insaf পরিচিতি ও ফেসবুক সেটআপ"), ("২", "AI দিয়ে মার্কেটিং কনটেন্ট"), ("৩", "ডিজিটাল মার্কেটিং ও রিসেলিং"),
    ("৪", "Allergy Clean"), ("৫", "Smart Body Halua"), ("৬", "Sultani Halua ও Lion Man"),
    ("৭", "সেলস পরিস্থিতি ও কৌশল"), ("৮", "হিজামা: প্রথম ক্লাস"), ("৯", "হিজামা: দ্বিতীয় ক্লাস"),
    ("১০", "পলিপাস"), ("১১", "Leucorrhea Safe"), ("১২", "Costo Clear"),
    ("১৩", "হিজামা: তৃতীয় ক্লাস"), ("১৪", "সেলস রিভিউ ও হিসাব"), ("১৫", "ফলাফল ও ভবিষ্যৎ"),
]
day_cells = "".join(
    f'<div style="background:{"#1F7A42" if n == "১৫" else "#FFFFFF"};border:1px solid #DCE6D6;border-radius:16px;padding:14px 18px;display:flex;flex-direction:row;gap:14px;align-items:center">'
    f'<p style="{HEAD};font-size:28px;font-weight:800;color:{"#3A1E05" if n == "১৫" else "#FFFFFF"};background:{"#F28C28" if n == "১৫" else "#2E9E5B"};border-radius:999px;padding:2px 14px">{n}</p>'
    f'<p style="font-size:26px;font-weight:600;line-height:1.3;color:{"#FFFFFF" if n == "১৫" else "#12352A"}">{t}</p></div>\n'
    for n, t in days
)
slides["journey"] = light("journey", "#EEF5EA",
    header("RECAP · ১৫ দিনের যাত্রা", "১৫ দিনে আমরা", "যা শিখেছি")
    + '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px 18px">\n' + day_cells + "</div>\n",
    2, "পুরো ১৫ দিনের এক নজরে সারসংক্ষেপ: মার্কেটিং ও রিসেলিং, ছয়টি প্রোডাক্ট, সেলস কৌশল, হিজামা ও পলিপাসের হেলথ সেবা, আর ব্যবসার হিসাব।")

slides["skills"] = light("skills", "#F6F7F0",
    header("SELF ASSESSMENT · দক্ষতার মূল্যায়ন" + NOTE, "নিজেকে নম্বর দিন:", "আমার দক্ষতা কতটুকু?")
    + table(["দক্ষতা", "শুরুতে (১-৫)", "এখন (১-৫)"], [
        ["ফেসবুক প্রোফাইল ও পেজ", "[__]", "[__]"],
        ["AI দিয়ে কনটেন্ট তৈরি", "[__]", "[__]"],
        ["৬টি প্রোডাক্ট সম্পর্কে জ্ঞান", "[__]", "[__]"],
        ["কাস্টমারের সাথে কথা ও বিক্রি", "[__]", "[__]"],
        ["কাস্টমার ফলোআপ", "[__]", "[__]"],
        ["অর্ডার ও লাভের হিসাব", "[__]", "[__]"],
    ], [56, 22, 22], size=29)
    + "<div></div>\n",
    3, "প্রত্যেকে নিজেকে ১ থেকে ৫ নম্বর দেবেন: প্রশিক্ষণের শুরুতে কেমন ছিলেন, আর এখন কেমন। যেখানে নম্বর কম, সেটাই সামনে শেখার জায়গা।")

stat = "".join(
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:26px;padding:32px 24px;display:flex;flex-direction:column;align-items:center;gap:8px">'
    f'<p style="{HEAD};font-size:84px;font-weight:800;line-height:1;color:#1F8A4C">{v}</p>'
    f'<h3 style="font-size:32px;font-weight:700;text-align:center">{t}</h3></div>\n'
    for v, t in [("[__]", "মোট পোস্ট"), ("[__]", "মোট অর্ডার"), ("৳[__]", "মোট বিক্রয়"), ("[__]", "রিপিট কাস্টমার")]
)
slides["progress"] = light("progress", "#EEF5EA",
    header("PROGRESS · মার্কেটিং ও রিসেলিং" + NOTE, "১৫ দিনে আমার", "মার্কেটিং ও রিসেলিং")
    + '<div style="display:flex;flex-direction:row;gap:22px">\n' + stat + "</div>\n"
    + note_pill("১৫ দিনের লক্ষ্য ছিল: প্রত্যেক সদস্যের অন্তত ১–২টি বিক্রি। আপনার লক্ষ্য পূরণ হয়েছে কি?", dark=True),
    4, "প্রত্যেকে নিজের ১৫ দিনের সংখ্যা বলবেন: পোস্ট, অর্ডার, বিক্রয় আর রিপিট কাস্টমার। লক্ষ্য ছিল প্রত্যেকের অন্তত ১ থেকে ২টি বিক্রি।")

goals = [("৩ মাসে", "[মাসে __টি অর্ডার, __জন নিয়মিত কাস্টমার]"), ("৬ মাসে", "[নিজের পেজে __ ফলোয়ার, একটি সেবা চালু]"),
         ("১ বছরে", "[নিজের হেলথ ব্যবসা / হিজামা বা পলিপাস সেবা]")]
goal_cards = "".join(
    f'<div style="flex:1;background:{"#1F7A42" if i == 2 else "#FFFFFF"};border:1px solid #DCE6D6;border-radius:28px;padding:36px 32px;display:flex;flex-direction:column;gap:16px">'
    f'<p style="{HEAD};font-size:56px;font-weight:800;color:{"#A6D65A" if i == 2 else "#1F8A4C"}">{t}</p>'
    f'<p style="font-size:30px;line-height:1.5;color:{"#D7F0C2" if i == 2 else "#4A6358"}">{d}</p></div>\n'
    for i, (t, d) in enumerate(goals)
)
slides["goals"] = light("goals", "#F6F7F0",
    header("FUTURE GOALS · ভবিষ্যৎ লক্ষ্য" + NOTE, "নিজের ভবিষ্যৎ", "লক্ষ্য নির্ধারণ")
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n' + goal_cards + "</div>\n"
    + note_pill("লক্ষ্য লিখে রাখুন, সংখ্যায় লিখুন, আর প্রতি মাসে মিলিয়ে দেখুন।"),
    5, "প্রত্যেকে তিনটি সময়ের লক্ষ্য লিখবেন: ৩ মাস, ৬ মাস আর ১ বছর। বন্ধনীর লেখা শুধু উদাহরণ, নিজের সংখ্যা নিজে বসাবেন।")

svc = "".join(
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:28px;padding:18px 18px 28px;display:flex;flex-direction:column;gap:16px">'
    f'<img src="{src}" alt="{alt}" style="width:772px;height:330px;object-fit:{fit};border-radius:20px;background:#FFFFFF">'
    f'<h3 style="font-size:40px;font-weight:700;padding:0 12px">{t}</h3>'
    f'<p style="font-size:28px;line-height:1.45;color:#4A6358;padding:0 12px">{d}</p></div>\n'
    for src, alt, fit, t, d in [
        (HIJAMA, "পিঠে কাপ বসিয়ে হিজামা", "cover", "হিজামা", "অনলাইনে তিনটি ক্লাসে শিখেছেন তত্ত্ব; ধাপে ধাপে পদ্ধতি, স্ক্র্যাচ, সুন্নাহ পয়েন্ট শিখবেন অফলাইনে"),
        (POLYP, "পলিপা কেয়ার কম্বো প্যাক", "contain", "পলিপাস", "লক্ষণ, ধরন ও সতর্কতা শিখেছেন; রোগী পরীক্ষা ও ক্রিম প্রয়োগ শিখবেন অফলাইনে"),
    ]
)
slides["practical"] = light("practical", "#EEF5EA",
    header("PRACTICAL TRAINING · প্র্যাকটিক্যাল প্রশিক্ষণ", "হিজামা ও পলিপাসের", "প্র্যাকটিক্যাল প্রশিক্ষণ")
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n' + svc + "</div>\n"
    + '<div style="display:flex;flex-direction:row;gap:18px">\n'
      '<p style="flex:1;font-size:28px;line-height:1.45;text-align:center;color:#FFFFFF;background:#1F7A42;border-radius:999px;padding:16px 32px">হাতে-কলমে শিখে নিজেই <b>সেবা দিয়ে আয়</b> করার সুযোগ</p>\n'
      '<p style="font-size:28px;line-height:1.45;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:999px;padding:16px 32px">ফি · স্থান · মেয়াদ: [__]</p>\n'
      "</div>\n",
    6, "হিজামা ও পলিপাস: অনলাইনে তত্ত্ব শিখেছেন, হাতে-কলমে পুরো পদ্ধতি শেখানো হবে অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ। প্রশিক্ষণ শেষে নিজেই সেবা দিয়ে আয় করা যায়। ফি, স্থান ও মেয়াদ: [বসাতে হবে]।")

paths = [("Chart", "রিসেলিং চালিয়ে যাওয়া", "৬টি প্রোডাক্ট নিয়ে নিয়মিত মার্কেটিং ও বিক্রি"),
         ("GraduationCap", "হিজামা প্রশিক্ষণ", "অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ ভর্তি"),
         ("Activity", "পলিপাস প্রশিক্ষণ", "অফলাইন প্র্যাকটিক্যাল ট্রেনিং-এ ভর্তি"),
         ("Users", "পরবর্তী ব্যাচ / কোর্স", "[পরবর্তী প্রশিক্ষণের তথ্য]")]
slides["next"] = light("next", "#F6F7F0",
    header("NEXT STEPS · পরবর্তী পরিকল্পনা" + NOTE, "পরবর্তী প্রশিক্ষণ ও", "ব্যবসায়িক কার্যক্রম")
    + cards(paths)
    + note_pill("একটি বা একাধিক পথ বেছে নিন: যেটা বেছে নেবেন, তার জন্য আজই প্রথম পদক্ষেপ নিন।"),
    7, "সামনে চারটি পথ: রিসেলিং চালিয়ে যাওয়া, হিজামা প্রশিক্ষণ, পলিপাস প্রশিক্ষণ, আর পরবর্তী ব্যাচ বা কোর্স। পরবর্তী প্রশিক্ষণের তথ্য: [বসাতে হবে]।")

col = (
    '<div style="flex:1;background:{bg};border:1px solid #DCE6D6;border-radius:28px;padding:34px 36px;display:flex;flex-direction:column;gap:18px">'
    '<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:{ib};border-radius:999px;padding:14px;display:flex"><x-icon name="{ic}" style="color:{ifc};width:36px;height:36px"></x-icon></div>'
    '<h3 style="font-size:40px;font-weight:700;color:{tc}">{t}</h3></div>'
    '<ul style="font-size:29px;line-height:1.6;color:{lc}">{li}</ul></div>'
)
slides["together"] = light("together", "#EEF5EA",
    header("WORK WITH US · Al-Insaf Life Care", "Al-Insaf-এর সঙ্গে কাজ:", "সুযোগ ও দায়িত্ব")
    + '<div style="display:flex;flex-direction:row;gap:24px;align-items:stretch">\n'
    + col.format(bg="#1F7A42", ib="#FFFFFF", ic="Star", ifc="#1F7A42", tc="#FFFFFF", lc="#D7F0C2", t="সুযোগ", li="".join(f"<li>{x}</li>" for x in [
        "বিনা অগ্রিম বিনিয়োগে রিসেলিং (প্রযোজ্য শর্ত অনুযায়ী)", "৬টি প্রোডাক্ট নিয়ে বিক্রি ও আয়", "হিজামা ও পলিপাসের প্র্যাকটিক্যাল প্রশিক্ষণ", "[অন্যান্য সুযোগ]"]))
    + "\n"
    + col.format(bg="#FFFFFF", ib="#F28C28", ic="Verified", ifc="#3A1E05", tc="#12352A", lc="#4A6358", t="দায়িত্ব", li="".join(f"<li>{x}</li>" for x in [
        "কাস্টমারকে সঠিক ও যাচাইকৃত তথ্য দেওয়া", "রোগ সেরে যাওয়ার নিশ্চয়তা না দেওয়া", "কাস্টমারের সাথে সততা ও নিয়মিত ফলোআপ", "নিয়মিত কাজের রিপোর্ট দেওয়া"]))
    + "\n</div>\n<div></div>\n",
    8, "Al-Insaf Life Care-এর সঙ্গে কাজের সুযোগ আর দায়িত্ব। অন্যান্য সুযোগ থাকলে বসিয়ে নিন: [বসাতে হবে]।")

slides["principle"] = statement("principle", "আমাদের মূল নীতি · OUR PRINCIPLE", "প্রতিদিন শিখব, প্রতিদিন কাজ করব", "",
    "দক্ষতা তৈরি করব এবং বাস্তব অভিজ্ঞতার মাধ্যমে সামনে এগিয়ে যাব।", 9,
    "আমাদের মূল নীতি: প্রতিদিন শিখব, প্রতিদিন কাজ করব, দক্ষতা তৈরি করব এবং বাস্তব অভিজ্ঞতার মাধ্যমে সামনে এগিয়ে যাব।")

slides["task"] = light("task", "#F6F7F0",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="CheckCircle" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">নিজের অগ্রগতি পর্যালোচনা করে পরবর্তী ধাপ সম্পর্কে সিদ্ধান্ত নেওয়া</p>\n</div>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>পর্যালোচনা:</b> <span style="color:#4A6358">দক্ষতার নম্বর ও ১৫ দিনের ফলাফল</span></p>\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>সিদ্ধান্ত:</b> <span style="color:#4A6358">কোন পথে এগোবেন, গ্রুপে জানান</span></p>\n</div>\n',
    10, "শেষ টাস্ক: নিজের অগ্রগতি পর্যালোচনা করে পরবর্তী ধাপ সম্পর্কে সিদ্ধান্ত নেওয়া, আর সিদ্ধান্তটা গ্রুপে জানানো। জমার শেষ সময়: [সময়]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:30px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">১৫ দিনের প্রশিক্ষণ সম্পন্ন</p>
<h2 style="{HEAD};font-size:110px;font-weight:800;line-height:1.1;text-align:center;color:#FFFFFF">অভিনন্দন ও <span style="color:#A6D65A">ধন্যবাদ</span></h2>
<p style="font-size:34px;line-height:1.45;text-align:center;color:#D7E8DD;width:1300px">শেখা এখানেই শেষ নয়, আজ থেকে শুরু বাস্তবে কাজ করার পথচলা।</p>
<hr style="border-top:3px solid #F28C28;width:160px">
<div style="display:flex;flex-direction:row;gap:20px;align-items:center">
<div style="background:#FFFFFF;border-radius:20px;padding:10px 22px;display:flex;flex-direction:row;gap:14px;align-items:center"><img src="{LOGO_A}" alt="আল-ইনসাফ লাইফ কেয়ার লোগো" style="width:62px;height:80px;object-fit:contain"><p style="font-size:26px;font-weight:700;line-height:1.15;color:#0E3B2C">Al-Insaf<br><span style="color:#C2620A">Life Care</span></p></div>
<div style="background:#FFFFFF;border-radius:20px;padding:10px 22px;display:flex;flex-direction:row;gap:14px;align-items:center"><img src="{LOGO_I}" alt="ইনসাফিক্স একাডেমি লোগো" style="width:80px;height:80px;object-fit:contain"><p style="font-size:26px;font-weight:700;line-height:1.15;color:#0E3B2C">Insafix<br><span style="color:#1597B8">Academy</span></p></div>
</div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(11)} / {num(TOTAL)}</p>
<aside>১৫ দিনের প্রশিক্ষণ শেষ। সবাইকে অভিনন্দন ও ধন্যবাদ জানান। যোগাযোগ: +880 1332-140494।</aside>
</section>
"""

order = ["cover", "journey", "skills", "progress", "goals", "practical", "next", "together", "principle", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-06T14:20:00Z"},
    "lists": "css",
    "title": "পঞ্চদশ দিন — ফলাফল পর্যালোচনা ও ভবিষ্যৎ পরিকল্পনা",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "১৫ দিনের কাজ, দক্ষতা ও বিক্রির মূল্যায়ন", "start": "cover"},
        "s2": {"description": "ভবিষ্যৎ লক্ষ্য, প্র্যাকটিক্যাল প্রশিক্ষণ ও পরবর্তী পরিকল্পনা", "start": "goals"},
        "s3": {"description": "Al-Insaf-এর সঙ্গে কাজ, মূল নীতি ও শেষ টাস্ক", "start": "together"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
