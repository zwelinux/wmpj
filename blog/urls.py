from django.urls import path
from .import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<int:post_id>/', views.detail, name='detail'),
]