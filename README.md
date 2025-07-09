# SimpleChurch

**SimpleChurch** is a voice-controlled music search assistant tailored for churches to quickly identify worship songs from spoken lyrics. It records short audio clips, transcribes them using speech recognition, then queries the Genius API to find matching songs. Results are carefully filtered to highlight trusted worship artists and gospel-related content, ensuring relevant and appropriate suggestions for church worship settings. This tool streamlines worship planning and enhances congregational engagement by making song discovery fast, accurate, and customized for your community.

---

## How to Use

1. **Build the Docker container:**

```bash
docker build -t audio-processor .
```

2. **Prepare the recording script (run once)
```bash
chmod +x record_audio.sh
```

3. **Record audio and process
```bash
./record_audio.sh
```
