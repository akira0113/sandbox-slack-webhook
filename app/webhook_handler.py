from fastapi import Request
from fastapi.responses import JSONResponse, PlainTextResponse
import json

async def handle_slack_webhook(request: Request):
    try:
        # Slackの Event API（JSON形式）のリクエスト
        payload = await request.json()
        print("Received JSON payload:", json.dumps(payload, indent=2))

        if payload.get("type") == "url_verification":
            return JSONResponse({"challenge": payload["challenge"]})

    except Exception:
        # スラッシュコマンドなど、JSONでないリクエストの場合は form を使う
        form = await request.form()
        print("Received form payload:", dict(form))

        # ✅ スラッシュコマンドの応答例
        if form.get("command") == "/ping":
            user = form.get("user_name", "user")
            text = form.get("text", "")
            return PlainTextResponse(f"Pong! {user} said: {text}")

    return JSONResponse({"status": "ok"})
