# Generated by Django 4.2.4 on 2023-08-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0005_alter_content_name_alter_content_video_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="content",
            field=models.TextField(),
        ),
    ]