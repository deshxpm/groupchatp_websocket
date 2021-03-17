from django.urls import path
from chat import views



urlpatterns = [
    path('', views.home, name='showchat'),
    path('room/<str:room_name>/<str:person_name>/', views.showchatpage, name='index'),

]
