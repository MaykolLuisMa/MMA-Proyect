from typing import List
from Thesis import Thesis
from Professor import Professor
class Task:
    def __init__(self, id, thesis : Thesis, professors : List[Professor]):
        self.id = id
        self.thesis = thesis
        self.professors = professors

def get_tasks(all_thesis : List[Thesis]):
    i = 0
    tasks = []
    for w in all_thesis:
        for t in w.get_tasks():
            tasks.append(Task(i,w,t))
            i += 1
    return tasks
    