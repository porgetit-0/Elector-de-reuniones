from random import randint

names = ["Meet","Alejandro","Jennyfer","Kevin"]
meetings = []

for i in range(0, 10):
    number = randint(0,len(names)-1)
    meetings.append(names[number])

print(meetings)