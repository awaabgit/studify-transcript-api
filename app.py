from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Local transcript API running"}

@app.get("/transcript")
def get_transcript(video_id: str = Query(...)):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([entry['text'] for entry in transcript])
        return {"transcript": full_text}
    except TranscriptsDisabled:
        return JSONResponse(status_code=400, content={"error": "Transcripts are disabled."})
    except NoTranscriptFound:
        return JSONResponse(status_code=404, content={"error": "Transcript not found."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
