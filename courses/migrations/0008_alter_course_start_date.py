# Generated by Django 4.2.4 on 2023-08-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0007_alter_course_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="start_date",
            field=models.DateField(),
        ),
    ]