# Generated by Django 4.2.4 on 2023-08-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0004_rename_courses_content_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="content",
            name="video_url",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
