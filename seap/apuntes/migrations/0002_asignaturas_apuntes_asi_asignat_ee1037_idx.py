# Generated by Django 5.1.1 on 2024-09-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apuntes", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="asignaturas",
            index=models.Index(
                fields=["asignatura"], name="apuntes_asi_asignat_ee1037_idx"
            ),
        ),
    ]
