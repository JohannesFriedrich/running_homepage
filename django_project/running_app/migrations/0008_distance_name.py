# Generated by Django 5.1.1 on 2024-10-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0007_runningevent_distances'),
    ]

    operations = [
        migrations.AddField(
            model_name='distance',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
