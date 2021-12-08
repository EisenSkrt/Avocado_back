from predictor.models import PredictionInput
from rest_framework import serializers


class PredictionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionInput
        fields = '__all__'
