import plotext as plt
import csv

x = []
y = []
x2 = []
y2 = []
with open('/home/peanutstick/Documents/scripts/python/bat-stat/bat-data1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[2]))

with open('/home/peanutstick/Documents/scripts/python/bat-stat/bat-data2.csv','r') as csvfile:
    plots2 = csv.reader(csvfile, delimiter=',')
    for row in plots2:
        x2.append(int(row[0]))
        y2.append(int(row[2]))

plt.plot(x2, y2, color = "yellow", marker = "small")
plt.plot(x,y, color = "white", marker = "small")# label = "battery")
plt.xlabel('Uptime (min)')
plt.ylabel('Battery status (%)')
plt.title("Battery usage")
plt.ylim([0, 100])
plt.plotsize(210, 80)
plt.grid(True)
plt.axes_color("none")
plt.canvas_color("none")
plt.ticks_color("green")
plt.ticks(11)
plt.show() 
