from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('docs/', include('statements.urls')), 
    path('auth/', include('authenticate.urls')),
]
