# Generated by Django 5.1.1 on 2024-10-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0005_distance_alter_runningevent_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningevent',
            name='distances',
        ),
        migrations.AlterField(
            model_name='distance',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=9, null=True),
        ),
    ]