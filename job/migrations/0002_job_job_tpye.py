# Generated by Django 3.1 on 2020-08-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_tpye',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part time', 'Part Time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
