# Generated by Django 4.2.7 on 2023-11-27 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0005_remove_calendar_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='counselor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_app.counselor'),
        ),
    ]
