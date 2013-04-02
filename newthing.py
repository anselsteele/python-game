from Tkinter import *
import curses
import sys
master = Tk()
cvs = Canvas(master,width = 500, height = 500)
cvs.pack()
scrn = curses.initscr()
curses.noecho()
curses.cbreak()
scrn.keypad(1)
scrn.nodelay(1)
while True:
  a = scrn.getch()
	print a
