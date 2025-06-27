from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_transcript_json(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {
            "video_id": video_id,
            "transcript": transcript
        }
    except TranscriptsDisabled:
        return {"error": "Transcripts are disabled for this video."}
    except NoTranscriptFound:
        return {"error": "No transcript found for this video."}
    except Exception as e:
        return {"error": str(e)}
