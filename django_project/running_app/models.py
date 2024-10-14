import requests
from django.db import models
    
class Distance(models.Model):
    name = models.CharField(max_length=200, null =True)
    distance = models.DecimalField(default = 0, max_digits=9, decimal_places=3, null=True, blank =True)

    def __str__ (self):
        return self.name
    
    class Meta:
        ordering = ['distance']  # Standardmäßige Sortierung nach Datum (aufsteigend)
    
class RunningEvent(models.Model):
    
    # required fields
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200) 
    postal_code = models.CharField(max_length=200)
    date = models.DateField()

    # additional fields
    state = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    distance = models.ManyToManyField(Distance)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def get_state_from_zip_code(self):
        try:
            # API-Anfrage an Zippopotam.us für Deutschland (DE)
            response = requests.get(f"http://api.zippopotam.us/de/{self.postal_code}")
            data = response.json()
            # Überprüfe, ob der Ortsname übereinstimmt
            for place in data['places']:
                if place['place name'].lower() == self.city.lower():
                    # Das Bundesland extrahieren
                    return place['state']
            return None
        except Exception as e:
            print(f"Fehler beim Abrufen des Bundeslands: {e}")
            return None
        
    def get_coordinates(self):
        """Verwendet die Nominatim API, um Koordinaten aus einer Adresse zu erhalten."""
        try:
            url = f"https://nominatim.openstreetmap.org/search?q={self.city}&format=json"
            response = requests.get(url)
            data = response.json()
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
            return float(latitude), float(longitude)
        except:
            return None, None  # Rückgabe von None, falls die API keine Daten findet


    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.get_coordinates()
        if not self.state:
            self.state = self.get_state_from_zip_code()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']  # Standardmäßige Sortierung nach Datum (aufsteigend)