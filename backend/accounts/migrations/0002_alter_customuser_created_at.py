# Generated by Django 5.0.6 on 2024-05-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]