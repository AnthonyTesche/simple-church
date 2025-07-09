import speech_recognition as sr
import requests

GENIUS_API_TOKEN = "genius_api_token"
AUDIO_FILE = "record.wav"

def search_genius(lyrics_snippet):
    base_url = "https://api.genius.com/search"
    headers = {'Authorization': f'Bearer {GENIUS_API_TOKEN}'}
    params = {'q': lyrics_snippet}
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Genius API error: {response.status_code}")
        return []
    json_resp = response.json()
    hits = json_resp.get('response', {}).get('hits', [])
    results = []
    for hit in hits:
        song_info = hit['result']
        results.append({
            'title': song_info['title'],
            'artist': song_info['primary_artist']['name'],
            'url': song_info['url']
        })
    return results

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language="pt-BR")
    print("Recognized text:", text)

    results = search_genius(text)
    if not results:
        print("No songs found on Genius for the recognized text.")
    else:
        print("\nTop Genius matches:")
        for i, song in enumerate(results[:5], 1):
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   URL: {song['url']}")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
