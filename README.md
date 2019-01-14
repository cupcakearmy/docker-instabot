# Intabot Docker

Docker container for runnning [Instabot](https://github.com/instabot-py/instabot.py).

## Quickstart 💥

```bash
docker-compose up -d
```

## Setup 🏗

```bash
git clone https://github.com/CupCakeArmy/docker-instabot
cd docker-instabot

# Copy or Move sample config.
cp config.sample.json config.json
# Insert own login data and tags.
vim config.json

# Run
docker-compose up -d
```

#### (Optional) Persist the DB 💽

Instabot saved the followers etc. in a sqlite db called `follows_db.db`. If you wish to persist the changes between updates you need to uncomment the line inside `docker-compose.yml` and run `touch data.db` before running `docker-compose up -d`

### Credits 

The actual code for the bot is from https://github.com/instabot-py/instabot.py
