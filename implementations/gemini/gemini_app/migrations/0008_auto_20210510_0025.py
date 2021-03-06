# Generated by Django 3.2 on 2021-05-09 17:25

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gemini_app', '0007_auto_20210509_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scienceplan',
            name='creator',
            field=models.CharField(default='Creator name', max_length=50),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='end_date',
            field=models.DateTimeField(default='09/05/2021 17:25:19', validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 5, 9, 17, 25, 19, 676378, tzinfo=utc), message='The end date is invalid.')]),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='start_date',
            field=models.DateTimeField(default='09/05/2021 17:25:19', validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 5, 9, 17, 25, 19, 676378, tzinfo=utc), message='The start date is invalid.')]),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='submitter',
            field=models.CharField(default='Submitter name', max_length=50),
        ),
    ]
