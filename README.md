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

### (Default) Persist the DB 💽

By default the DB is persisted. Instabot saved the followers etc. in a sqlite db called `follows_db.db`. To start with a clean state you need to delete the `data.db` file.
Either run `rm data.db; touch data.db` or `cat /dev/null > data.db`.

### Credits

The actual code for the bot is from https://github.com/instabot-py/instabot.py
