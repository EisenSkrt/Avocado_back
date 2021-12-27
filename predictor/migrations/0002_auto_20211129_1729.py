# Generated by Django 3.2.9 on 2021-11-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictioninput',
            name='val_one',
            field=models.FloatField(default=0, verbose_name='4046'),
        ),
        migrations.AddField(
            model_name='predictioninput',
            name='val_three',
            field=models.FloatField(default=0, verbose_name='4770'),
        ),
        migrations.AddField(
            model_name='predictioninput',
            name='val_two',
            field=models.FloatField(default=0, verbose_name='4225'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='large_bags',
            field=models.FloatField(default=0, verbose_name='Large bags'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='small_bags',
            field=models.FloatField(default=0, verbose_name='Small bags'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='total_bags',
            field=models.FloatField(default=0, verbose_name='Total bags'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='total_volume',
            field=models.FloatField(default=0, verbose_name='Total volume'),
        ),
        migrations.AlterField(
            model_name='predictioninput',
            name='xl_bags',
            field=models.FloatField(default=0, verbose_name='Extra large bags'),
        ),
    ]