# Generated by Django 5.0.6 on 2024-05-22 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("file_transfer", "0002_file_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="file_name",
        ),
        migrations.RemoveField(
            model_name="file",
            name="file_size",
        ),
    ]