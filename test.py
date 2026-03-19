from course import Course
from player import Player
from course_type import CourseType as ct


ex = [1,1,1,1]
typ = ["T", "T", "T", "Wettkampf"]
day = ["MI", "FR", "DI", "SA"]
dat = ["12.3", "23.3", "24.3", "26.3"]

f = Course(executed=ex, types=typ, days=day, dates=dat)
andri = Player(f, [1,1,1], "Andri")

print(f.att)
print(f.get_indices_where_not_carried(ct.exercise))
print(f.get_indices_where_not_carried(ct.wednesday))
print(andri.att)
