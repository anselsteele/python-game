from Tkinter import *
import curses
import sys
import random
import math
mode = raw_input('easy, medium, or hard?: ')
master = Tk()
master.attributes('-topmost', 1)
cvs = Canvas(master,width = 1300, height = 700)
cvs.pack()
scrn = curses.initscr()
curses.noecho()
curses.cbreak()
scrn.keypad(1)
scrn.nodelay(1)
mode = 1
if mode == 'easy':
  mode = 1
if mode == 'medium':
	mode = 3
if mode == 'hard':
	mode = 6
level = 1	
class lifedisplay:
	def __init__(self,life):
		self.life = life
	def barfill(self):
		lifebar = self.life/20
		cvs.delete('lifebar')
		counter = 1
		x1 = 1150
		x2 = 1250
		while counter <= lifebar + 1:
			lbmult = counter * 20
			cvs.create_polygon(x1,lbmult,x2,lbmult,x2,lbmult + 14, x1, lbmult + 14,tag = 'lifebar')
			counter = counter + 1

while True:
	charnum = [0,0,20,0,20,20,0,20]
	xcounter = 0
	ycounter = 0
	while ycounter <= 35:
		xcounter = 0
		while xcounter <= 55:
			xadder = xcounter * 20
			yadder = ycounter * 20
			newrect = []
			oscillator = 1
			for item in charnum:
				if oscillator == 1:
					newrect.append(item + xadder)
				if oscillator == -1:
					newrect.append(item + yadder)
				oscillator = oscillator * -1
			cvs.create_polygon(newrect,tag = 'rect')
			xcounter = xcounter + 1
		ycounter = ycounter + 1
	character = cvs.create_polygon(0,0,0,20,20,20,20,0, fill = 'green',tag = 'character')
	xmap = 0
	ymap = 0
	intmap = []
	completed = False
	thislevel = level
	difficulty = (level **2)/(level*1.5) * mode
	walls = math.ceil(difficulty * 2.5)
	coincount = difficulty * 10
	count = 0
	listcoins = []
	listwalls = []
	while count <= walls:
		wall = []
		wallrange = 2.5 * walls
		wallrange = int(wallrange)
		lenx = random.randint(1,wallrange)
		leny = random.randint(1,wallrange)
		lenx = lenx * 20
		leny = leny * 20
		if lenx >= 240:
			lenx = 240
		if leny >= 200:
			leny = 200
		if lenx >= leny:
			polylen = [lenx,20]
			horizontal = 1
		if leny >= lenx:
			polylen = [20,leny]
			horizontal = 0
		
		xbase = random.randint(1,54) * 20
		ybase = random.randint(1,34) * 20
		fullx = polylen[0] + xbase
		fully = polylen[1] + ybase
		if horizontal == 1:
			while xbase <= fullx:
				topx = xbase + 20
				topy = ybase + 20
				xmapper = xbase/20
				ymapper = ybase/20
				mapper = (xmapper,ymapper)
				polylist = [xbase,ybase,topx,ybase,topx,topy,xbase,topy]
				cvs.create_polygon(polylist,fill = 'blue',tag = 'wall')
				intmap.append(mapper)
				xbase = xbase + 20
		if horizontal == 0:
			while ybase <= fully:
				topx = xbase + 20
				topy = ybase + 20
				xmapper = xbase/20
				ymapper = ybase/20
				mapper = xmapper,ymapper
				polylist = [xbase,ybase,topx,ybase,topx,topy,xbase,topy]
				cvs.create_polygon(polylist,fill = 'blue',tag = 'wall')
				intmap.append(mapper)
				ybase = ybase + 20

		count = count + 1
	cvs.lift('wall')
	count = 0
	while count <= coincount:
		done = False
		newcoinx = random.randint(0,54)
		newcoiny = random.randint(0,34)
		randomcoin = [newcoinx,newcoiny]
		for item in intmap:
			if item[0] == randomcoin[0] and item[1] == randomcoin[1]:
				done = True

		if done == False:
			newcoinx = newcoinx * 20
			newcoiny = newcoiny * 20
			randomcoin = [newcoinx,newcoiny]
			cvs.create_polygon(newcoinx,newcoiny,(newcoinx+20),newcoiny,(newcoinx + 20),(newcoiny + 20),newcoinx,(newcoiny + 20),fill = 'orange',tag = 'coin')
			listcoins.append(randomcoin)
			count = count + 1
	coincoords = []
	for item in listcoins:
		randomx = int(item[0]/20)
		randomy = int(item[1]/20)
		randomitem = [randomx,randomy]
		coincoords.append(randomitem)
	

	coinlimit = len(coincoords)
	coins = 0
	initlife = 150
	life = int(coincount * 5 - (level**2)) + initlife
	lifebars = life/20

	counter = 1
	x1 = 1150
	x2 = 1250
	while counter < lifebars:
		lbmult = counter * 20
		cvs.create_polygon(x1,lbmult,x2,lbmult,x2,lbmult + 14, x1, lbmult + 14,fill = 'orange',tag = 'lifebar')
		counter = counter + 1

	while completed == False:
		updatelife = lifedisplay(life)
		updatelife.barfill()

		if life <= 0:
			completed = True
			level = 1
		mapcheck = 0
		a = scrn.getch()
		if a == 260:
			cvs.move('character',-20,0)
			xmap = xmap - 1
			mapcheck = 1
			life = life - 1
		if a == 261:
			cvs.move('character',20,0)
			xmap = xmap + 1
			mapcheck = 1
			life = life - 1
		if a == 259:
			cvs.move('character',0,-20)
			ymap = ymap - 1
			mapcheck = 1
			life = life - 1 
		if a == 258:
			cvs.move('character',0,20)
			ymap = ymap + 1
			mapcheck = 1
			life = life - 1
		if mapcheck == 1:
			mapthing = [xmap,ymap]
			for item in coincoords:
				if item[0] == xmap and item[1] == ymap:
					coins = coins + 1
					life = life + 1


			for item in intmap:
				if item[0] == xmap and item[1] == ymap:
						curses.endwin()
						print 'game over'
						pass

			charcoords = cvs.coords('character')
			cvs.create_polygon(charcoords,fill = 'red',tag = 'trail')
			cvs.lift('character')
			intmap.append(mapthing)
		
		if coins == coinlimit:
			completed = True
			level = level + 1
		if completed == True:
			print 'level (%d) completed' %(level)
			cvs.delete('rect')
			cvs.delete('coin')
			cvs.delete('trail')
			cvs.delete('character')
			cvs.delete('wall')
		cvs.update()
master.mainloop()
	  	
