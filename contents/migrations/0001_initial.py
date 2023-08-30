# Generated by Django 4.2.4 on 2023-08-24 16:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("video_url", models.CharField(max_length=200)),
            ],
        ),
    ]