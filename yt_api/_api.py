from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import requests

SCRAPER_API_KEY = "48c9a193c3eab620c3e3d5fed532fcf81"  # replace with your key

def get_transcript_json(video_id: str):
    try:
        # Attempt direct transcript fetch
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join(entry["text"] for entry in transcript)
        return f"<html><body>{full_text}</body></html>"

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        return f"<html><body>Error: {str(e)}</body></html>"

    except Exception as e:
        print("Default method failed. Trying ScraperAPI...")
        try:
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
          params = {
    'api_key': SCRAPER_API_KEY,
    'url': youtube_url,
}
response = requests.get("http://api.scraperapi.com/", params=params)

            # Just return the HTML (for now). You can later parse this into real transcript
            return f"<html><body>{response.text}</body></html>"

        except Exception as fallback_error:
            return f"<html><body>ScraperAPI failed: {str(fallback_error)}</body></html>"
