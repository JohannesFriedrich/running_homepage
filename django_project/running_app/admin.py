from django.contrib import admin
from .models import RunningEvent
from .models import Distance
from .models import Source

class RunningEventAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'name', 'city', 'state', 
        'distances', 'latitude', 'longitude',
        'source', 'created_at', 'logo')

    def distances(self, obj):
        return "\n".join([str(d.distance) for d in obj.distance.all()])
    
    def save_model(self, request, obj, form, change):

        # Überprüfe, ob das Event eine Location hat, aber noch keine Koordinaten
        if not obj.latitude or not obj.longitude:
            obj.latitude, obj.longitude = obj.get_coordinates()
        if not obj.state:
            obj.state = obj.get_state_from_zip_code()
        super().save_model(request, obj, form, change)

class DistanceAdmin(admin.ModelAdmin):
    pass

class SourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(RunningEvent, RunningEventAdmin)
admin.site.register(Distance, DistanceAdmin)
admin.site.register(Source, SourceAdmin)

