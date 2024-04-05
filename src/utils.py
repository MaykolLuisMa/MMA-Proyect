from typing import Dict,List
from datetime import datetime,time
import os
import json

def hour__dict__(h : datetime):
    if h is None:
        return None
    return {"year":h.year,"month":h.month,"day":h.day,"hour":h.hour,"minute":h.minute}

def hour_from_dict(dic):
    if dic is None:
        return None
    return datetime(dic["year"],dic["month"],dic["day"],dic["hour"],dic["minute"])

def get_default_hour(professors : List):
    if len(professors) == 0:
        return
    elif professors[0].hours_preference is None:
        return datetime.now()
    else:
        return list(professors[0].hours_preference.keys())[0]

def get_start_hour(professors : List):
    if professors is None or len(professors) == 0 or professors[0].hours_preference is None:
        return None
    return list(professors[0].hours_preference.keys())[0]
        

def load_stats():
    with open(os.getcwd() + "/data/stats.json",'r') as file:
        stats = json.load(file)
    return hour_from_dict(stats["begin"]),time(stats["start"][0],stats["start"][1]),time(stats["end"][0],stats["end"][1]),stats["duration"]

def save_stats(begin : datetime = datetime.now(),start  : time = time(9,0), end : time = time(18,0), duration : int = 3):
    stats_dicts = {"begin":hour__dict__(begin),"start":[start.hour,start.minute],"end":[end.hour,end.minute],"duration":duration}
    with open(os.getcwd() + "/data/stats.json",'w') as file:
        return json.dump(stats_dicts,file)
    
def do_change(begin,start,end,duration):
    begin2,start2,end2,duration2 = load_stats()
    if (begin != begin2 or start != start2 or end != end2 or duration != duration2):
        return True
    return False