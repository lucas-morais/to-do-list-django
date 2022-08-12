import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    class Category(models.TextChoices):
        LEISURE = "L", _("Leisure")
        WORK = "W", _("Work")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    finished = models.BooleanField(default=False, null=False)
    category = models.CharField(
        max_length=1,
        choices=Category.choices,
        null=False,
        blank=False,
        default=Category.LEISURE,
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description
