from datetime import datetime, timedelta
from copy import copy, deepcopy
from typing import List
from Professor import Professor
class Date_Controller:
    total_days = 3.0
    tesis_duration = timedelta(hours=1.0)
    start_hour = 9
    finish_hour = 19
    def get_finish_date(self, start_date : datetime):
        finish_date = start_date + timedelta(days=self.total_days-1)
        finish_date = finish_date.replace(hour=self.finish_hour)
        return finish_date

    def get_hours(self, start_date : datetime):
        start_date = max(datetime(start_date.year,start_date.month,start_date.day,self.start_hour,0),start_date)
        date = start_date
        finish_date = self.get_finish_date(start_date)
        hours = []
        while (date < finish_date):
            if date.hour < self.finish_hour and date.hour >= self.start_hour:
                hours.append(copy(date))
            date += self.tesis_duration
        return hours
    def set_default_hour_preference(self, professors : List[Professor], start_date):
        hours = self.get_hours(start_date)
        for p in professors:
            p.hours_preference = {h:3 for h in hours}
