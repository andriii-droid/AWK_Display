class Course:
    players = [] #Contains a list of all Players of that attended the course
    att = {"Exercise": [], "Competition": [], "Tuesday": [], "Wednesday": [], "Friday": []}

    def __init__(self, executed, types, days, dates):
        if len(executed) == len(types) == len(days) == len(dates):
            for exec, type, day, date in zip(executed, types, days, dates):
                if type.startswith("Wettkampf"):
                    self.att["Competition"].append([exec, date])
                elif type.startswith("T"):
                    self.att["Exercise"].append([exec, date])
                    if day.startswith("DI"):
                        self.att["Tuesday"].append([exec, date])
                    elif day.startswith("MI"):
                        self.att["Wednesday"].append([exec, date])
                    elif day.startswith("FR"):
                        self.att["Friday"].append([exec, date])
        else:
            print("init Arrays aro not the same lenght!")