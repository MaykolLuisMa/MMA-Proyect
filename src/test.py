from pulp import *
from Professor import Professor, save_professors, load_professors
from Thesis import Thesis, save_thesis, load_thesis
from Places import load_places
from Hour import Date_Controller
from model import model
import datetime
from Hour import Date_Controller
p = [Professor("Albert Einstein"),Professor("Alan Turing"), Professor("Isaac Newton"), Professor("Pitágoras de Samos"), Professor("Euclides"),Professor("Tales de Mileto"), Professor("Rene Descartes"), Professor("Arquimedes de Siracusa"), Professor("Sophie Germain"), Professor("Emmy Noether")]
w = [Thesis("Title1",p[0],p[1],p[2],p[3],p[4]),Thesis("Title2",p[5],p[6],p[7],p[8],p[9]),Thesis("Title3",p[1],p[3],p[5],p[7],p[9]),Thesis("Title4",p[0],p[2],p[4],p[6],p[8])]
start = datetime.datetime(2000,1,1,1,1,1,1)
h = Date_Controller().get_hours(start)
Date_Controller().set_default_hour_preference(p,start)

#p = load_professors()
#w = load_thesis(p)
l = load_places()
l = ["local"]
#h = Date_Controller().get_hours(list(p[0].hours_preference.keys())[0])

#for h1 in h:
#    print(h1)

model(p,w,h,l)
for i in w:
    print(i.hour)
#print(l)
#save_professors(p)
#professors = load_professors()
#for i in professors:
#    print(i.name)
#    print(type(i.hours_preference))

#save_thesis(w)
#all_thesis = load_thesis(p)
#for i in all_thesis:
#    print(i.title)  
#    print(type(i.mentor))
#    print(type(i.hour))
