# Generated by Django 5.0.3 on 2024-03-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="image_url",
            field=models.URLField(
                default="https://upload.wikimedia.org/wikipedia/commons/1/17/Hotel_Ritz_Paris.jpg"
            ),
        ),
    ]
