# Generated by Django 5.1.1 on 2024-10-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0015_alter_distance_distance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningevent',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
