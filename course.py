from course_type import CourseType as ct

class Course:
    def __init__(self, executed, types, days, dates):
        self.players = []
        self.att = {ct.exercise: [], ct.competition: [], ct.tuesday: [], ct.wednesday: [], ct.friday: []}

        if len(executed) == len(types) == len(days) == len(dates):
            for exec, type, day, date in zip(executed, types, days, dates):
                if type.startswith("Wettkampf"):
                    self.att[ct.competition].append([exec, date])
                elif type.startswith("T"):
                    self.att[ct.exercise].append([exec, date])
                    if day.startswith("DI"):
                        self.att[ct.tuesday].append([exec, date])
                    elif day.startswith("MI"):
                        self.att[ct.wednesday].append([exec, date])
                    elif day.startswith("FR"):
                        self.att[ct.friday].append([exec, date])
        else:
            print("init Arrays aro not the same lenght!")

    #Adds a pointer to player object
    def addPlayer(self, player):
        self.players.append(player)

    #returns number of courses of provided type
    def getNumCourses(self, type):
        return len(self.att[type])

    #returns number of carried out courses of provided type
    def getNumCarriedCourses(self, type):
        totCarr = 0
        for wasCarr in self.att[type]:
            totCarr += wasCarr[0]
        return totCarr
    
    #returns the indices where the courses did not carried out
    def getIndicesWhereNotCarried(self, type):
        indices = []
        for n, attendance in enumerate(self.att[type]):
            if not attendance[0]:
                indices.append(n)
        return indices
    
    #returns average absolute number attended  courses
    def avCourseAbs(self):
        totalAttendace = 0
        for player in self.players:
            pass #TODO Implement
        return None
    
    #returns average relative number attended  courses
    def avCourseRel(self):
        totalAttendace = 0
        for player in self.players:
            pass #TODO Implement
        return None

