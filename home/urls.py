from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('feature-request/', views.feature_request_view, name='feature_request'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('documentation/', views.documentation_view, name='documentation'),
    path('blog/', views.blog_view, name='blog'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
]