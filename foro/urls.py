from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('f/<str:forum>/p/<int:id>/', views.post_detail, name='post-detail'),
]