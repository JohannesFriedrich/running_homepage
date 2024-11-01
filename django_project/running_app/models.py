import requests
from django.db import models
import time
    
class RunningEvent(models.Model):
    
    # required fields
    name = models.CharField(max_length=200)
    date = models.DateField()

    # additional fields
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200) 
    state = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="")
    distance = models.ManyToManyField("Distance", blank=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    # card_color = models.CharField(max_length=7, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True, default="running")
    source = models.ForeignKey("Source", on_delete=models.CASCADE, null =True, blank =True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_change = models.DateTimeField(auto_now=True, blank=True, null=True)
        
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
        
    def get_zip_and_state_from_long_lat(self):
        try:
            url = f"https://nominatim.openstreetmap.org/reverse?lat={self.latitude}&lon={self.longitude}&format=json"
            headers = {'user-agent': 'running_homepage/0.0.1'}
            response = requests.get(url, headers=headers)

            if response.ok:
                data = response.json()
                print("Nominatim API successful scraped state and postcode -> Wait 70s until next query ...")
                time.sleep(70)
                return data["address"]["state"], data["address"]["postcode"] 
            else:
                print("No return from nominatim API")
                return None, None               
        except:
            print("No return from nominatim API")
            return None, None


    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.get_coordinates()
        if not self.state or not self.postal_code:
            self.state, self.postal_code = self.get_zip_and_state_from_long_lat()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']  # Standardmäßige Sortierung nach Datum (aufsteigend)


class Distance(models.Model):
    name = models.CharField(max_length=200, null =True)
    distance = models.DecimalField(default = None, max_digits=9, decimal_places=3, blank=True)

    def __str__ (self) -> str:
        return str(self.name)
    
    class Meta:
        ordering = ['distance']  # Standardmäßige Sortierung nach Datum (aufsteigend)
    
class Source(models.Model):
    source = models.CharField(max_length=200, null =True)

    def __str__ (self) -> str:
        return str(self.source)
