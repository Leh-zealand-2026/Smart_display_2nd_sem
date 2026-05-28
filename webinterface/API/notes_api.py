import json

from webinterface.models import Note


def get_notes():
    notes = Note.objects.filter(is_archived=False).order_by("-is_pinned", "-id")

    return [
        {
            "id": note.id,
            "text": note.text,
        }
        for note in notes
    ]


def add_note(text):
    text = text.strip()

    if text == "":
        return None

    note = Note.objects.create(text=text)

    return {
        "id": note.id,
        "text": note.text,
    }


def remove_note(note_id):
    deleted_count, _ = Note.objects.filter(id=note_id).delete()
    return deleted_count > 0