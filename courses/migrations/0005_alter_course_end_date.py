# Generated by Django 4.2.4 on 2023-08-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0004_alter_course_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="end_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
