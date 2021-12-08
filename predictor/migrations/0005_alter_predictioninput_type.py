# Generated by Django 3.2.9 on 2021-12-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0004_auto_20211202_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictioninput',
            name='type',
            field=models.CharField(choices=[('ORG', 'Organic'), ('CON', 'Conventional')], default='CON', max_length=3, verbose_name='Type'),
        ),
    ]
