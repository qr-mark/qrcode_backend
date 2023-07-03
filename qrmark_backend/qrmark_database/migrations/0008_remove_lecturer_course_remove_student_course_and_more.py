# Generated by Django 4.2.2 on 2023-07-03 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qrmark_database', '0007_remove_attendance_student_attendance_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='qrmark_database.student'),
        ),
    ]
