from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/add/', views.EventCreate.as_view(), name='event-add'),
]
