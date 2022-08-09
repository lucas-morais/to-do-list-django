import uuid
from django.db import models


class Todo(models.Model):
    CATEGORY = (("L", "Leisure"), ("W", "Work"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    finished = models.BooleanField(default=False, null=False)
    category = models.CharField(
        max_length=1, choices=CATEGORY, null=False, blank=False, default="L"
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description
