# Generated by Django 4.1.7 on 2024-07-13 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('capacity', models.IntegerField()),
                ('projector_available', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='booking_hall',
            name='hall_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.hall'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedules_m',
            name='hall_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.hall'),
            preserve_default=False,
        ),
    ]