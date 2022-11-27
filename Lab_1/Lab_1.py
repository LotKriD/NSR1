import pandas as pd
import os

times = []
times_mor = []
times_day = []
times_ev = []
times_night = []

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'ufo_sighting_data.csv')
data = pd.read_csv(path)

for i in data['Date_time']:
    time = i.split(' ')[1]
    times.append(time)

for i in times:
    t = i.split(':')
    minut = int(t[0]) * 60 + int(t[1])
    if(minut > 0 and minut <= 360):
        times_night.append(i)
    elif (minut > 360 and minut <= 720):
        times_mor.append(i)
    elif (minut > 720 and minut <= 1080):
        times_day.append(i)
    else:
        times_ev.append(i)
    
d = ""

print("Morning: ")
d = d + "Morning:\n"
for i in times_mor:
    d = d + str(i) + "\n"
    print(i)

print("Day: ")
d = d + "Day:\n"
for i in times_day:
    d = d + str(i) + "\n"
    print(i)

print("Evening: ")
d = d + "Evening:\n"
for i in times_ev:
    d = d + str(i) + "\n"
    print(i)

print("Night: ")
d = d + "Night:\n"
for i in times_night:
    d = d + str(i) + "\n"
    print(i)

file = open('test.txt', 'w')
file.write(d)
file.close()

#for i in data['longitude']:
#    if i < min:
#        min = i
#    if i > max:
#        max = i
#    mid = mid + i

#mid = mid / data.shape[0]

#file = open('test.txt', 'w')
#file.write(str(data.shape) + '\n' +
#str(data.dtypes) + '\nmax: ' + str(max) +
#'\nmin: ' + str(min) + '\nmid: ' + str(mid))
#file.close()