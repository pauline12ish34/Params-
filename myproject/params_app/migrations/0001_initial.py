# Generated by Django 5.1.3 on 2024-11-24 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ParkingLot",
            fields=[
                ("lot_id", models.AutoField(primary_key=True, serialize=False)),
                ("location", models.CharField(max_length=255)),
                ("total_spaces", models.IntegerField()),
                ("available_spaces", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                (
                    "role",
                    models.CharField(
                        choices=[("Admin", "Admin"), ("Staff", "Staff")], max_length=50
                    ),
                ),
                ("contact_info", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                ("vehicle_id", models.AutoField(primary_key=True, serialize=False)),
                ("plate_number", models.CharField(max_length=20, unique=True)),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("Car", "Car"),
                            ("Motorcycle", "Motorcycle"),
                            ("Truck", "Truck"),
                        ],
                        max_length=50,
                    ),
                ),
                ("owner_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ParkingSpace",
            fields=[
                ("space_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "space_type",
                    models.CharField(
                        choices=[
                            ("Compact", "Compact"),
                            ("Large", "Large"),
                            ("Electric Vehicle", "Electric Vehicle"),
                        ],
                        max_length=50,
                    ),
                ),
                ("is_occupied", models.BooleanField(default=False)),
                (
                    "parking_lot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spaces",
                        to="params_app.parkinglot",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParkingTicket",
            fields=[
                ("ticket_id", models.AutoField(primary_key=True, serialize=False)),
                ("entry_time", models.DateTimeField(auto_now_add=True)),
                ("exit_time", models.DateTimeField(blank=True, null=True)),
                (
                    "fee",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "parking_space",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="params_app.parkingspace",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="params_app.vehicle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("payment_id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("Cash", "Cash"),
                            ("Credit Card", "Credit Card"),
                            ("Digital Wallet", "Digital Wallet"),
                        ],
                        max_length=50,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "ticket",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to="params_app.parkingticket",
                    ),
                ),
            ],
        ),
    ]
