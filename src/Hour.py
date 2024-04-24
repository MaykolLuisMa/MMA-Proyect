from datetime import datetime, timedelta
from copy import copy, deepcopy
from typing import List
class Date_Controller:
    
    tesis_duration = timedelta(hours=1.0)
    def __init__(self,total_days, start,finish):
        self.total_days = total_days
        self.start = start
        self.finish = finish

    def get_finish_all_date(self, begin_all : datetime):
        finish_date = begin_all + timedelta(days=self.total_days-1)
        finish_date = finish_date.replace(hour=self.finish.hour)
        finish_date = finish_date.replace(minute=self.finish.minute)
        return finish_date

    def get_hours(self, begin_all : datetime):
        begin_all = max(datetime(begin_all.year,begin_all.month,begin_all.day,self.start.hour,self.start.minute),begin_all)
        #print("begin all")
        #print(begin_all)
        #print("finish all")
        date = begin_all
        finish_date = self.get_finish_all_date(begin_all)
        #print(finish_date)
        #input()
        hours = []
        while (date < finish_date):
            if date.hour < self.finish.hour and date.hour >= self.start.hour:
                hours.append(copy(date))
            date += self.tesis_duration
        #print("hours")
        #print(hours)
        #input()
        return hours
    def set_default_hour_preference(self, professors : List, begin_all):
        hours = self.get_hours(begin_all)
        for p in professors:
            p.hours_preference = {h:3 for h in hours}
