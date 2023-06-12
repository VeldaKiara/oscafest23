# Create your views here.
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Merchandise
# from .serializers import MerchandiseSerializer

# class MerchandiseListAPIView(APIView):
#     def get(self, request):
#         merchandise = Merchandise.objects.all()
#         serializer = MerchandiseSerializer(merchandise, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MerchandiseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MerchandiseDetailAPIView(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Merchandise, pk=pk)
#         serializer = MerchandiseSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = get_object_or_404(Merchandise, pk=pk)
#         serializer = MerchandiseSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = get_object_or_404(Merchandise, pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

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
