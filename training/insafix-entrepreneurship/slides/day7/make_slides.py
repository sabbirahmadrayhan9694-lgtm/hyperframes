"""Write the Day 7 (sales situations and selling skills) slide files, same look as Days 1–6."""

import json
from pathlib import Path

# Reuse the Day 5 helpers (header, cards, statement, footer, backgrounds).
_day5 = (Path(__file__).parent.parent / "day5" / "make_slides.py").read_text(encoding="utf-8")
exec(_day5.split("slides = {}")[0])

ROOT = Path(__file__).parent / "project"
SL = ROOT / "slides"
SL.mkdir(parents=True, exist_ok=True)
TOTAL = 12
LOGO_ALINSAF = "/_blob/05511a6049f02924d5edebc0fefff5ea"
LOGO_INSAFIX = "/_blob/1423ed46c14882788fda52186237c753"


def pairs(rows, left_label, right_label):
    """Two-column rows: a situation on the left, the way to handle it on the right."""
    out = [
        '<div style="display:flex;flex-direction:column;gap:14px">',
        '<div style="display:flex;flex-direction:row;gap:20px;align-items:center">'
        f'<p style="width:560px;font-size:24px;font-weight:700;letter-spacing:1px;color:#B85A0C">{left_label}</p>'
        '<div style="width:44px"></div>'
        f'<p style="flex:1;font-size:24px;font-weight:700;letter-spacing:1px;color:#1F7A42">{right_label}</p></div>',
    ]
    for left, right in rows:
        out.append(
            '<div style="display:flex;flex-direction:row;gap:20px;align-items:center">'
            f'<p style="width:560px;font-size:29px;font-weight:700;line-height:1.35;color:#5A3510;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:18px;padding:18px 24px">{left}</p>'
            '<x-shape kind="arrow-right" style="background:#F28C28;width:44px;height:22px"></x-shape>'
            f'<p style="flex:1;font-size:28px;line-height:1.4;color:#12352A;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 24px">{right}</p></div>'
        )
    out.append("</div>\n")
    return "\n".join(out)


def checklist(items, two_cols=True):
    cols = "1fr 1fr" if two_cols else "1fr"
    parts = [f'<div style="display:grid;grid-template-columns:{cols};gap:12px">']
    for i, (title, sub) in enumerate(items):
        last = i == len(items) - 1
        border = "2px solid #F28C28" if last else "1px solid #DCE6D6"
        box = "#F28C28" if last else "#2E9E5B"
        parts.append(
            f'<div style="background:#FFFFFF;border-radius:16px;padding:16px 22px;display:flex;flex-direction:row;gap:18px;align-items:center;border:{border}">'
            f'<x-shape kind="rounded" style="background:#FFFFFF;border:3px solid {box};width:36px;height:36px"></x-shape>'
            f'<p style="font-size:28px;line-height:1.3"><b>{title}</b><br><span style="color:#4A6358">{sub}</span></p></div>'
        )
    parts.append("</div>\n")
    return "\n".join(parts)


def report_card():
    return """<div style="display:flex;flex-direction:column;gap:20px">
<div style="background:#1F7A42;border-radius:24px;padding:30px 36px;display:flex;flex-direction:column;gap:16px">
<h3 style="font-size:32px;font-weight:700;color:#FFFFFF">Group-এ Report দিন</h3>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><x-icon name="CheckCircle" style="color:#D7F0C2;width:40px;height:40px"></x-icon><p style="font-size:28px;color:#FFFFFF">কী সম্পন্ন করেছি</p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><x-icon name="Warning" style="color:#FFD3A1;width:40px;height:40px"></x-icon><p style="font-size:28px;color:#FFFFFF">কোথায় সমস্যা হয়েছে</p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><x-icon name="Chat" style="color:#D7F0C2;width:40px;height:40px"></x-icon><p style="font-size:28px;color:#FFFFFF">কোন বিষয়ে সাহায্য দরকার</p></div>
</div>
<div style="background:#FFF1E0;border-left:6px solid #F28C28;border-radius:12px;padding:18px 26px">
<p style="font-size:26px;line-height:1.45;color:#5A3510"><b>কাজ অসম্পূর্ণ?</b> সমস্যা চিহ্নিত করুন, পরের ক্লাসের আগে সমাধানের চেষ্টা করুন।</p>
</div>
</div>
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
<p style="{HEAD};font-size:28px;font-weight:800;color:#3A1E05;background:#F28C28;padding:6px 22px;border-radius:999px;letter-spacing:2px">DAY 07</p>
<p style="font-size:28px;font-weight:600;color:#4A6358;letter-spacing:1px">বিশেষ সেশন · Sales Skills</p>
</div>
<h1 style="{HEAD};font-size:100px;font-weight:800;line-height:1.1;color:#12352A">কথা থেকে অর্ডার:<br><span style="color:#1F8A4C">বিক্রির কৌশল</span></h1>
</div>
<div style="display:flex;flex-direction:row;gap:36px;align-items:center;width:1120px">
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="Chat" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">Talk<br><span style="color:#1F7A42">কথা বলা</span></p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="Trust" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">Handle<br><span style="color:#1F7A42">আপত্তি সামলানো</span></p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#2E9E5B;border-radius:999px;padding:16px;display:flex"><x-icon name="Clock" style="color:#FFFFFF;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">Follow-up<br><span style="color:#1F7A42">ফলোআপ</span></p></div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center"><div style="background:#F28C28;border-radius:999px;padding:16px;display:flex"><x-icon name="CheckCircle" style="color:#3A1E05;width:40px;height:40px"></x-icon></div><p style="font-size:28px;font-weight:700;line-height:1.15;color:#12352A">Close<br><span style="color:#B85A0C">বিক্রি সম্পন্ন</span></p></div>
</div>
<div style="display:flex;flex-direction:row;gap:18px;align-items:center;background:#FFFFFF;border:1px solid #CFE0C6;border-radius:999px;padding:14px 32px;width:1120px;box-shadow:0 6px 20px rgba(18,53,42,0.08)">
<x-icon name="CheckCircle" style="color:#2E9E5B;width:36px;height:36px"></x-icon>
<p style="font-size:28px;color:#12352A"><b style="color:#B85A0C">আজকের Goal:</b> আগের সম্ভাব্য ক্রেতাদের সঙ্গে ফলোআপ ও অর্ডার</p>
</div>
<div style="position:absolute;left:1370px;top:260px;width:420px;height:420px;border-radius:50%;border:6px solid #2E9E5B;background:#FFFFFF;box-shadow:0 20px 60px rgba(18,53,42,0.12);display:flex;flex-direction:column;align-items:center;justify-content:center">
<p style="{HEAD};font-size:56px;font-weight:800;letter-spacing:6px;color:#12352A">DAY</p>
<p style="{HEAD};font-size:200px;font-weight:800;line-height:1;color:#1F8A4C">০৭</p>
<p style="font-size:26px;font-weight:600;color:#B85A0C">Sales Skills</p>
</div>
<aside>সালাম দিয়ে শুরু করুন। গত তিন দিনে আমরা পণ্য চিনেছি, আজ শিখব সেই পণ্য নিয়ে মানুষের সঙ্গে কীভাবে কথা বলতে হয়, প্রশ্ন ও আপত্তি কীভাবে সামলাতে হয়, ফলোআপ কীভাবে করতে হয় আর অর্ডার কীভাবে নিতে হয়।</aside>
</section>
"""

slides["recap"] = light("recap", "#EEF5EA",
    header("RECAP · গত তিন দিন", "পণ্য চেনা", "শেষ")
    + cards([("Verified", "Allergy Clean", "Day 04"), ("Activity", "Smart Body Halua", "Day 05"), ("Lightning", "Lion Man", "Day 06"), ("Star", "Sultani Halua", "Day 06")])
    + '<div style="background:#1F7A42;border-radius:28px;padding:32px 48px;display:flex;flex-direction:row;gap:28px;align-items:center;justify-content:center">\n'
      f'<div style="display:flex;flex-direction:column;gap:4px;align-items:center"><p style="font-size:26px;color:#D7F0C2">এতদিন</p><p style="{HEAD};font-size:44px;font-weight:800;color:#FFFFFF">পণ্য জানা</p></div>\n'
      '<x-shape kind="arrow-right" style="background:#F6B26B;width:64px;height:32px"></x-shape>\n'
      f'<div style="display:flex;flex-direction:column;gap:4px;align-items:center"><p style="font-size:26px;color:#FFD3A1">আজ</p><p style="{HEAD};font-size:44px;font-weight:800;color:#FFFFFF">মানুষের কাছে বিক্রি</p></div>\n</div>\n',
    2, "গত তিন দিনে চারটি পণ্য চিনেছি: Allergy Clean, Smart Body Halua, Lion Man আর Sultani Halua। প্রতিদিন পর্যবেক্ষণের কাজও করেছেন। দুই-তিনজনকে জিজ্ঞেস করুন তাঁদের আশেপাশে কী দেখলেন। তারপর বলুন: পণ্য জানা হলো, এখন সেই জ্ঞান নিয়ে মানুষের কাছে যাওয়ার পালা।")

slides["journey"] = light("journey", "#F6F7F0",
    header("SALES JOURNEY · বিক্রির পথ", "বিক্রির", "৫টি ধাপ")
    + cards([("Chat", "কথা বলা", "Talk"), ("Trust", "প্রশ্ন ও আপত্তি", "Handle"), ("Clock", "ফলোআপ", "Follow-up"),
             ("PaperPlane", "অর্ডার নেওয়া", "Order"), ("CheckCircle", "বিক্রি সম্পন্ন", "Close")], arrows=True)
    + note_pill("প্রতিটি ধাপ ঠিকমতো হলে বিক্রি নিজে থেকেই আসে। তাড়াহুড়ো নয়, ধাপে ধাপে।", dark=True),
    3, "আজকের পুরো ক্লাস এই পাঁচটি ধাপ নিয়ে: কথা বলা, প্রশ্ন ও আপত্তি সামলানো, ফলোআপ, অর্ডার নেওয়া, আর বিক্রি সম্পন্ন করা। প্রতিটি ধাপ পরের স্লাইডগুলোতে আলাদা করে দেখব।")

slides["talk"] = light("talk", "#EEF5EA",
    header("STEP 1 · কাস্টমারের সঙ্গে কথা", "কথা বলার", "৪টি নিয়ম")
    + cards([("১", "সালাম ও খোঁজখবর", "সম্পর্ক আগে"), ("২", "প্রশ্ন করুন", "প্রয়োজন জানুন"), ("৩", "মন দিয়ে শুনুন", "বেশি শুনুন, কম বলুন"), ("৪", "সঠিক তথ্য দিন", "প্রয়োজন অনুযায়ী")], icons=False)
    + '<div style="display:flex;flex-direction:row;gap:16px;flex-wrap:wrap">\n'
      '<p style="font-size:27px;color:#12352A;background:#FFFFFF;border:1px solid #DCE6D6;padding:12px 26px;border-radius:999px">"আপনার পরিবারে কারও এমন সমস্যা আছে?"</p>\n'
      '<p style="font-size:27px;color:#12352A;background:#FFFFFF;border:1px solid #DCE6D6;padding:12px 26px;border-radius:999px">"আগে কী ব্যবহার করেছেন?"</p>\n'
      '<p style="font-size:27px;color:#12352A;background:#FFFFFF;border:1px solid #DCE6D6;padding:12px 26px;border-radius:999px">"কোন বিষয়টা আপনার কাছে জরুরি?"</p>\n</div>\n',
    4, "চারটি নিয়ম: প্রথমে সালাম ও খোঁজখবর, তারপর প্রশ্ন করে প্রয়োজন জানা, মন দিয়ে শোনা, আর প্রয়োজন অনুযায়ী পণ্যের সঠিক তথ্য দেওয়া। নিচের তিনটি প্রশ্ন উদাহরণ, প্রশিক্ষণার্থীদের নিজের ভাষায় বলতে বলুন। একটানা নিজে কথা বলে গেলে মানুষ আগ্রহ হারায়।")

slides["objections"] = light("objections", "#F6F7F0",
    header("STEP 2 · প্রশ্ন ও আপত্তি", "আপত্তি মানে না নয়,", "একটি প্রশ্ন")
    + pairs([
        ('"দাম বেশি"', "পণ্যের পরিমাণ ও মান বুঝিয়ে বলুন, জোর করবেন না"),
        ('"কাজ করবে তো?"', "নিশ্চয়তা নয়, সঠিক তথ্য দিন। প্রয়োজনে ডাক্তারের পরামর্শ নিতে বলুন"),
        ('"পরে নেব"', "সম্মান করুন, অনুমতি নিয়ে ফলোআপের দিন ঠিক করুন"),
        ('"অনলাইনে বিশ্বাস হয় না"', "নিজের পরিচয়, প্রোফাইল ও যোগাযোগ নম্বর দিন"),
    ], "ক্রেতা বলেন", "আপনি যা করবেন"),
    5, "চারটি সাধারণ আপত্তি আর সেগুলো সামলানোর উপায়। সবচেয়ে গুরুত্বপূর্ণ: \"কাজ করবে তো?\" প্রশ্নে কখনো নিশ্চয়তা বা রোগ সারানোর কথা দেবেন না। সঠিক তথ্য দিন আর প্রয়োজনে ডাক্তারের পরামর্শ নিতে বলুন। অন্য কোম্পানির পণ্যকে খারাপ বলবেন না।")

slides["followup"] = light("followup", "#EEF5EA",
    header("STEP 3 · ফলোআপ", "ফলোআপের", "নিয়ম")
    + cards([("১", "প্রথম কথা", "আজ"), ("২", "ফলোআপ ১", "[২] দিন পর"), ("৩", "ফলোআপ ২", "[৫] দিন পর"), ("৪", "ফলোআপ ৩", "[১০] দিন পর")], icons=False, arrows=True)
    + '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">\n'
      '<p style="font-size:27px;line-height:1.4;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 24px"><b>অনুমতি নিয়ে</b><br><span style="color:#4A6358">"কবে আবার খোঁজ নিলে সুবিধা?"</span></p>\n'
      '<p style="font-size:27px;line-height:1.4;background:#FFFFFF;border:1px solid #DCE6D6;border-radius:18px;padding:18px 24px"><b>প্রতিবার নতুন তথ্য</b><br><span style="color:#4A6358">শুধু "নেবেন?" নয়</span></p>\n'
      '<p style="font-size:27px;line-height:1.4;background:#FFF1E0;border:2px solid #F6D2A8;border-radius:18px;padding:18px 24px"><b>৩ বার সাড়া নেই?</b><br><span style="color:#5A3510">বিরতি দিন, সম্পর্ক রাখুন</span></p>\n</div>\n',
    6, "ফলোআপের সময়গুলো উদাহরণ, বন্ধনীর সংখ্যা আপনার মতো ঠিক করে নিন। মূল নিয়ম তিনটি: অনুমতি নিয়ে ফলোআপ, প্রতিবার কোনো নতুন উপকারী তথ্য, আর তিনবার সাড়া না পেলে বিরতি। প্রতিটি ফলোআপের পর ক্রেতার তালিকায় অবস্থা লিখে রাখুন।")

slides["order"] = light("order", "#F6F7F0",
    header("STEP 4 · অর্ডার নেওয়া", "অর্ডারের", "চেকলিস্ট")
    + checklist([("নাম ও ফোন", "সঠিক বানান ও নম্বর"), ("পূর্ণ ঠিকানা", "এলাকা ও কাছের চিহ্ন"), ("পণ্য ও পরিমাণ", "কোনটা, কয়টা"),
                 ("দাম ও ডেলিভারি চার্জ", "[দাম] · [চার্জ]"), ("পেমেন্ট পদ্ধতি", "[পদ্ধতি]"), ("আবার মিলিয়ে নিন", "ক্রেতাকে পড়ে শোনান")])
    + note_pill("অর্ডার নিশ্চিত হলে Al-Insaf-এর প্রক্রিয়া অনুযায়ী পাঠান (Day 03-এর ৬টি ধাপ)।", dark=True),
    7, "অর্ডার নেওয়ার সময় এই ছয়টি তথ্য অবশ্যই নিন। শেষে সব তথ্য ক্রেতাকে পড়ে শোনান, যাতে ভুল না হয়। দাম, ডেলিভারি চার্জ আর পেমেন্ট পদ্ধতির ঘরে Al-Insaf-এর আসল তথ্য বসাতে হবে।")

slides["close"] = light("close", "#EEF5EA",
    header("STEP 5 · বিক্রি সম্পন্ন", "বিক্রি শেষ করার", "৩টি কথা")
    + cards([("১", "সারাংশ বলুন", "\"তাহলে আপনার জন্য ১টি পাঠাচ্ছি\""), ("২", "সিদ্ধান্তের প্রশ্ন", "\"কবে ডেলিভারি নিলে সুবিধা?\""), ("৩", "ধন্যবাদ দিন", "পরের যোগাযোগ ঠিক করুন")], icons=False)
    + note_pill("বিক্রির পরেও খোঁজ নিন: ডেলিভারি পেয়েছেন কি না, ব্যবহার কেমন লাগছে। সন্তুষ্ট ক্রেতাই আবার কেনেন।"),
    8, "বিক্রি শেষ করতে তিনটি কথা: সারাংশ বলা, সিদ্ধান্তের প্রশ্ন করা, আর ধন্যবাদ দিয়ে পরের যোগাযোগ ঠিক করা। বিক্রির পরের খোঁজখবর সবচেয়ে বেশি গুরুত্বপূর্ণ, কারণ সন্তুষ্ট ক্রেতাই নিয়মিত ক্রেতা হন।")

slides["problems"] = light("problems", "#F6F7F0",
    header("COMMON PROBLEMS · সাধারণ সমস্যা", "বিক্রির সমস্যা ও", "সমাধান")
    + pairs([
        ("মেসেজ দেখেছে, উত্তর নেই", "১–২ দিন পর একবার ভদ্রভাবে খোঁজ নিন"),
        ("অর্ডার দিয়ে ফোন ধরছে না", "পাঠানোর আগে ফোনে অর্ডার নিশ্চিত করুন"),
        ("উত্তর জানি না এমন প্রশ্ন", "\"জেনে জানাচ্ছি\" বলুন, টিমের সাহায্য নিন"),
        ("নেতিবাচক মন্তব্য", "শান্ত থাকুন, তর্ক নয়, ভদ্র উত্তর দিন"),
    ], "সমস্যা", "সমাধান"),
    9, "চারটি সাধারণ সমস্যা আর সমাধান। প্রশিক্ষণার্থীদের জিজ্ঞেস করুন গত কয়েক দিনে তাঁরা কী কী সমস্যায় পড়েছেন, সেগুলোর সমাধান নিয়ে একসঙ্গে আলোচনা করুন।")

slides["roleplay"] = statement("roleplay", "ক্লাসেই অনুশীলন · ROLE-PLAY", "এবার করে দেখান", "দুজন মিলে অনুশীলন",
                               "একজন বিক্রেতা, একজন ক্রেতা। পরিস্থিতি ১: \"দাম বেশি\" · পরিস্থিতি ২: \"কাজ করবে তো?\" · পরিস্থিতি ৩: \"পরে নেব\"", 10,
                               "দুজন করে জোড়া বানান। একজন বিক্রেতা, একজন ক্রেতা। তিনটি পরিস্থিতি একে একে অনুশীলন করান। প্রতিটির পর অন্যরা মতামত দিক: কোনটা ভালো হয়েছে, কোথায় আরও ভালো করা যায়।")

slides["assignment"] = light("assignment", "#EEF5EA",
    header("TODAY'S ASSIGNMENT · শিখুন এবং করে দেখান", "আজকের Task:", "ফলোআপ")
    + '<div style="display:grid;grid-template-columns:1000px 624px;gap:40px;align-items:start">\n'
    + checklist([("ফলোআপ", "তালিকার [৫] জনের সঙ্গে"), ("অবস্থা আপডেট", "প্রতিটি নামের পাশে"), ("১টি আপত্তি", "আর আপনার উত্তর লিখুন"),
                 ("রোল-প্লে", "একজনের সঙ্গে অনুশীলন"), ("অর্ডার হলে", "চেকলিস্ট অনুযায়ী নিন"), ("Screenshot", "নাম ও নম্বর ঢেকে জমা")])
    + report_card()
    + "</div>\n",
    11, "আজকের কাজ: আগের দিনগুলোর সম্ভাব্য ক্রেতাদের সঙ্গে ফলোআপ। তালিকার কতজনের সঙ্গে ফলোআপ করবেন, সংখ্যাটা আপনার মতো ঠিক করে নিন: [৫] জন। রিপোর্ট জমার শেষ সময়: [সময়]। গ্রুপের নাম বা লিংক: [গ্রুপের নাম বা লিংক]।")

slides["closing"] = f"""<section id="closing" data-transition="fade" style="background:#12352A;color:#FFFFFF;{FONT};padding:112px 128px 160px;display:flex;flex-direction:column;justify-content:space-between">
{DARK_BG}
<div style="display:flex;flex-direction:column;gap:14px">
<p style="font-size:24px;font-weight:700;letter-spacing:2px;color:#F6B26B">THE JOURNEY AHEAD · সামনের পথ</p>
<h2 style="{HEAD};font-size:76px;font-weight:800;line-height:1.15;color:#FFFFFF">বিক্রির কৌশল শেখা হলো, <span style="color:#A6D65A">এবার স্বাস্থ্যসেবা</span></h2>
</div>
<div style="display:flex;flex-direction:row;gap:12px;align-items:start;justify-content:space-between">
<div style="width:250px;display:flex;flex-direction:column;gap:12px;align-items:center"><p style="{HEAD};font-size:28px;font-weight:800;color:#12352A;background:#A6D65A;padding:10px 26px;border-radius:999px">Day 1–6</p><p style="font-size:26px;font-weight:600;line-height:1.3;text-align:center;color:#D7F0C2">Profile থেকে পণ্য · শেষ</p></div>
<div style="padding-top:22px;display:flex"><x-shape kind="arrow-right" style="background:#4F7F68;width:40px;height:20px"></x-shape></div>
<div style="width:250px;display:flex;flex-direction:column;gap:12px;align-items:center"><p style="{HEAD};font-size:28px;font-weight:800;color:#3A1E05;background:#F28C28;padding:10px 26px;border-radius:999px">Day 7</p><p style="font-size:26px;font-weight:600;line-height:1.3;text-align:center;color:#FFFFFF">Sales Skills</p></div>
<div style="padding-top:22px;display:flex"><x-shape kind="arrow-right" style="background:#4F7F68;width:40px;height:20px"></x-shape></div>
<div style="width:250px;display:flex;flex-direction:column;gap:12px;align-items:center"><p style="{HEAD};font-size:28px;font-weight:800;color:#FFFFFF;border:2px solid #F6B26B;padding:8px 24px;border-radius:999px">Day 8</p><p style="font-size:26px;font-weight:600;line-height:1.3;text-align:center;color:#FFD3A1">হিজামা পরিচিতি</p></div>
<div style="padding-top:22px;display:flex"><x-shape kind="arrow-right" style="background:#4F7F68;width:40px;height:20px"></x-shape></div>
<div style="width:250px;display:flex;flex-direction:column;gap:12px;align-items:center"><p style="{HEAD};font-size:28px;font-weight:800;color:#FFFFFF;border:2px solid #4F7F68;padding:8px 24px;border-radius:999px">Day 9–13</p><p style="font-size:26px;font-weight:600;line-height:1.3;text-align:center;color:#D7F0C2">Health ও পণ্য</p></div>
<div style="padding-top:22px;display:flex"><x-shape kind="arrow-right" style="background:#4F7F68;width:40px;height:20px"></x-shape></div>
<div style="width:250px;display:flex;flex-direction:column;gap:12px;align-items:center"><p style="{HEAD};font-size:28px;font-weight:800;color:#FFFFFF;border:2px solid #4F7F68;padding:8px 24px;border-radius:999px">Day 14–15</p><p style="font-size:26px;font-weight:600;line-height:1.3;text-align:center;color:#D7F0C2">Review ও Future Plan</p></div>
</div>
<div style="display:flex;flex-direction:row;gap:16px;align-items:center;background:rgba(255,255,255,0.06);border:1px solid #2F5A47;border-radius:16px;padding:16px 28px">
<x-icon name="Lightbulb" style="color:#F6B26B;width:36px;height:36px"></x-icon>
<p style="font-size:26px;color:#D7E8DD"><b style="color:#FFFFFF">আগামীকাল:</b> হিজামা, প্রথম ক্লাস। স্বাস্থ্যসেবায় কাজের নতুন সুযোগ।</p>
</div>
<div style="display:flex;flex-direction:column;gap:16px">
<p style="font-size:26px;font-weight:700;letter-spacing:1px;color:#F6B26B">আমাদের ৩টি অঙ্গীকার</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">
<div style="background:#F6F7F0;border-radius:20px;padding:22px 28px;display:flex;flex-direction:row;gap:18px;align-items:center"><p style="{HEAD};font-size:52px;font-weight:800;color:#1F8A4C">১</p><p style="font-size:30px;font-weight:700;line-height:1.25;color:#12352A">প্রতিদিন শিখব</p></div>
<div style="background:#F6F7F0;border-radius:20px;padding:22px 28px;display:flex;flex-direction:row;gap:18px;align-items:center"><p style="{HEAD};font-size:52px;font-weight:800;color:#1F8A4C">২</p><p style="font-size:30px;font-weight:700;line-height:1.25;color:#12352A">বাস্তবে প্রয়োগ করব</p></div>
<div style="background:#F28C28;border-radius:20px;padding:22px 28px;display:flex;flex-direction:row;gap:18px;align-items:center"><p style="{HEAD};font-size:52px;font-weight:800;color:#3A1E05">৩</p><p style="font-size:30px;font-weight:700;line-height:1.25;color:#3A1E05">সৎভাবে Report করব</p></div>
</div>
</div>
<div style="position:absolute;left:128px;bottom:56px;width:1664px;display:flex;flex-direction:row;align-items:center;justify-content:space-between">
<p style="{HEAD};font-size:32px;font-weight:700;color:#A6D65A">ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি</p>
<p style="font-size:24px;font-weight:700;color:#9DB8AA">{num(12)} / {num(TOTAL)}</p>
</div>
<aside>আজকের সারাংশ: কথা বলা, আপত্তি সামলানো, ফলোআপ, অর্ডার আর বিক্রি সম্পন্ন করা। আগামীকাল থেকে স্বাস্থ্যসেবার অংশ শুরু, প্রথমে হিজামা। তিনটি অঙ্গীকার একসঙ্গে বলুন। পরের ক্লাসের সময় জানান: [তারিখ ও সময়]। দোয়া ও ধন্যবাদ দিয়ে শেষ করুন।</aside>
</section>
"""

order = ["cover", "recap", "journey", "talk", "objections", "followup", "order", "close", "problems", "roleplay", "assignment", "closing"]
for sid in order:
    (SL / f"{sid}.html").write_text(slides[sid], encoding="utf-8")

deck = {
    "v": 4,
    "createdOnFiles": {"v": 1, "at": "2026-11-02T09:00:00Z"},
    "lists": "css",
    "title": "সপ্তম দিন — সেলস পরিস্থিতি ও বিক্রির কৌশল",
    "cover": "cover",
    "order": order,
    "sections": {
        "s1": {"description": "পণ্য চেনা থেকে বিক্রির পথ", "start": "cover"},
        "s2": {"description": "কথা, আপত্তি, ফলোআপ, অর্ডার ও বিক্রি সম্পন্ন", "start": "talk"},
        "s3": {"description": "সমস্যা, অনুশীলন, আজকের কাজ ও সামনের পথ", "start": "problems"},
    },
    "faces": {
        "baloo-da-2": {"family": "Baloo Da 2", "href": "https://fonts.googleapis.com/css2?family=Baloo+Da+2:wght@500..800&display=swap"},
        "hind-siliguri": {"family": "Hind Siliguri", "href": "https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(order), "slides")
