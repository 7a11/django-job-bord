# Generated by Django 3.1 on 2020-08-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_tpye'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='discriptin',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
