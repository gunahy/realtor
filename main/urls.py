from django.urls import path
from .views import mainapp, refresh_db


app_name = 'main'


urlpatterns = [
    path('', mainapp, name='index'),
    path('refresh/', refresh_db, name='refresh')
]