# Generated by Django 5.0.2 on 2024-02-21 04:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "room_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "room_type",
                    models.IntegerField(
                        choices=[(1, "Hu"), (2, "Stu"), (3, "Br1"), (4, "Br2")],
                        default=1,
                    ),
                ),
                (
                    "price_per_night",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("room_number", models.IntegerField()),
                (
                    "hotel_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotels.hotel"
                    ),
                ),
            ],
        ),
    ]
