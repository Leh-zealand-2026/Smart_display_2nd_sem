from pathlib import Path
from datetime import datetime, timezone, timedelta

from django.conf import settings

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def get_calendar_service():
    creds = None

    token_path = Path(settings.GOOGLE_TOKEN_PATH)
    credentials_path = Path(settings.GOOGLE_JSON_PATH)

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(
            str(token_path),
            settings.GOOGLE_CALENDAR_SCOPES
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_path),
                settings.GOOGLE_CALENDAR_SCOPES
            )
            creds = flow.run_local_server(port=0)

        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def get_upcoming_events(max_results=30, days_ahead=7):

    service = get_calendar_service()

    now = datetime.now(timezone.utc)
    end_time = now + timedelta(days=days_ahead)

    result = service.events().list(
        calendarId="primary",
        timeMin=now.isoformat(),
        timeMax=end_time.isoformat(),
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = result.get("items", [])

    return [
        {
            "title": event.get("summary", "No title"),
            "start": event["start"].get("dateTime", event["start"].get("date")),
            "end": event["end"].get("dateTime", event["end"].get("date")),
            "location": event.get("location", ""),
        }
        for event in events
    ]