# -*- coding: utf-8 -*-
import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on " + time.ctime())

while (break_count < total_breaks):
    time.sleep(0.5*60*60)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1