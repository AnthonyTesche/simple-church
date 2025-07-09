FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    flac \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy soundfile matplotlib speechrecognition pydub requests

WORKDIR /app

COPY process.py .

CMD ["python", "process.py"]
