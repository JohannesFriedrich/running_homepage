# Generated by Django 5.1.1 on 2024-11-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0024_runningevent_last_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runningevent',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
