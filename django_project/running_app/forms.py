from django import forms

class EventSubmissionForm(forms.Form):
    name = forms.CharField(max_length=255, label="Name der Veranstaltung")
    location = forms.CharField(max_length=255, label="Ort")
    date = forms.DateField(label="Datum", widget=forms.SelectDateWidget)
    description = forms.CharField(widget=forms.Textarea, label="Beschreibung")
    email = forms.EmailField(label="Deine E-Mail-Adresse")  # E-Mail des Benutzers
