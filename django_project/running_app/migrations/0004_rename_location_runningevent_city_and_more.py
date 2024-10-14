# Generated by Django 5.1.1 on 2024-09-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0003_runningevent_state_alter_runningevent_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runningevent',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='runningevent',
            name='postal_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]