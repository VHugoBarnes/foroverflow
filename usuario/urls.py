from django.urls import path
from . import views

urlpatterns = [
    path('u/<str:nombre_usuario>', views.user_profile, name='user-profile'),
]