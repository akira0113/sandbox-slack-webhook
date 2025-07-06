from fastapi import FastAPI, Request
from app.webhook_handler import handle_slack_webhook

app = FastAPI()

@app.post("/slack/events")
async def slack_events(request: Request):
    return await handle_slack_webhook(request)
