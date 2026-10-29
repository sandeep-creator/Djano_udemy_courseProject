from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    path('details/<int:item_id>/', views.details, name='details')
]