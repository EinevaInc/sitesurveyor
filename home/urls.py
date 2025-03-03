from django.urls import path
from . import views

app_name = 'home'  # Add this line

urlpatterns = [
    path('', views.index, name='index'),
    path('feature-request/', views.feature_request_view, name='feature_request'),
]