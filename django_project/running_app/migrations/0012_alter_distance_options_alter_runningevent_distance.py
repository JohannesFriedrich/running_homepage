# Generated by Django 5.1.1 on 2024-10-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0011_remove_distance_events_distance_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distance',
            options={'ordering': ['distance']},
        ),
        migrations.AlterField(
            model_name='runningevent',
            name='distance',
            field=models.ManyToManyField(to='running_app.distance'),
        ),
    ]
