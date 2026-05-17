import os
import datetime
import zoneinfo
import requests

now = datetime.datetime.now(zoneinfo.ZoneInfo("America/Los_Angeles"))
if now.hour != 17:
    print(f"Not 5PM Pacific (current hour: {now.hour}), skipping.")
    exit()

webhook_url = os.environ["WEBHOOK_URL"]
gif_url = "https://tenor.com/view/friday-ladies-and-gentlemen-the-weekend-daniel-craig-snl-gif-22971017"

requests.post(webhook_url, json={"content": gif_url})
print("Posted!")
