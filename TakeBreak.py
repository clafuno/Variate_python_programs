# Udacity course - PROGRAMMING FOUNDATIONS WITH PYTHON
# Programm 1: Take a break

import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
#time.ctime provides date and hour from the computer.

while (break_count < total_breaks):
	time.sleep(10) #Wait for x seconds
	webbrowser.open("https://www.google.com")
	break_count = break_count + 1

