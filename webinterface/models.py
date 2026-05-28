from django.db import models


class Note(models.Model):
    text = models.TextField(db_column="content")
    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    class Meta:
        db_table = "dashboard_notes"
        managed = False
        ordering = ["-is_pinned", "-id"]

    def __str__(self):
        return self.text