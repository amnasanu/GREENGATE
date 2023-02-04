from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Farmer
from .serializers import FarmerSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    