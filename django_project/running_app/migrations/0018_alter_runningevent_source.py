# Generated by Django 5.1.1 on 2024-10-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0017_runningevent_source_runningevent_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runningevent',
            name='source',
            field=models.CharField(blank=True, default='running', max_length=200, null=True),
        ),
    ]
