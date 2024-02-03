# Generated by Django 4.2.9 on 2024-02-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hackhive", "0002_alter_calendar_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="calendar",
            options={},
        ),
        migrations.AlterField(
            model_name="calendar",
            name="event_host",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="event_host_phone",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="event_image",
            field=models.ImageField(blank=True, upload_to="event_images"),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="event_location",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="event_name",
            field=models.CharField(max_length=200),
        ),
    ]
