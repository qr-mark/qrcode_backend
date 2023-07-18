# Generated by Django 4.2.2 on 2023-07-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qrmark_database", "0011_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[
                    ("FEMALE", "FEMALE"),
                    ("MALE", "MALE"),
                    ("MR", "MR"),
                    ("MRS", "MRS"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
