from typing import List
from Professor import Professor
from pulp import *
from Task import Task, get_tasks
from Thesis import Thesis, assign_hour

def objetive_function(variables, tasks : List[Task], hours : List):
    return lpSum(variables[(t,h)]*t.professor.hours_preference[h] for t in tasks for h in hours)

def reestriction1(problem : LpProblem,variables, tasks : List[Task], hours : List, professors):
    for p in professors:
        for h in hours:
            problem += lpSum(variables[(t,h)] for t in tasks if t.professor == p) <= 1,f"restriction1{p}{h}"        
    

def reestriction2(problem : LpProblem,variable, tasks : List[Task], hours : List):
    for h in hours:
        for t in tasks:
            problem += t.professor.hours_preference[h] >= variable[(t,h)] ,f"restriction2{t}{h}"                

def reestriction3(problem : LpProblem ,variable, tasks : List[Task], hours : List, locals_num : int):
    for h in hours:
        problem += (1/5*lpSum(variable[(t,h)] for t in tasks))<=locals_num,f"restriction3{h}"

def reestriction4(problem : LpProblem, variable, tasks : List[Task], hours : List, all_thesis : List[Thesis]):
    for w in all_thesis:
        w_tasks = [t for t in tasks if t.thesis == w]
        for h in hours:
            problem += lpSum(variable[(t,h)] for t in w_tasks) == 5*variable[(w_tasks[0],h)]

def reestriction5(problem : LpProblem,variable, tasks : List[Task], hours : List):
    for t in tasks:
        problem += lpSum(lpSum(variable[(t,h)] for h in hours))==1 ,f"restriction2{t}"                

def assign_local(all_thesis : List[Thesis], hours : List, places : List[str]):
    to_assign = [0 for h in hours]
    for w in all_thesis:
        for h_index in range(0,len(hours)):
            if w.hour == hours[h_index]:
                place_index = to_assign[h_index]
                w.place = places[place_index]
                to_assign[h_index] += 1

def model(professors : List[Professor], all_thesis : List[Thesis], hours : List, places : List[str]):
    tasks = get_tasks(all_thesis)
    print("Lenths")
    print(f"Tasks: {len(tasks)}")
    print(f"Hours: {len(hours)}")
    print(f"Locals: {len(places)}")
    
    problem = LpProblem('Problem', LpMaximize)
    variables = LpVariable.dicts('variables',[(t,h) for t in tasks for h in hours],cat = 'Binary')
    problem += objetive_function(variables,tasks,hours)
    reestriction1(problem,variables,tasks,hours, professors)
    reestriction2(problem,variables,tasks,hours)
    reestriction3(problem,variables,tasks,hours, len(places))
    reestriction4(problem,variables,tasks,hours,all_thesis)
    reestriction5(problem,variables,tasks,hours)
    problem.solve()
    
    assign_hour(tasks,{key:var.varValue for key,var in variables.items()},hours)
    assign_local(all_thesis,hours,places)
    print(f"status: {problem.status}")
    return problem.status == LpStatusOptimal

