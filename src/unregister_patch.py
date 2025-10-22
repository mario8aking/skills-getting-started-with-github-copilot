# Add unregister endpoint for tests and frontend
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# ...existing code...

@app.post("/activities/{activity_name}/unregister")
def unregister_for_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    try:
        activity["participants"].remove(email)
    except ValueError:
        raise HTTPException(status_code=404, detail="Participant not found")
    return {"message": f"Unregistered {email} from {activity_name}"}
