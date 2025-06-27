from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Allow importing youtube_transcript_api as a submodule
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "youtube_transcript_api")))

from yt_api._api import get_transcript_json

app = FastAPI()

# ✅ Add CORS Middleware to support frontend requests from Bolt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Local transcript API running"}

@app.get("/transcript")
def get_transcript(video_id: str = Query(...)):
    try:
        html = get_transcript_json(video_id)
        return {"html_snippet": html}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
