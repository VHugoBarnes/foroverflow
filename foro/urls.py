from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('f/<str:forum>/p/<int:id>/', views.post_detail, name='post-detail'),
    path('create-post', views.create_post, name='create-post'),
    path('f/<str:forum>/p/<int:id>/edit', views.edit_post, name='edit-post'),
    # path('f/<str:forum>/p/<int:id>/edit', views.PostUpdateView.as_view(), name='edit-post'),
]