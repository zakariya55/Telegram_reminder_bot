import datetime
import time
import requests

BOT_TOKEN = "7539330695:AAElYvAvig5TkbD3xfUvs3EcOEkbIT3z7YM"
CHAT_ID = "@jakariya2025xrp"

reminders = {
    "05:30": "🌅 শুভ সকাল! নতুন দিনের ট্রেডিং প্রস্তুতি নাও।",
    "10:00": "🕙 সকালের ট্রেডিং সেশন শুরু করো এখন!",
    "15:00": "☀️ বিকেলের মার্কেট আপডেট দেখে অ্যাকশন নাও।",
    "20:30": "🌙 রাতের ট্রেডিং পর্যবেক্ষণ করো।",
    "23:00": "🛏️ ঘুমানোর আগে আজকের ট্রেডিং ডায়েরি লিখে ফেলো।",
}

def send_reminder(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def is_sunday_to_thursday():
    today = datetime.datetime.today().weekday()
    return today in [6, 0, 1, 2, 3]  # Sunday to Thursday

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if is_sunday_to_thursday() and now in reminders:
        send_reminder(reminders[now])
        time.sleep(60)  # avoid multiple sends in 1 minute
    time.sleep(10)
