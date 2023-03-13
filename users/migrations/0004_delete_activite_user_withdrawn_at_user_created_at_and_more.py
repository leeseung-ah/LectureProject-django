# Generated by Django 4.1.7 on 2023-03-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_activite_remove_user_withdrawn_at_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Activite",
        ),
        migrations.AddField(
            model_name="user",
            name="Withdrawn_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="isWithdrawn",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="lectureDate",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="loginDate",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="paymentDate",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]