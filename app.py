from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from fastapi.responses import JSONResponse

app = FastAPI()

# Optional: allow access from any frontend (can restrict to Bolt domain later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Studify transcript API is working!"}

@app.get("/transcript")
async def get_transcript(video_id: str = Query(..., description="YouTube video ID only")):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([entry['text'] for entry in transcript])
        return {"transcript": full_text}
    except TranscriptsDisabled:
        return JSONResponse(
            status_code=400,
            content={"error": "Transcripts are disabled for this video."}
        )
    except NoTranscriptFound:
        return JSONResponse(
            status_code=404,
            content={"error": "Transcript not found. The video may not have captions or may be restricted."}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
