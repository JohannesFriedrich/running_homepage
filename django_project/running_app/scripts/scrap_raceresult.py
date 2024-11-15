from running_app.models import RunningEvent
from running_app.models import Distance
from running_app.models import Source
import requests
import regex as re
from datetime import date, datetime
import time

"""_summary_
    "id": event[0],        
    "name": event[2],      
    "date_start": event[3],
    "date_end": event[4],
    "city": event[5],
    "country": event[6],
    "lat": event[7],
    "long": event[8],
    "country_2": event[9],
    "event_type": event[10]
"""


# contests: https://my.raceresult.com/313043/RRPublish/data/config

def get_distances(event_id: int):

    url: str = "https://my.raceresult.com/"+str(event_id)+"/RRPublish/data/config"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        contests = str(data["contests"])
        matches = re.findall(
            r'(?<=(^|[- ]))(?<!ultra[- ])(viertelmarathon|halbmarathon|marathon)', 
            contests.lower())

        if matches:
            print(matches)
        else:
            matches = re.findall(
                r'^*?([0-9]+(?:[,.][0-9]+)?)[ ]?km?', 
                contests)
            if matches:
                print(matches)



def run():

    source = Source.objects.filter(source="raceresult").get()

    year = "2024"
    type = "0" #running
    type = "30" #trail-running
    country = "276" # 276: Deutschland
    url = "https://my.raceresult.com/RREvents/list?type="+type+"&year="+year+"&country="+country
    print(url)
    response = requests.get(url)

    if response.ok:
        events = response.json()

        for event in events:
            get_distances(event_id = event[0])

            # distances_event = Distance.objects.create(

            # )
            # Just create object if it is not already in the database
            if not RunningEvent.objects.filter(name = event[2]):
                if datetime.now() < datetime.strptime(event[3], "%Y-%m-%d"):

                    running_event: RunningEvent = RunningEvent.objects.create(
                        name = event[2],
                        city = event[5],
                        date = event[3],
                        latitude =  event[7],
                        longitude =  event[8],
                        url = "https://my.raceresult.com/"+str(event[0]),
                        logo = "https://my.raceresult.com/"+str(event[0])+"/logo",
                        source = source,
                        type = "running" if type==30 else "trail-running",
                        description = ""
                    )

                    print(f"Created event {event[2]}")
                else:
                    print(f"Event {event[2]} was in the past.")
            else:
                print(f"Event {event[2]} already exists.")
            time.sleep(30)
    else:
        print(f"Problems scraping raceresults")   