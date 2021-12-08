from django.db import models
from django.core.validators import MinValueValidator


class PredictionInput(models.Model):
    AVOCADO_TYPES = (
        ("ORG", "Organic"),
        ("CON", "Conventional"),
    )

    total_volume = models.FloatField('Total volume', validators=[MinValueValidator(0.0)])
    small_avo = models.FloatField('Small avocados', validators=[MinValueValidator(0.0)])
    large_avo = models.FloatField('Large avocados', validators=[MinValueValidator(0.0)])
    xl_avo = models.FloatField('Extra large avocados', validators=[MinValueValidator(0.0)])
    total_bags = models.FloatField('Total bags', validators=[MinValueValidator(0.0)])
    small_bags = models.FloatField('Small bags', validators=[MinValueValidator(0.0)])
    large_bags = models.FloatField('Large bags', validators=[MinValueValidator(0.0)])
    xl_bags = models.FloatField('Extra large bags', validators=[MinValueValidator(0.0)])
    type = models.CharField('Type',
                            max_length=3,
                            choices=AVOCADO_TYPES,
                            )
    year = models.PositiveIntegerField('Year', validators=[MinValueValidator(0)])
    region = models.CharField('Region', max_length=50)

