from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Transcript API is live!"}

@app.get("/transcript")
def get_transcript(video_id: str = Query(..., description="YouTube video ID only")):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {"transcript": transcript}
    except TranscriptsDisabled:
        return {"error": "Transcripts are disabled for this video."}
    except NoTranscriptFound:
        return {"error": "No transcript found."}
    except VideoUnavailable:
        return {"error": "Video is unavailable."}
    except Exception as e:
        return {"error": str(e)}
