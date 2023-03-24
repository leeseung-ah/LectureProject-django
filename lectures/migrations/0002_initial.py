# Generated by Django 4.1.7 on 2023-03-24 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lectures", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lecture",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lectures",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="calculatedlecture",
            name="lecture",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lecture",
                to="lectures.lecture",
            ),
        ),
    ]
