from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "youtube_transcript_api")))

from yt_api._api import get_transcript_json


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Local transcript API running"}

@app.get("/transcript")
def get_transcript(video_id: str = Query(...)):
    try:
        html = get_transcript_json(video_id)
        return {"html_snippet": html[:1000]}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
