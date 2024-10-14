from django.shortcuts import render, get_object_or_404
from .models import RunningEvent
from django.core.mail import send_mail
from django.conf import settings
from .forms import EventSubmissionForm
from collections import defaultdict
from datetime import date
from django.db.models import Q
from django.template.defaultfilters import date as _date
from utils.calendar_functions import convert_to_german_month_names

def home(request):
    form = EventSubmissionForm()  # Event-Formular initialisieren
    
    # Veranstaltungen nach Monat gruppieren
    today = date.today()
    all_events = RunningEvent.objects.filter(date__gte=today).order_by('date')
    events_by_month = defaultdict(list)
    for event in all_events:
        month = convert_to_german_month_names(int(event.date.strftime("%-m")))
        year  = event.date.strftime("%Y")
        month_year = month + " " + year
        events_by_month[month_year].append(event)

    # bug: https://www.dermitch.de/post/django-template-iterate-over-defaultdict/
    events_by_month = dict(events_by_month)

    distances = [list(e.distance.all().values_list('name', flat =True)) for e in all_events]

    data = list(all_events.values('city', 'state', 'name', 'date', 'latitude', 'longitude', 'id'))
    # return render(request, 'running_app/events_list.html', {'events_by_month': events_by_month, 'form': form, 'data': data})
    return render(request, 'running_app/home.html', 
                  {'events_by_month': events_by_month, 'form': form, 
                   'data': data})


def all_event_list(request):
    # Nur Events mit einem Datum in der Vergangenheit abrufen
    today = date.today()
    all_events = RunningEvent.objects.filter(date__gte=today).order_by('date')  # In absteigender Reihenfolge (neuste zuerst)

    # Events nach Monaten gruppieren
    events_by_month = defaultdict(list)
    for event in all_events:
        month = convert_to_german_month_names(int(event.date.strftime("%-m")))
        year  = event.date.strftime("%Y")
        month_year = month + " " + year
        events_by_month[month_year].append(event)

    # bug: https://www.dermitch.de/post/django-template-iterate-over-defaultdict/
    events_by_month = dict(events_by_month)

    return render(request, 'running_app/all_event_list.html', {'events_by_month': events_by_month})


def event_detail(request, id):
    # Holt das spezifische Event basierend auf der ID oder zeigt 404-Fehler an
    event = get_object_or_404(RunningEvent, id=id)
    data = {"id": id, "city": event.city, "longitude": event.longitude, "latitude": event.latitude}
    
    return render(request, 'running_app/event_detail.html', {'event': event, 'data':data})



def submit_event(request):
    if request.method == 'POST':
        form = EventSubmissionForm(request.POST)
        if form.is_valid():
            # Daten aus dem Formular holen
            name        = form.cleaned_data['name']
            location    = form.cleaned_data['location']
            date        = form.cleaned_data['date']
            description = form.cleaned_data['description']
            user_email  = form.cleaned_data['email']

            # E-Mail-Inhalt vorbereiten
            subject = f'Neue Veranstaltung: {name}'
            message = f"Details zur Veranstaltung:\n\nName: {name}\nOrt: {location}\nDatum: {date}\n\nBeschreibung:\n{description}\n\nGesendet von: {user_email}"
            recipient_list = ['deine-email@beispiel.de']  # Ziel-E-Mail-Adresse

            # E-Mail senden
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

            # Rückmeldung an den Benutzer geben
            return render(request, 'running_app/submit_success.html', {'name': name})
    else:
        form = EventSubmissionForm()

    return render(request, 'running_app/submit_event.html', {'form': form})
    

def event_search(request):
    query = request.GET.get('query')
    results = []
    data = []
    
    if query:
        # Suche nach Event-Namen oder Ort (Case-Insensitive)
        results = RunningEvent.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query)
        )
        data = list(results.values('city', 'name','date', 'latitude', 'longitude', 'id'))



    return render(request, 'running_app/event_search.html', {'results': results, 'query': query, 'data':data})
