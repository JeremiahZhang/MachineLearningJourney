# -*- coding: utf-8 -*-
import time
import webbrowser

total_breaks = 10
break_count = 0

print ("This program started on " + time.ctime())

while (break_count < total_breaks):
    time.sleep(30*60)
    webbrowser.open("http://www.zanmeishi.com/player/zan.html")
    print ('Have a nice music, and praise the Lord! ^-^!')
    time.sleep(5*60)
    break_count += 1
    print (break_count)