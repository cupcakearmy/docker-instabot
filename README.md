# Intabot Docker

Docker container for runnning [Instabot](https://github.com/instabot-py/instabot.py).

## Quickstart 💥

```
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