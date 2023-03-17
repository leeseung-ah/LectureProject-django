

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(

            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Lecture",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("LectureId", models.AutoField(primary_key=True, serialize=False)),
                ("lectureTitle", models.CharField(max_length=100)),
                ("lectureDescription", models.TextField(max_length=1000)),
                ("lectureDifficulty", models.CharField(max_length=100)),
                ("targetAudience", models.CharField(max_length=100)),
                ("lectureFee", models.PositiveIntegerField(blank=True, null=True)),
                ("thumbnail", models.URLField(blank=True, null=True)),
                ("lecturePeriod", models.DateField(blank=True, null=True)),
                ("isOpened", models.BooleanField(default=True)),
                ("likes", models.PositiveIntegerField(blank=True, null=True)),
                ("lectureDuration", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "lectureTotal",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("grade", models.PositiveIntegerField()),
                (
                    "categories",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ledetailes",
                        to="categories.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
