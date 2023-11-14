from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('car_details/<int:car_id>/', views.car_details, name='car_details'),
    path('feedback/', views.feedbackurl, name='feedback'),
    path('main/', views.copyindex, name='main'),
    path('shipping/', views.shipping, name='shipping'),
    path('arivalls/', views.newariv, name='arivalls'),
    path('submit_form/', views.submit_form, name='submit_form')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
