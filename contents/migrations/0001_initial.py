# Generated by Django 5.0.4 on 2024-05-06 17:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('video_url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
