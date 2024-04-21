# Generated by Django 1.11.5 on 2017-12-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactEmail",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=128)),
                ("sent_to", models.EmailField(max_length=128)),
                ("message", models.TextField()),
                (
                    "contact_type",
                    models.CharField(
                        choices=[
                            ("chapter", "Django Girls Local Organizers"),
                            ("support", "Django Girls HQ (Support Team)"),
                        ],
                        default="chapter",
                        max_length=20,
                        verbose_name="Who do you want to contact?",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("sent_successfully", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]
