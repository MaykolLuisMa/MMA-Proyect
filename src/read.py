import pandas
from Thesis import Thesis
import streamlit as st

def get_past_dates():
    file = pandas.read_excel("data/tribunales.xlsx", engine='openpyxl')
    all_thesis = []
    professors = []
    places = []
    form = ['Día','Hora','Lugar','Estudiante','Tutor','Presidente','Secretario','Vocal','Oponente']

    for d in file.iloc:
        if all([type(s) != str or is_empty(s) for s in d]):
            continue
        if any(s in form for s in d):
            continue

        members = [d['Estudiante'],
                   extract_professor(d['Tutor']),
                   extract_professor(d['Oponente']),
                   extract_professor(d['Presidente']),
                   extract_professor(d['Secretario']),
                   extract_professor(d['Vocal'])
                   ]
        
        w = Thesis(f"Tesis de {members[0]}",members[1],members[2],members[3],members[4],members[5])
        place = d['Lugar']
        all_thesis.append(w)
        places.append(place)
        for rol in members[1:]:
            professors.extend(rol)
        professors = list(set(professors))
        places = list(set(places))
        all_thesis = list(set(all_thesis))
    return all_thesis, professors, places

def is_empty(field : str):
    for c in field:
        if c == '?':
            return True
    return False
def show_error(message):
    st.title = "Error detectado en la tabla"
    st.write(message)
    while(True): pass
def extract_professor(professors : str):
    #print(professors)
    if is_empty(professors):
        show_error(f"No se admiten datos inciertos como {professors}")
    if type(professors) is not str:
        show_error(f"Se encontó una casilla con datos no admisibles")
    return [p.strip() for p in professors.split(",")]

#_, p, _ = get_past_dates()
#print(p)

