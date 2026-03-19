from course_type import CourseType as ct

class Player:
    def __init__(self, course, data, name, *, coach=False):
        self.course = course
        self.course.players.append(self)
        self.name = name
        self.coach = coach
        self.att = {ct.exercise: [], ct.competition: [], ct.tuesday: [], ct.wednesday: [], ct.friday: []}


        for type, exec in zip(course.course_type, data):
            self.att[type].append(exec)
            if type in {ct.tuesday, ct.wednesday, ct.friday}:
                self.att[ct.exercise].append(exec)