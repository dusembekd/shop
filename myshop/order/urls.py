from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.order_crete, name = 'order_create'),

]