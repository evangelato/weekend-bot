# weekend-bot

Posts a Friday 5PM GIF to Discord every week.

## How it works
- GitHub Actions triggers at 5PM Pacific (DST-aware)
- Posts to a Discord channel via webhook

## Setup
- Add your Discord webhook URL as a GitHub secret named `WEBHOOK_URL`
