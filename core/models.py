import uuid

from django.db import models


class BaseModel(models.Model):
    """Base model for all models in the project excluding Django's built-in models like User"""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = [
            "-created_at",
            "-updated_at",
        ]
