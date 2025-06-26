import requests

def _get_transcript_json(video_id):
    response = requests.get(
        f"https://www.youtube.com/watch?v={video_id}",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "*/*",
        }
    )
    return response.text
