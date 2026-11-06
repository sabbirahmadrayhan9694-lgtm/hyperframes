"""Write the Day 14 (sales review, follow-up and business accounts) slide files, same look as Days 1–13.

Built from the schedule's day 14 topics; there is no old deck for this day.
Every figure is a bracketed placeholder for the learners to fill in.
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
LOGO_A = "/_blob/b93f068641ca76f896746dcbaf426ecf"
LOGO_I = "/_blob/d61dc6f81cc79430384b147a10dd0aaf"
PRODUCTS = [
    ("/_blob/dac64a2cbb92ae33da2bd4db9e275ff0", "Allergy Clean"),
    ("/_blob/0809df2fbb5cbc9182203110cdae76ad", "Smart Body Halua"),
    ("/_blob/112545abebc6608907f988eb319a6262", "Lion Man"),
    ("/_blob/89a7993719b97bc81bb58149804d4cd9", "Sultani Halua"),
    ("/_blob/9690ebe74fd16ad24eda16b46a0a851f", "Leucorrhea Safe"),
    ("/_blob/1663dd124cdc7b3f32c4e4712a67eae8", "Costo Clear"),
]


def table(head, rows_, widths, size=28, width=1664):
    th = "".join(f'<th style="width:{w}%;text-align:left">{h}</th>' for h, w in zip(head, widths))
    body = "".join(
        f'<tr style="background:{"#FFFFFF" if i % 2 == 0 else "#F3F7F0"}">' + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
        for i, r in enumerate(rows_)
    )
    return (
        f'<table style="width:{width}px;font-size:{size}px;color:#12352A;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px">'
        f'<tr style="background:#1F7A42;color:#FFFFFF">{th}</tr>{body}</table>\n'
    )


slides = {}

cover = (HERE.parent / "day8" / "project" / "slides" / "cover.html").read_text(encoding="utf-8")
grid = (
    '<div style="position:absolute;left:1290px;top:100px;width:502px;display:grid;grid-template-columns:1fr 1fr;gap:14px">'
    + "".join(
        f'<img src="{src}" alt="{name} প্রোডাক্টের ছবি" style="width:244px;height:244px;object-fit:cover;border-radius:20px;border:4px solid #FFFFFF;box-shadow:0 12px 30px rgba(18,53,42,0.16)">'
        for src, name in [PRODUCTS[0], PRODUCTS[1], PRODUCTS[4], PRODUCTS[5]]
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
    (">DAY 08<", ">DAY 14<"),
    ("হিজামা · প্রথম ক্লাস", "Sales Review · Follow-up · Accounts"),
    ('<h1 style="{HEAD};font-size:100px;'.replace("{HEAD}", HEAD), f'<h1 style="{HEAD};font-size:84px;'),
    ('হিজামা ও কাপিং-এর<br><span style="color:#1F8A4C">প্রাথমিক আলোচনা</span>', 'সেলস রিভিউ, ফলোআপ<br><span style="color:#1F8A4C">ও ব্যবসার হিসাব</span>'),
    (">০৮<", ">১৪<"),
    ('name="Book" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">পরিচিতি<br><span style="color:#1F7A42">ও ধরন</span>',
     'name="Chart" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">অগ্রগতি<br><span style="color:#1F7A42">যাচাই</span>'),
    ('name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">ইতিহাস<br><span style="color:#1F7A42">ও হাদিস</span>',
     'name="Users" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">কাস্টমার<br><span style="color:#1F7A42">ফলোআপ</span>'),
    ('name="Activity" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">রোগের<br><span style="color:#1F7A42">চিকিৎসা</span>',
     'name="Database" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">লাভের<br><span style="color:#1F7A42">হিসাব</span>'),
    ('<b style="color:#B85A0C">খাতা-কলম নিন:</b> আজকের প্রতিটি বিষয় নোট করে রাখুন',
     '<b style="color:#B85A0C">সাথে রাখুন:</b> আপনার পোস্ট, মেসেজ ও অর্ডারের হিসাব'),
]:
    assert cover.count(a) == 1, a[:60]
    cover = cover.replace(a, b)
a = cover.index("<aside>")
b = cover.index("</aside>")
cover = cover[:a] + "<aside>চতুর্দশ দিন। আজ গত দিনগুলোর মার্কেটিং ও বিক্রির অগ্রগতি দেখবো, কাস্টমার ফলোআপ ও অর্ডার ব্যবস্থাপনা শিখবো, বিক্রয়-খরচ-লাভের হিসাব করবো, আর সামনের পরিকল্পনা করবো। সবাইকে নিজের পোস্ট, মেসেজ আর অর্ডারের হিসাব সাথে রাখতে বলুন।" + cover[b:]
slides["cover"] = cover

journey = [("১-৩", "ফেসবুক, AI কনটেন্ট", "মার্কেটিং ও রিসেলিং"), ("৪-৬, ১১-১২", "৬টি প্রোডাক্ট", "চেনা ও বিক্রি"),
           ("৭", "সেলস কৌশল", "বিক্রির পরিস্থিতি"), ("৮-১০, ১৩", "হিজামা ও পলিপাস", "হেলথ সেবা")]
slides["journey"] = light("journey", "#EEF5EA",
    header("RECAP · ১৩ দিনের যাত্রা", "গত ১৩ দিনে", "আমরা যা শিখেছি")
    + cards([(d, t, s) for d, t, s in journey], icons=False, arrows=True)
    + note_pill("আজ দেখবো: শেখা থেকে বাস্তবে কতটা কাজ হয়েছে, আর কীভাবে আরও ভালো করা যায়।", dark=True),
    2, "গত ১৩ দিনের সারসংক্ষেপ: প্রথম তিন দিন ফেসবুক, AI কনটেন্ট, মার্কেটিং ও রিসেলিং। তারপর ছয়টি প্রোডাক্ট, সেলস কৌশল, আর হিজামা ও পলিপাসের হেলথ সেবা।")

tiles = "".join(
    '<div style="flex:1;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:22px;padding:14px;display:flex;flex-direction:column;align-items:center;gap:10px">'
    f'<img src="{src}" alt="{name} প্রোডাক্টের ছবি" style="width:226px;height:226px;object-fit:cover;border-radius:14px">'
    f'<p style="font-size:26px;font-weight:700;text-align:center">{name}</p>'
    '<p style="font-size:24px;color:#4A6358;text-align:center">বিক্রি: [__]টি</p></div>\n'
    for src, name in PRODUCTS
)
slides["products"] = light("products", "#F6F7F0",
    header("SALES REVIEW · বিক্রির অগ্রগতি" + NOTE, "কোন প্রোডাক্ট", "কতটি বিক্রি হলো?")
    + '<div style="display:flex;flex-direction:row;gap:16px">\n' + tiles + "</div>\n"
    + note_pill("যে প্রোডাক্ট বেশি চলছে, তার কারণ খুঁজুন; যেটা কম চলছে, তার জন্য নতুন কনটেন্ট বানান।"),
    3, "প্রত্যেকে নিজের হিসাব থেকে প্রতিটি প্রোডাক্টের বিক্রির সংখ্যা লিখবেন। কোনটা বেশি চলছে আর কেন, সেটা নিয়ে আলোচনা করুন।")

slides["progress"] = light("progress", "#EEF5EA",
    header("SALES REVIEW · অগ্রগতি যাচাই" + NOTE, "মার্কেটিং থেকে বিক্রি:", "আপনার হিসাব")
    + table(["ধাপ", "কী গুনবেন", "আপনার সংখ্যা"], [
        ["১. পোস্ট", "কতটি পোস্ট/ভিডিও দিয়েছেন", "[__]"],
        ["২. সাড়া", "কতজন মেসেজ বা কমেন্ট করেছেন", "[__]"],
        ["৩. অর্ডার", "কতটি অর্ডার পেয়েছেন", "[__]"],
        ["৪. ডেলিভারি", "কতটি অর্ডার পৌঁছেছে", "[__]"],
        ["৫. রিপিট", "কতজন আবার কিনেছেন", "[__]"],
    ], [22, 56, 22], size=29)
    + note_pill("কোন ধাপে সংখ্যা হঠাৎ কমে যাচ্ছে, সেখানেই আপনার সমস্যা।"),
    4, "পাঁচটি ধাপের সংখ্যা লিখুন: পোস্ট, সাড়া, অর্ডার, ডেলিভারি, রিপিট। যে ধাপে সংখ্যা হঠাৎ কমে যায়, সেখানেই কাজ করতে হবে।")

follow = [("Chat", "অর্ডারের দিন", "ধন্যবাদ ও ডেলিভারির সময় জানানো"), ("Home", "ডেলিভারির পরে", "প্রোডাক্ট ঠিকমতো পেয়েছেন কিনা"),
          ("Activity", "ব্যবহারের কয়েক দিন পর", "অভিজ্ঞতা ও প্রশ্ন জানা"), ("Clock", "শেষ হওয়ার আগে", "আবার অর্ডারের রিমাইন্ডার")]
slides["followup"] = light("followup", "#F6F7F0",
    header("FOLLOW-UP · কাস্টমার ফলোআপ" + NOTE, "কাস্টমার ফলোআপের", "৪টি সময়")
    + cards(follow, arrows=True)
    + note_pill("নতুন কাস্টমার খোঁজার চেয়ে পুরনো কাস্টমারকে ধরে রাখা সহজ, ফলোআপই রিপিট কাস্টমার তৈরি করে।"),
    5, "ফলোআপের চারটি সময়: অর্ডারের দিন, ডেলিভারির পরে, ব্যবহারের কয়েক দিন পর, আর প্রোডাক্ট শেষ হওয়ার আগে। ফলোআপই রিপিট কাস্টমার তৈরি করে।")

order_steps = [("১", "অর্ডার নেওয়া", "নাম, ঠিকানা, ফোন, প্রোডাক্ট"), ("২", "নিশ্চিত করা", "ফোনে কথা বলে কনফার্ম"),
               ("৩", "অর্ডার পাঠানো", "[Al-Insaf-এর অর্ডার প্রক্রিয়া]"), ("৪", "ডেলিভারি ও পেমেন্ট", "[ডেলিভারি ও পেমেন্ট পদ্ধতি]"),
               ("৫", "খাতায় তোলা", "প্রতিটি অর্ডারের রেকর্ড")]
slides["orders"] = light("orders", "#EEF5EA",
    header("ORDER MANAGEMENT · অর্ডার ব্যবস্থাপনা" + NOTE, "অর্ডার ব্যবস্থাপনার", "৫টি ধাপ")
    + cards(order_steps, icons=False, arrows=True)
    + note_pill("একটি অর্ডারও যেন হারিয়ে না যায়, প্রতিটি অর্ডার খাতায় বা মোবাইলে লিখে রাখুন।"),
    6, "অর্ডার ব্যবস্থাপনার পাঁচ ধাপ। তৃতীয় আর চতুর্থ ধাপে Al-Insaf-এর অর্ডার প্রক্রিয়া, ডেলিভারি ও পেমেন্ট পদ্ধতি বলে দিন: [বসাতে হবে]।")

slides["ledger"] = light("ledger", "#F6F7F0",
    header("ORDER BOOK · অর্ডার খাতা" + NOTE, "আপনার", "অর্ডার খাতা")
    + table(["তারিখ", "কাস্টমার", "ফোন", "প্রোডাক্ট", "দাম", "অবস্থা"], [
        ["[__]", "[নাম]", "[নম্বর]", "[প্রোডাক্ট]", "৳[__]", "ডেলিভারি হয়েছে"],
        ["[__]", "[নাম]", "[নম্বর]", "[প্রোডাক্ট]", "৳[__]", "পথে আছে"],
        ["[__]", "[নাম]", "[নম্বর]", "[প্রোডাক্ট]", "৳[__]", "ফলোআপ বাকি"],
        ["[__]", "[নাম]", "[নম্বর]", "[প্রোডাক্ট]", "৳[__]", "রিপিট অর্ডার"],
    ], [12, 18, 16, 22, 12, 20], size=27)
    + note_pill("এই ছয়টি ঘর থাকলেই যথেষ্ট: খাতা, এক্সেল বা গুগল শিট, যেটা সহজ।"),
    7, "অর্ডার খাতার ছয়টি ঘর: তারিখ, কাস্টমার, ফোন, প্রোডাক্ট, দাম আর অবস্থা। অবস্থার ঘর দেখেই বোঝা যাবে কার ফলোআপ বাকি।")

slides["formula"] = statement("formula", "ব্যবসার হিসাব · PROFIT", "লাভ = বিক্রয় − খরচ", "",
    "হিসাব না রাখলে বোঝা যায় না ব্যবসা আসলে লাভে চলছে নাকি লোকসানে।", 8,
    "লাভের সহজ সূত্র: লাভ সমান বিক্রয় বিয়োগ খরচ। হিসাব না রাখলে বোঝা যায় না ব্যবসা লাভে চলছে নাকি লোকসানে।")

slides["profit"] = light("profit", "#EEF5EA",
    header("ACCOUNTS · বিক্রয়, খরচ ও লাভ" + NOTE, "মাসের হিসাব:", "বিক্রয়, খরচ ও লাভ")
    + '<div style="display:flex;flex-direction:row;gap:32px;align-items:stretch">\n'
      '<div style="flex:1">\n'
    + table(["হিসাব", "টাকা"], [
        ["মোট বিক্রয়", "৳[__]"],
        ["প্রোডাক্টের ক্রয়মূল্য", "− ৳[__]"],
        ["ডেলিভারি খরচ", "− ৳[__]"],
        ["বিজ্ঞাপন / বুস্ট", "− ৳[__]"],
        ["মোবাইল, ইন্টারনেট, অন্যান্য", "− ৳[__]"],
    ], [64, 36], size=29, width=1190)
    + "</div>\n"
      '<div style="width:440px;background:#1F7A42;border-radius:28px;padding:40px 36px;display:flex;flex-direction:column;justify-content:center;gap:14px">'
      '<p style="font-size:28px;font-weight:700;letter-spacing:1px;color:#F6B26B">নিট লাভ</p>'
      f'<p style="{HEAD};font-size:96px;font-weight:800;line-height:1;color:#FFFFFF">৳[__]</p>'
      '<p style="font-size:26px;line-height:1.45;color:#D7F0C2">মোট বিক্রয় থেকে সব খরচ বাদ দিয়ে যা থাকে</p></div>\n'
      "</div>\n",
    9, "প্রত্যেকে নিজের মাসের হিসাব বসাবেন: মোট বিক্রয় থেকে প্রোডাক্টের ক্রয়মূল্য, ডেলিভারি, বিজ্ঞাপন আর অন্যান্য খরচ বাদ দিলে নিট লাভ।")

slides["problems"] = light("problems", "#F6F7F0",
    header("PROBLEMS · সমস্যা চিহ্নিত করা" + NOTE, "বিক্রির সাধারণ সমস্যা", "ও সমাধান")
    + table(["সমস্যা", "সম্ভাব্য সমাধান"], [
        ["পোস্টে সাড়া কম", "সমস্যা-ভিত্তিক কনটেন্ট, ভালো ছবি, নিয়মিত পোস্ট"],
        ["মেসেজ আসে, অর্ডার হয় না", "দ্রুত উত্তর, প্রশ্নের সঠিক জবাব, বিশ্বাস তৈরি"],
        ["দাম নিয়ে আপত্তি", "প্রোডাক্টের উপকার ও মান বুঝিয়ে বলা"],
        ["ডেলিভারিতে দেরি", "আগে থেকেই সঠিক সময় জানিয়ে রাখা"],
        ["রিপিট কাস্টমার নেই", "নিয়মিত ফলোআপ ও রিমাইন্ডার"],
    ], [38, 62], size=29)
    + "<div></div>\n",
    10, "বিক্রির পাঁচটি সাধারণ সমস্যা আর সমাধান। প্রত্যেককে জিজ্ঞেস করুন, তার সবচেয়ে বড় সমস্যা কোনটা।")

plan = [("পরের ৩০ দিনের লক্ষ্য", "[__]টি অর্ডার, [__]জন নতুন কাস্টমার"), ("নিয়মিত কনটেন্ট", "প্রতিদিন [__]টি পোস্ট বা ভিডিও"),
        ("সাপ্তাহিক ফলোআপ", "প্রতি সপ্তাহে সব কাস্টমারের খোঁজ"), ("হিসাব রাখা", "প্রতিদিন অর্ডার খাতা, মাস শেষে লাভের হিসাব"),
        ("দক্ষতা বাড়ানো", "হিজামা বা পলিপাসের অফলাইন প্র্যাকটিক্যাল ট্রেনিং"), ("একটি সমস্যা সমাধান", "এই মাসে সবচেয়ে বড় সমস্যাটি ঠিক করা")]
slides["plan"] = light("plan", "#EEF5EA",
    header("NEXT PLAN · ব্যবসায়িক পরিকল্পনা" + NOTE, "পরবর্তী ৩০ দিনের", "ব্যবসায়িক পরিকল্পনা")
    + grid_cards(plan, hi_last=True)
    + "<div></div>\n",
    11, "পরের ৩০ দিনের ছয়টি পরিকল্পনা। প্রত্যেকে নিজের লক্ষ্যের সংখ্যা নিজে বসাবেন।")

slides["task"] = light("task", "#F6F7F0",
    header("TODAY'S TASK · আজকের টাস্ক", "আজকের", "Task")
    + '<div style="background:#1F7A42;border-radius:28px;padding:40px 48px;display:flex;flex-direction:row;gap:28px;align-items:center">\n'
      '<div style="background:#FFFFFF;border-radius:999px;padding:22px;display:flex"><x-icon name="Chart" style="color:#1F7A42;width:56px;height:56px"></x-icon></div>\n'
      f'<p style="{HEAD};font-size:50px;font-weight:800;line-height:1.3;color:#FFFFFF">নিজের কাজের রিপোর্ট তৈরি এবং পরবর্তী বিক্রির পরিকল্পনা করা</p>\n</div>\n'
    + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>রিপোর্ট:</b> <span style="color:#4A6358">পোস্ট, সাড়া, অর্ডার, বিক্রয়, খরচ ও লাভ</span></p>\n'
      '<p style="font-size:28px;line-height:1.45;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:20px;padding:22px 28px"><b>পরিকল্পনা:</b> <span style="color:#4A6358">পরের ৩০ দিনের লক্ষ্য লিখে গ্রুপে দিন</span></p>\n</div>\n',
    12, "আজকের কাজ: নিজের কাজের রিপোর্ট তৈরি এবং পরবর্তী বিক্রির পরিকল্পনা। রিপোর্ট আর পরিকল্পনা গ্রুপে জমা দিন। জমার শেষ সময়: [সময়]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:128px 160px 160px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px">
{DARK_BG}
<p style="{HEAD};font-size:30px;font-weight:800;letter-spacing:3px;color:#3A1E05;background:#F28C28;padding:8px 32px;border-radius:999px">আগামীকাল · শেষ ক্লাস</p>
<h2 style="{HEAD};font-size:84px;font-weight:800;line-height:1.15;text-align:center;color:#FFFFFF">ফলাফল পর্যালোচনা<br><span style="color:#A6D65A">ও ভবিষ্যৎ পরিকল্পনা</span></h2>
<hr style="border-top:3px solid #F28C28;width:160px">
<p style="{HEAD};font-size:44px;font-weight:800;color:#A6D65A">আল ইনসাফ লাইফ কেয়ার</p>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.08);border:1px solid #2F5A47;border-radius:999px;padding:16px 40px"><x-icon name="Chat" style="color:#A6D65A;width:36px;height:36px"></x-icon><p style="font-size:34px;font-weight:700;color:#FFFFFF">+880 1332-140494</p></div>
<p style="position:absolute;right:128px;bottom:64px;width:200px;font-size:24px;font-weight:700;color:#9DB8AA;text-align:right">{num(13)} / {num(TOTAL)}</p>
<aside>আগামীকাল শেষ ক্লাস, পঞ্চদশ দিন: ফলাফল পর্যালোচনা ও ভবিষ্যৎ পরিকল্পনা। পরের ক্লাসের সময়: [তারিখ ও সময়]।</aside>
</section>
"""

order = ["cover", "journey", "products", "progress", "followup", "orders", "ledger", "formula", "profit", "problems", "plan", "task", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-06T14:00:00Z"},
    "lists": "css",
    "title": "চতুর্দশ দিন — সেলস রিভিউ ও ব্যবসার হিসাব",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "মার্কেটিং ও বিক্রির অগ্রগতি পর্যালোচনা", "start": "cover"},
        "s2": {"description": "কাস্টমার ফলোআপ ও অর্ডার ব্যবস্থাপনা", "start": "followup"},
        "s3": {"description": "বিক্রয়, খরচ ও লাভের হিসাব, সমস্যা ও পরিকল্পনা", "start": "formula"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
