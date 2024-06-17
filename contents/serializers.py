from contents.models import Content
from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "name", "video_url", "content"]
