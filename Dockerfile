FROM alpine

# Install FFmpeg
RUN apk update && \
    apk add ffmpeg python3 py3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app
RUN mkdir ./media
RUN pip3 install -r requirements.txt --break-system-packages

CMD ["python3", "watch.py"]
