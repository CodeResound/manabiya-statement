from django.urls import path
from .import views

urlpatterns = [
    path('users/', views.UsersView.as_view({'post':'create','get':'list'}), name='users'),
    path('users/<str:pk>/', views.UsersView.as_view({'patch':'partial_update','delete':'destroy'}), name='users-ind'),

    path('login/', views.Login.as_view(), name='login'),
    path('refresh/token/', views.RefreshToken.as_view(), name='refresh-token'),  

    path('logout/', views.Logout.as_view(), name='logout'),
]