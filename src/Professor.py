import json
import os
from datetime import datetime
from typing import Dict, List
from utils import hour__dict__, hour_from_dict
class Professor:
    def __init__(self, name):
        self.name = name
        self.hours_preference = None
    def __eq__(self, other : object):
        return self.name == other.name

def load_professors():
    with open(os.getcwd() + "/data/professors.json",'r') as file:
        professors = json.load(file)
    profs = []
    for p in professors:
        pr = Professor(p[0])
        pr.hours_preference = {hour_from_dict(hi[0]):hi[1] for hi in p[1]}
        profs.append(pr)
    return profs

def save_professors(professors : List[Professor]):
    professors_dicts = [[p.name,[[hour__dict__(h),i] for h,i in p.hours_preference.items()]] for p in professors]
    with open(os.getcwd() + "/data/professors.json",'w') as file:
        return json.dump(professors_dicts,file)