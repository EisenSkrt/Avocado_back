# Generated by Django 3.2.9 on 2021-12-02 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0007_alter_predictioninput_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictioninput',
            name='large_avo',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Large avocados'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='large_bags',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Large bags'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='small_avo',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Small avocados'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='small_bags',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Small bags'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='total_bags',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Total bags'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='total_volume',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Total volume'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='xl_avo',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Extra large avocados'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='xl_bags',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Extra large bags'),
        ),
    ]
