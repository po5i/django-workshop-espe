from django.views.generic import TemplateView
from django.views.generic import ListView
from demo.models import Event

from django.views.generic.edit import CreateView


class HomeView(TemplateView):
    template_name = "demo/home.html"


class EventList(ListView):
    model = Event
    ordering = ['date']


class EventCreate(CreateView):
    model = Event
    success_url = '/demo/events/'
    fields = '__all__'
