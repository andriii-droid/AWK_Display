class Player:
    def __init__(self, course, data, name, *, coach=False):
        self.course = course
        self.course.players.append(self)
        self.name = name
        self.coach = coach
