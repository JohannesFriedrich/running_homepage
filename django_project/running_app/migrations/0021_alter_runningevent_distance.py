# Generated by Django 5.1.1 on 2024-10-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0020_source_runningevent_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runningevent',
            name='distance',
            field=models.ManyToManyField(blank=True, null=True, to='running_app.distance'),
        ),
    ]
