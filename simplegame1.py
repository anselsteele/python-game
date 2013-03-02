#importing math, curses and Tkinter modules; math is used for positional calculations,
#curses is used for key input, Tkinter is used for graphics.
import sys
import termios
import math
import curses
from Tkinter import *
from PIL import Image, ImageTk
master = Tk()

#creating a canvas object
cvswidth = 500
cvsheight = 500
cvs = Canvas(master, width = cvswidth, height = cvsheight)
cvs.pack()
window = Tk()

#variable assignment; xdist and y dist are looped to simulate movement
xdist = 0
ydist = 0
xcoords = 0
ycoords = 0
counter1 = 0
counter2 = 0
oldangle1 = 0

#character image files
img1 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/robot1a.gif")
img2 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/robot2a.gif")
img3 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/robot3a.gif")
img4 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/robot4a.gif")
img5 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob1a.gif")
img6 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob2a.gif")
img7 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob3a.gif")
img8 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob4a.gif")
img9 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/turret.gif")
img10 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/wheel.gif")
#img11 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img12 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img13 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img14 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img15 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img16 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img17 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img18 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img19 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img20 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img21 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img22 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img23 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img24 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img25 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img26 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img27 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img28 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img29 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img30 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img31 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img32 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img33 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img34 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img35 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")
#img36 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/")

#creating the background first causes new objects to be in the foreground
#cutting off a section of the large background that corresponds to the starting location
#the region array is used in the main loop to modify the bgdiv array by telling it which x by x "region
#of the background image is being displayed
region = (0,0)
regionx = 0
regiony = 0
bgdiv = (0,0,500,500)
bgchecker = 500
bground1 = Image.open("/Users/anselsteele/Desktop/foldpy/sprites/sanctum1.gif")
bground1crop = bground1.crop(bgdiv)
tkbg1 = ImageTk.PhotoImage(bground1crop)
bg1 = cvs.create_image(250,250, image = tkbg1, anchor = CENTER, tag = 'background1')

robot1 = cvs.create_image(50,50,image = img4, anchor = CENTER, tag='figure')
mob1 = cvs.create_image(100,100,image = img5, anchor = CENTER, tag ='mob1')
mob2 = cvs.create_image(150,150,image = img5, anchor = CENTER, tag = 'mob2')

droneimg1 = Image.open("/Users/anselsteele/Desktop/foldpy/sprites/turretcannon.gif")
dronepivot1 = droneimg1.rotate(160)
tkdrone1 = ImageTk.PhotoImage(dronepivot1)

tkimg1 = Image.open("/Users/anselsteele/Desktop/foldpy/sprites/turret.gif")
turret1 = cvs.create_image(100,200, image = tkdrone1, anchor = CENTER, tag = 'drone')

#setting up curses parameters
scrn = curses.initscr()
curses.noecho()
curses.cbreak()
scrn.keypad(1)
scrn.nodelay(1)

#the primary movement loop; while True creates an infinite loop
mapcounter = 0
counterlimit = 0
while True:
    
    #reassigns variables that may have been altered during the loop
    counter1 = (counter1 + 1)
    counter2 = (counter2 + 1)
    xdist = 0
    ydist = 0
    dispx = 0
    dispy = 0
    xtrig = 0
    ytrig = 0
    xytrig = 0
    hypo = 0
    posivx = 0
    posivy = 0
    posivx2 = 0
    posivy2 = 0
    counterval1 = 5
    counterval2 = 3
    
    #use of the .coords method to generate arrays corresponding to tagged objects
    figurecoords=cvs.coords('figure')
    mobcoords=cvs.coords('mob1')
    mob2coords=cvs.coords('mob2')
    dronecoords=cvs.coords('drone')
    
    #extracting data from the coords arrays which is assigned to variables
    xcoords = figurecoords[0]
    ycoords = figurecoords[1]
    xcoordsmob = mobcoords[0]
    ycoordsmob = mobcoords[1]
    xcoordsmob2 = mob2coords[0]
    ycoordsmob2 = mob2coords[1]
    xcoordsdrone = dronecoords[0]
    ycoordsdrone = dronecoords[1]
    
    #a method for cutting sections of a larger background picture to fit
    print mouse

    if mapcounter >= (counterlimit):
        if xcoords > 500:
            cvs.move('figure',-499,0)
            regionx = (region[0]) + 1
        if xcoords < 0:
            cvs.move('figure',499,0)
            regionx = (region[0]) - 1
        if ycoords > 500:
            cvs.move('figure',0,-499)
            regiony = (region[1]) + 1
        if ycoords < 0:
            cvs.move('figure',0,499)
            regiony = (region[1]) - 1
        bgsize = bground1.size
        bgsizex = bgsize[0]
        bgsizey = bgsize[1]
        bgdivx = 500 - bgsizex
        bgdivy = 500 - bgsizey
    
        done = False
        finalx = 0
        finaly = 0
        multicheck = 1
        while not done:
            if bgsizex - (bgchecker * multicheck) > 500:
                finalx = finalx + 1
                multicheck = multicheck + 1
            else:
                done = True
                multicheck = 1
        done = False
        while not done:
            if bgsizey - (bgchecker * multicheck) > 500:
                finaly = finaly + 1
                multicheck = multicheck + 1
            else:
                done = True
                multicheck = 1
    
    
            region = (regionx,regiony)
    
            finderx1 = (regionx * 500)
            findery1 = (regiony * 500)
    
            if regionx != finalx:
                finderx2 = ((regionx * 500) + 500)
            else:
                finderx2 =(bgsizex)
            if regiony != finaly:
                findery2 = ((regiony * 500) + 500)
            else:
                findery2 =(bgsizey)
    
        
            bgdiv = (finderx1,findery1,finderx2,findery2)
            bground1crop = bground1.crop(bgdiv)
            tkbg1 = ImageTk.PhotoImage(bground1crop)
            cvs.delete('background1')
            bg1 = cvs.create_image(250,250, image = tkbg1, anchor = CENTER, tag = 'background1')
            cvs.lower('background1')
            
            xinference1 = 500 - xcoords
            yinference2 = 500 - ycoords
            
            route1 = xinference1
            route2 = yinference2
            route3 = xcoords
            route4 = ycoords
            
            if route1 <= route2 and route1 <= route3 and route1 <= route4:
                counterlimit = route1
            if route2 <= route1 and route2 <= route3 and route2 <= route4:
                counterlimit = route2
            if route3 <= route1 and route3 <= route2 and route3 <= route4:
                counterlimit = route3
            if route4 <= route1 and route4 <= route2 and route4 <= route3:
                counterlimit = route4
            cvs.lower('background1')
            cvs.lift('figure')
                
        mapcounter = 0
                    
                
 
    
    
    #assigns a variable to a key press, allowing user input.  Depending on this value the image file of the character is changed to face
    #a direction corresponding to the key input, and the xdist or ydist variables are modified to tell how to move the character at the end
    #of the loop
    c=scrn.getch()
    if c == 260:
        xdist = (xdist - 5)
        cvs.itemconfig('figure',image = img1)
    if c == 259:
        ydist = (ydist - 5)
        cvs.itemconfig('figure',image = img3)
    if c == 258:
        ydist = (ydist + 5)
        cvs.itemconfig('figure',image = img4)
    if c == 261:
        xdist = (xdist + 5)
        cvs.itemconfig('figure',image = img2)
    
    #displacement calculation between various objects
    dispx = (xcoords - xcoordsmob)
    dispy = (ycoords - ycoordsmob)
    
    dispx1 = (xcoords - xcoordsdrone)
    dispy1 = (ycoords - ycoordsdrone)
    
    dispx2 = (xcoords - xcoordsmob2)
    dispy2 = (ycoords - ycoordsmob2)
    #creates virtual quadrants around with the object representing 0,0 on a graph by comparing its position to the character's position
    if ycoordsdrone > ycoords and xcoordsdrone > xcoords:
        quadrant = 2
    if ycoordsdrone > ycoords and xcoordsdrone < xcoords:
        quadrant = 1
    if ycoordsdrone < ycoords and xcoordsdrone > xcoords:
        quadrant = 3
    if ycoordsdrone < ycoords and xcoordsdrone < xcoords:
        quadrant = 4
        
    #creates an displacement ratio by dividing the y displacement by the x displacement
    if dispx1 != 0:
        angleratio1 = (dispy1/dispx1)
        
    #if the x displacement is zero, such as at 90 and 270 degrees, slightly adjust the ratio so that there is no divide by zero error
    #this adjustment will later be corrected when the angle it produces through inverse tan is turned into an integer
    else:
        angleratio1 = (dispy1/(dispx1-0.001))
    
    #use the displacement ratio with the arc, or inverse tangent, to calculate an angle between the object.  This angle is in radians, so
    #it must be converted into degrees and then turned into an integer before it can be used effectively.
    rawanglerad1 = math.atan(angleratio1)
    rawangle1 = math.degrees(rawanglerad1)
    newangle1 = int(rawangle1)

    #imports the image of the object, adds one to oldangle1 untill it is equal to newangle1
    while newangle1 != oldangle1:
        if newangle1 > oldangle1:
            oldangle1 = (oldangle1 + 1)
        if newangle1 < oldangle1:
            oldangle1 = (oldangle1 - 1)
        if newangle1 == oldangle1:
            continue
        
    #rotates droneimg1 by oldangle1, the quadrants fix the 180 degree flipping that occurs in the 2nd and 3rd quadrant from the tangent function
    if quadrant == 1 or quadrant == 4:
        dronepivot1 = droneimg1.rotate(oldangle1 * -1)
    if quadrant == 2 or quadrant == 3:
        dronepivot1 = droneimg1.rotate((oldangle1 * -1)+180)
    
    #creates a new image using the rotated dronepivot1 as an argument.  Deletes the old image of the previous drone.
    tkdrone1 = ImageTk.PhotoImage(dronepivot1)
    cvs.delete('drone')
    turret1 = cvs.create_image(100,200, image = tkdrone1, anchor = CENTER, tag = 'drone')

    #makes the object move every nth loop to follow the character.  The object will turn so that it is facing the same way as the character
    #by changing its image file depending on the x and y displacement ratio between the character and the object
    if counter1 == counterval1:
        if dispx > 0:
           posivx = 1
           if abs(dispx) > abs(dispy):
                cvs.itemconfig('mob1',image = img7)
        elif dispx < 0:
            posivx = -1
            if abs(dispx) > abs(dispy):
                cvs.itemconfig('mob1',image = img6)
        else:
            posivx = 0
        if dispy > 0:
            posivy = 1
            if abs(dispy) > abs(dispx):
                cvs.itemconfig('mob1',image = img5)
        elif dispy < 0:
            posivy = -1
            if abs(dispy) > abs(dispx):
                cvs.itemconfig('mob1',image = img8)
        else:
            posivy = 0
        counter1 = 0
        
    if counter2 == counterval2:
        if dispx2 > 0:
           posivx2 = 1
           if abs(dispx2) > abs(dispy2):
                cvs.itemconfig('mob2',image = img7)
        elif dispx2 < 0:
            posivx2 = -1
            if abs(dispx2) > abs(dispy2):
                cvs.itemconfig('mob2',image = img6)
        else:
            posivx2 = 0
        if dispy2 > 0:
            posivy2 = 1
            if abs(dispy2) > abs(dispx2):
                cvs.itemconfig('mob2',image = img5)
        elif dispy2 < 0:
            posivy2 = -1
            if abs(dispy2) > abs(dispx2):
                cvs.itemconfig('mob2',image = img8)
        else:
            posivy2 = 0
        counter2 = 0
        
    #moves the character and objects responding to the character by the amount determined by the arrow keys
    cvs.move('figure',xdist,ydist)
    cvs.move('mob1',posivx,posivy)
    cvs.move('mob2',posivx2,posivy2)
    
    #finds the coordinates of the character and other objects and then assigns their y position, the first number in the .coords array, to new variables.
    figurecoords=cvs.coords('figure')
    mobcoords=cvs.coords('mob1')
    mob2coords = cvs.coords('mob2')
    ycoords = figurecoords[1]
    ycoordsmob = mobcoords[1]
    
    #makes it so that the character will appear behind an object if it is higher on the screen than it, and in front if it is lower.
    if ycoords < (ycoordsmob):
        cvs.lift('mob1')
    else:
        cvs.lift('figure')
    if ycoords < (ycoordsmob2):
        cvs.lift('mob2')
    else:
        cvs.lift('figure')
            
    cvs.update()
    mapcounter = mapcounter + 5
    print region
master.mainloop()

#these commands break down curses
#curses.nocbreak(); scrn.keypad(0); curses.echo()
#curses.endwin() 
