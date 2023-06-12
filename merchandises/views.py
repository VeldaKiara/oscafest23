from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Merchandise
from .serializers import MerchandiseSerializer

class MerchandiseListView(ListAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class MerchandiseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer
