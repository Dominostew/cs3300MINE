# Generated by Django 4.2.7 on 2023-11-28 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0008_delete_calendarincounselors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Busy', 'Busy'), ('Not Busy', 'Not Busy')], max_length=200, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('counselor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_app.counselor')),
            ],
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]