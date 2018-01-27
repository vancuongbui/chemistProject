from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('new/',views.CreateProductView.as_view(),name='new'),
    path('detail/<slug>/',views.ProductDetailView.as_view(),name='detail'),
]