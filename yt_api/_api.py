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
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptDisabled, NoTranscriptFound

def get_transcript_json(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join(entry["text"] for entry in transcript)
        return f"<html><body>{full_text}</body></html>"
    except TranscriptDisabled:
        return "<html><body>Error: Transcripts are disabled for this video.</body></html>"
    except NoTranscriptFound:
        return "<html><body>Error: No transcript found for this video.</body></html>"
    except Exception as e:
        return f"<html><body>Unexpected error: {str(e)}</body></html>"
