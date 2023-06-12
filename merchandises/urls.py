from django.urls import path
from django.views.generic import TemplateView
from .views import MerchandiseListView, MerchandiseDetailView

app_name='merchandises'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('merchandise/', MerchandiseListView.as_view(), name='merchandise-list'),
    path('merchandise/<uuid:pk>/', MerchandiseDetailView.as_view(), name='merchandise-detail'),
]
