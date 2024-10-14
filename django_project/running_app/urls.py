from django.urls import path
from running_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),  # Detailansicht für ein Event
    path('submit/', views.submit_event, name='submit_event'),  # Formular für Event-Einreichung
    path('all/', views.all_event_list, name='all_event_list'),  # URL für alle Events
    path('search/', views.event_search, name='event_search'),

]
