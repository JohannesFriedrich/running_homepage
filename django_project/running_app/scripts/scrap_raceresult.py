from running_app.models import RunningEvent
from running_app.models import Distance
from running_app.models import Source
import requests

# contests: https://my.raceresult.com/313043/RRPublish/data/config

def get_distances(event_id: int):

    url: str = "https://my.raceresult.com/"+str(event_id)+"/RRPublish/data/config"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        data["contests"]



def run():
    year = "2025"
    type = "0" #running
    # # type = "30" #trail-running
    url = "https://my.raceresult.com/RREvents/list?type="+type+"&year="+year+"&country=276"

    response = requests.get(url)

    # if response.ok:
    events = response.json()

    events_dict = []
    event = events[4]
    # print(event)
    # for event in events:

    event_id = event[0]
    source = Source.objects.filter(source="raceresult").get()

    # distances_raceresult = 

    # distances_event = Distance.objects.create(

    # )
    # Just create object if it is not already in the database
    if not RunningEvent.objects.filter(name = event[2]):

        running_event = RunningEvent.objects.create(
            name = event[2],
            city = event[5],
            date = event[3],
            latitude =  event[7],
            longitude =  event[8],
            logo = "https://my.raceresult.com/"+str(event[0])+"/logo",
            source = source
        )

        print(f"Created event {event[2]}")

    
    # events_dict.append({
    #     "id": event[0],        
    #     "name": event[2],      
    #     "date_start": event[3],
    #     "date_end": event[4],
    #     "city": event[5],
    #     "country": event[6],
    #     "lat": event[7],
    #     "long": event[8],
    #     "country_2": event[9],
    #     "event_type": event[10]
    # })

# print(events_dict)


# url: str = f"https://nominatim.openstreetmap.org/search?q=Monschau-Mützenich&format=json"
# response = requests.get(url)
# data = response.json()

# print(data)

# events_dict = []
# for event in data:
#     events_dict.append({
#         "id": event[0],        
#         "name": event[2],      
#         "date_start": event[3],
#         "date_end": event[4],
#         "city": event[5],
#         "country": event[6],
#         "lat": event[7],
#         "long": event[8],
#         "country_2": event[9],
#         "event_type": event[10]
#     })

# print(events_dict)
