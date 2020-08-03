from django.urls import path,include,re_path
from characters import views

urlpatterns = [
    path('', views.heroes, name='heroes'),
]
