from course_type import CourseType as ct
import sys
from page import Page as pg

class Course:
    def __init__(self, executed, types, days, dates, name):
        self.players = []
        self. name = name
        self.att = {ct.exercise: [], ct.competition: [], ct.tuesday: [], ct.wednesday: [], ct.friday: []}

        self.course_type = []
        if len(executed) == len(types) == len(days) == len(dates):
            for type, day in zip(types, days):
                if type.startswith("Wettkampf") or type.startswith("TT"):
                    self.course_type.append(ct.competition)
                elif type.startswith("T"):
                    if day.startswith("DI"):
                        self.course_type.append(ct.tuesday)
                    elif day.startswith("MI"):
                        self.course_type.append(ct.wednesday)
                    elif day.startswith("FR"):
                        self.course_type.append(ct.friday)
        else:
            print("init Arrays aro not the same lenght!")
            sys.exit()
        
        for type, exec, date in zip(self.course_type, executed, dates):
            self.att[type].append([exec, date])
            if type in {ct.tuesday, ct.wednesday, ct.friday}:
                self.att[ct.exercise].append([exec, date])

        self.page = pg(self)
        

    def add_player(self, player):
        '''Add a pointer to player object'''
        self.players.append(player)

    def get_num_courses(self, type):
        '''return number of courses of provided type'''
        return len(self.att[type])

    def get_num_carried_courses(self, type):
        '''return number of carried out courses of provided type'''
        totCarr = 0
        for wasCarr in self.att[type]:
            totCarr += wasCarr[0]
        return totCarr
    
    def get_indices_where_not_carried(self, type):
        '''return the indices where the courses did not carrie out'''
        indices = []
        for n, attendance in enumerate(self.att[type]):
            if not attendance[0]:
                indices.append(n)
        return indices
    
    def get_date_array(self, type):
        '''return an Array of the dates depending on the type'''
        return [date[1] for date in self.att[type]]
    
    def av_course_abs(self, type):
        '''return average absolute number attended courses of provided type'''
        return sum(self.players.get_sum_abs(type)) / len(self.players)
    
    def av_course_rel(self, type):
        '''return average relative number attended  courses of provided type'''
        return round(sum(self.players.get_sum_rel(type)) / len(self.players), 2)


