# Multi State
# Download and extract latest code
FROM alpine as GIT
ADD https://github.com/instabot-py/instabot.py/archive/master.zip /tmp
RUN unzip -q /tmp/master.zip
RUN cp -r instabot.py-master/src instabot.py-master/requirements.txt /tmp


FROM python:3-alpine
WORKDIR /app
COPY --from=GIT /tmp/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --from=GIT /tmp/src ./src
COPY app.py .

CMD [ "python3", "-u", "app.py" ]
