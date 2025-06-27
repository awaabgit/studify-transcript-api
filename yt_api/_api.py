from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_transcript_json(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join(entry["text"] for entry in transcript)
        return f"<html><body>{full_text}</body></html>"
    except TranscriptsDisabled:
        return "<html><body>Error: Transcripts are disabled for this video.</body></html>"
    except NoTranscriptFound:
        return "<html><body>Error: No transcript found for this video.</body></html>"
    except Exception as e:
        return f"<html><body>Unexpected error: {str(e)}</body></html>"
