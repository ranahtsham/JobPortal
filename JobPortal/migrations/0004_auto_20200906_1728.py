# Generated by Django 3.0.8 on 2020-09-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('JobPortal', '0003_candidates_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]