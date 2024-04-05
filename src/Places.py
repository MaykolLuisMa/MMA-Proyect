import os
import json
from typing import List
def load_places() -> List[str]:
    with open(os.getcwd() + "/data/places.json",'r') as file:
        return json.load(file)
def save_places(places : List[str]):
    with open(os.getcwd() + "/data/places.json",'w') as file:
        json.dump(places,file)
