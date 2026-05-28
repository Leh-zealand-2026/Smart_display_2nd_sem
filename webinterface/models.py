from django.db import models

# Create your models here.


class Note(models.Model):
    text = models.TextField(db_column="content")
    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "dashboard_notes"
        managed = False
        ordering = ["-is_pinned", "-updated_at", "-created_at"]

    def __str__(self):
        return self.text