from predictor.models import PredictionInput
from rest_framework import viewsets
from predictor.serializers import PredictionInputSerializer


class PredictionInputViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows predictor inputs to be viewed or edited.
    """
    queryset = PredictionInput.objects.all()
    serializer_class = PredictionInputSerializer
