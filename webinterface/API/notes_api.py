from django.db.models import Max
from webinterface.models import Note


def get_notes():
    notes = Note.objects.all()

    return [
        {
            "id": note.id,
            "text": note.text,
            "position": note.position,
        }
        for note in notes
    ]


def add_note(text):
    text = text.strip()

    if text == "":
        return None

    last_position = Note.objects.aggregate(Max("position"))["position__max"] or 0

    note = Note.objects.create(
        text=text,
        position=last_position + 1
    )

    return {
        "id": note.id,
        "text": note.text,
        "position": note.position,
    }


def remove_note(note_id):
    deleted_count, _ = Note.objects.filter(id=note_id).delete()
    return deleted_count > 0