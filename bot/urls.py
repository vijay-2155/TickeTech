from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('chat/', views.chat_with_ai, name='chat_with_ai'),
    path('bot/<int:museum_id>/', views.botpage, name='bot'),
    path('selectCity/', views.selectCity, name='selectCity'),
    path('places/<int:city_id>/', views.place, name='place'),
    path('ticket-booking/<str:museum_name>/', views.ticket_booking_view, name='ticket_booking'),

]
