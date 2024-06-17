import uuid
from django.db import models


class Content(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    video_url = models.CharField(max_length=200, null=True, blank=True)

    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="contents", null=False
    )
