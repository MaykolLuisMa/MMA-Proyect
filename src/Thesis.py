import os
import json
from Professor import Professor
from typing import List
from datetime import datetime
from utils import hour__dict__, hour_from_dict
class Thesis:
    def __init__(self, title : str, mentor : Professor, opponent : Professor, president : Professor, secretary : Professor, spokesman : Professor, hour = None, place = None):
        self.title = title
        self.mentor = mentor
        self.opponent = opponent
        self.president = president
        self.secretary = secretary
        self.spokesman = spokesman
        self.hour = hour
        self.place = place
    def get_tasks(self):
        return [self.mentor,self.opponent,self.president,self.secretary,self.spokesman]
    def is_in(self, h : datetime):
        if self.hour == h:
            return 1
        else:
            return 0
            
    def __eq__(self, other : object):
        return self.title == other.title
        
def assign_hour(tasks, variable, hour : List):
    for t in tasks:
        for h in hour:
            if variable[(t,h)] == 1:
                t.thesis.hour = h

def load_thesis(professors : List[Professor]):
    with open(os.getcwd() + "/data/thesis.json",'r') as file:
        all_thesis = json.load(file)
    pd = {p.name:p for p in professors}
    return [Thesis(w[0],pd[w[1][0]],pd[w[1][1]],pd[w[1][2]],pd[w[1][3]],pd[w[1][4]],hour_from_dict(w[2]),w[3]) for w in all_thesis]

def save_thesis(all_thesis : List[Thesis]):
    with open(os.getcwd() + "/data/thesis.json",'w') as file:
        json.dump([[w.title,[p.name for p in w.get_tasks()],hour__dict__(w.hour),w.place] for w in all_thesis],file)
