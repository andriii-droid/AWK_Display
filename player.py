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