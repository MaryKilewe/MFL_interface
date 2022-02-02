from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'update_facility/<int:facility_id>', views.update_facility_data, name='update_facility_data'),
    path(r'partners', views.partners, name='partners'),
]