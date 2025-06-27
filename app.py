from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import os
import sys

# Allow import of yt_api module
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from yt_api._api import get_transcript_json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Local transcript API running"}

@app.get("/transcript")
def get_transcript(video_id: str = Query(...)):
    try:
        result = get_transcript_json(video_id)
        return result  # This will be a dict or error
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
