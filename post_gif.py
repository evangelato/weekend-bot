import os
import requests

webhook_url = os.environ["WEBHOOK_URL"]
gif_url = "https://tenor.com/view/friday-ladies-and-gentlemen-the-weekend-daniel-craig-snl-gif-22971017"

requests.post(webhook_url, json={"content": gif_url})
