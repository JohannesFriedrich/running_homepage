# Generated by Django 5.1.1 on 2024-10-05 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_app', '0004_rename_location_runningevent_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=3, default=0, max_digits=9)),
            ],
        ),
        migrations.AlterModelOptions(
            name='runningevent',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='runningevent',
            name='distances',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='running_app.distance'),
        ),
    ]
