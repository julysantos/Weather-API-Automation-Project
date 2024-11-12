import schedule
import time
import requests
from datetime import datetime
from plyer import notification

def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/today")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            return f"Quote of the Day: \"{quote}\" - {author}"
        else:
            return "Stay positive and keep pushing forward!"
    except Exception as e:
        print("Error fetching quote:", e)
        return "Keep striving for greatness!"

def send_daily_reminder():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reminder_message = "Good morning! Here’s your daily reminder to stay motivated and focused."
    quote_message = get_motivational_quote()
    
    print(f"\n[{current_time}] Reminder:")
    print(reminder_message)
    print(quote_message)

    notification.notify(
        title="Daily Reminder",
        message=f"{reminder_message}\n\n{quote_message}",
        timeout=10
    )

schedule.every().day.at("17:20").do(send_daily_reminder)

print("Daily reminder script running...")

while True:
    schedule.run_pending()
    time.sleep(1)
