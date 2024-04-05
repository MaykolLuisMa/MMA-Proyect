import streamlit as st
import pandas
from typing import List
from Hour import Date_Controller
from Professor import Professor, load_professors, save_professors
from Thesis import Thesis, load_thesis
from datetime import *
from model import model
from Places import load_places, save_places
from utils import get_default_hour,load_stats,save_stats,do_change
def print_aignation(all_thesis : List[Thesis]):
    titles = []
    hours = []
    places = []
    for w in all_thesis:
        titles.append(w.title)
        hours.append(w.hour)
        places.append(w.place)
    dic = {"Título":titles,"Hora":hours,"Lugar":places}
    df = pandas.DataFrame(dic)
    st.table(df.set_index(df.columns[0]))

def home_page(professors : List[Professor], all_thesis : List[Thesis], places : List[str]):
    st.title("Planificación de defensa de Tesis")
    try:
        begin1,start1,end1,duration1 = load_stats()
    except:
        save_stats()
        begin1,start1,end1,duration1 = load_stats()
    date_ = st.date_input("Fecha de comienzo",value=date(begin1.year,begin1.month,begin1.day))
    time_ = st.time_input("Hora de comienzo",value=time(begin1.hour,begin1.minute))
    begin = datetime.combine(date_,time_)
    duration = st.text_input("Días de duración:",value=str(duration1))
    try:
        duration = int(duration)
    except:
        duration = 3
    st.write("Horario laboral:")
    x, y = st.columns(2)
    start = x.time_input("Abre:",value=start1)
    end = y.time_input("Cierra:",value=end1)
    acept = st.button("Aceptar")
    hours = Date_Controller().get_hours(get_default_hour(professors))
    if(acept and do_change(begin,start,end,duration)):
        Date_Controller().set_default_hour_preference(professors,datetime.combine(date_,time_))
        hours = Date_Controller().get_hours(datetime.combine(date_,time_))
        save_professors(professors)
        save_stats(begin,start,end,duration)
    asign = st.button("Asignación automática")
    if asign:
        sol = model(professors,all_thesis,hours,places)
        if(sol):
            print_aignation(all_thesis)
        else:
            st.write("No se ha podido encontrar una solución con las condiciones establecidas")

def print_professor(i : int, p : Professor):
    with st.expander(p.name):
            if p.hours_preference != None:
                for j,h in enumerate(p.hours_preference):
                    st.write(h)
                    pref = st.slider(label=f"preference{i}{j}",min_value=0,max_value=3,value=p.hours_preference[h],label_visibility="hidden")
                    p.hours_preference[h] = pref

def professor_page(professors : List[Professor]):
    st.title("Profesores")
    for i,p in enumerate(professors):
        print_professor(i,p)
    save_professors(professors)

def tesis_page(thesis : List[Thesis]):
    st.title("Tesis")
    titles = []
    mentors = []
    oponents = []
    presidents = []
    secretaries = []
    spokesmen = []
    for w in thesis:
        titles.append(w.title)
        mentors.append(w.mentor.name)
        oponents.append(w.opponent.name)
        presidents.append(w.president.name)
        secretaries.append(w.secretary.name)
        spokesmen.append(w.spokesman.name)
    df = pandas.DataFrame({"Titulo":titles,"Mentor":mentors,"Oponente":oponents,"Presidente":presidents,"Secretario":secretaries,"Vocal":spokesmen})
    st.table(df.set_index(df.columns[0]))

def delete_place(place, places : List[str]):
    places.remove(place)
    save_places(places)

def add_place(place, places : List[str]):
    if place in places:
        return
    places.append(place)
    save_places(places)

def places_page(places : List[str]):
    st.title("Locales")
    col1,col2 = st.columns([5,1])
    for c in places:
        col1.button(label=c,use_container_width=True)
        col2.button(label="Eliminar",key=c,on_click=delete_place,args=(c,places,))
    new = col1.text_input(label="Nuevo local",label_visibility='hidden')
    col1.button(label="Agregar",on_click=add_place,args=(new,places,))

options = st.sidebar.selectbox("Menu",["Home", "Profesores", "Tesis","Lugares"])
start_hour = None
professors = load_professors()
places = load_places()
all_thesis = load_thesis(professors)

if options == "Home":
    home_page(professors,all_thesis,places)
elif options == "Profesores":
    professor_page(professors)
elif options == "Tesis":
    tesis_page(all_thesis)
elif options == "Lugares":
    places_page(places)