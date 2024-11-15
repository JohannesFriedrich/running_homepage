# Generated by Django 5.1.1 on 2024-09-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0002_alter_runningevent_distances'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningevent',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='runningevent',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='runningevent',
            name='distances',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='runningevent',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
