from course import Course
from player import Player
from course_type import CourseType as ct
from awk_table import AWKTable as awkt

from nicegui import ui

ex = [1,1,1,1]
typ = ["T", "T", "T", "Wettkampf"]
day = ["MI", "FR", "DI", "SA"]
dat = ["12.3", "23.3", "24.3", "26.3"]

f = Course(executed=ex, types=typ, days=day, dates=dat)
andri = Player(f, [1,0,1,1], "Andri", coach=False)

awkt(f, coach=False)

ui.run(dark=True)