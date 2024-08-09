from django.urls import path
from . import views

app_name = 'recommendation_system'

urlpatterns = [
    path('', views.home, name='home'),

]
