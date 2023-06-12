from django.urls import path
from django.views.generic import TemplateView
# from access import views
app_name='merchandises'

# urlpatterns=[
# path('', TemplateView.as_view(template_name='home.html'), name='home'),
# path('merchandises/', name='merchandise'),

# # path('hello/', views.HelloView.as_view(), name='hello'),

# ]


from .views import MerchandiseListView, MerchandiseDetailView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('merchandise/', MerchandiseListAPIView.as_view(), name='merchandise-list'),
    # path('merchandise/<int:pk>/', MerchandiseDetailAPIView.as_view(), name='merchandise-detail'),
    path('merchandise/', MerchandiseListView.as_view(), name='merchandise-list'),
    path('merchandise/<uuid:pk>/', MerchandiseDetailView.as_view(), name='merchandise-detail'),


]

