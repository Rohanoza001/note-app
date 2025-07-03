from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('login', views.login, name='login'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.logout, name='logout'),
    path('homepage', views.homepage, name='homepage'),
    path('create_note', views.create_note, name='create_note'),
    path('create_note_user', views.create_note_user, name='create_note_user'),
]
