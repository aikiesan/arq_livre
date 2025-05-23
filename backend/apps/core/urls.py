from django.urls import path
from . import views

app_name = 'core' # Define um namespace para suas URLs

urlpatterns = [
    path('', views.home_view, name='home'),
]