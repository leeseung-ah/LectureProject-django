# Generated by Django 4.1.3 on 2023-03-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="classification",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
