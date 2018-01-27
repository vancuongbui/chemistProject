from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from products import views as productViews


app_name = 'categories'

urlpatterns = [
    path('list/',views.CategoryList.as_view(),name='list'),
    path('new/',views.CreateCategoryView.as_view(),name='new'),
    path('<slug>/',productViews.ProductListView.as_view(),name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)