from course_type import CourseType as ct
import sys

class Player:
    def __init__(self, course, data, name, *, coach=False):
        if len(data) != len(course.course_type):
            print(f"Anwesenheitsliste von {name} hat falsche Länge")
            sys.exit()
        self.course = course
        self.course.players.append(self)
        self.name = name
        self.coach = coach
        self.att = {ct.exercise: [], ct.competition: [], ct.tuesday: [], ct.wednesday: [], ct.friday: []}


        for type, exec in zip(self.course.course_type, data):
            self.att[type].append(exec)
            if type in {ct.tuesday, ct.wednesday, ct.friday}:
                self.att[ct.exercise].append(exec)

    def get_step_arr(self, type):
        '''Return an Array that increases by one, when attended, depending on provided course_type'''
        sum_array = []
        count = 0
        for attendance in self.att[type]:
            count += attendance
            sum_array.append(count)
        return sum_array
    
    def get_sum_abs(self, type):
        '''return total number of attended courses, depending on provided course_type'''
        return sum(self.att[type])    
    
    def get_sum_rel(self, type):
        '''return percentage of attended courses depending on provided course_type'''
        if self.course.get_num_carried_courses(type) == 0:
            return 0
        return round(self.get_sum_abs(type) / self.course.get_num_carried_courses(type) *100, 2)


