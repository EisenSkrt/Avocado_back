# Generated by Django 3.2.9 on 2021-12-02 09:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0008_auto_20211202_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictioninput',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Year'),
        ),
    ]
