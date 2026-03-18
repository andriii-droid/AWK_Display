from course import Course

ex = [1,1,1,1]
typ = ["T", "T", "T", "Wettkampf"]
day = ["MI", "FR", "DI", "SA"]
dat = ["12.3", "23.3", "24.3", "26.3"]

f = Course(executed=ex, types=typ, days=day, dates=dat)

print(f.att)
print(f.getIndicesWhereNotCarried("Exercise"))
print(f.getIndicesWhereNotCarried("Wednesday"))