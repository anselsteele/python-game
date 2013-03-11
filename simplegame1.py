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
img1 = [300, 300, 290, 220, 280, 220, 270, 270, 270, 300, 280, 320, 260, 320, 250, 300, 250, 290, 250, 280, 270, 220, 270, 220, 270, 200, 290, 200, 300, 200, 300, 190, 290, 190, 290, 150, 340, 150, 340, 190, 330, 190, 330, 200, 360, 200, 360, 220, 380, 280, 380, 300, 370, 320, 350, 320, 360, 300, 360, 280, 350, 220, 340, 220, 330, 300, 340, 300, 340, 390, 370, 390, 370, 400, 320, 400, 320, 300, 310, 300, 310, 400, 260, 400, 260, 390, 290, 390, 290, 300, 300, 300]

img5 = [300, 300, 300, 370, 320, 380, 310, 390, 310, 450, 300, 460, 300, 470, 310, 480, 310, 540, 280, 550, 270, 560, 270, 570, 340, 570, 340, 550, 330, 540, 340, 500, 340, 460, 330, 450, 340, 440, 350, 380, 360, 380, 370, 440, 380, 450, 370, 460, 370, 500, 380, 540, 370, 550, 370, 570, 440, 570, 440, 560, 430, 550, 400, 540, 400, 480, 410, 470, 410, 460, 400, 450, 400, 390, 390, 380, 410, 370, 410, 300, 400, 260, 400, 250, 410, 250, 430, 320, 430, 380, 420, 390, 410, 410, 410, 420, 420, 440, 430, 450, 420, 430, 420, 420, 420, 410, 430, 390, 440, 390, 450, 410, 450, 430, 440, 450, 450, 440, 460, 420, 460, 410, 450, 390, 440, 380, 450, 360, 450, 330, 460, 320, 450, 310, 430, 250, 430, 240, 410, 230, 390, 220, 380, 210, 500, 420, 380, 210, 380, 200, 390, 200, 390, 170, 380, 150, 370, 140, 360, 140, 350, 140, 340, 150, 330, 170, 330, 200, 340, 200, 340, 210, 330, 220, 290, 240, 280, 250, 260, 310, 250, 320, 260, 330, 260, 360, 270, 380, 260, 390, 250, 410, 250, 420, 260, 440, 270, 450, 260, 430, 260, 410, 270, 390, 280, 390, 290, 410, 290, 420, 290, 430, 280, 450, 290, 440, 300, 420, 300, 410, 290, 390, 280, 380, 280, 320, 300, 250, 310, 250, 300, 300]
img6 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob2a.gif")
img7 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob3a.gif")
img8 = PhotoImage(file = "/Users/anselsteele/Desktop/foldpy/sprites/mob4a.gif")
img9 = [200, 200, 230, 170, 260, 150, 290, 140, 320, 140, 350, 150, 380, 170, 410, 200, 430, 230, 440, 260, 440, 290, 430, 320, 410, 350, 380, 380, 350, 400, 330, 410, 330, 590, 280, 590, 280, 410, 260, 400, 230, 380, 200, 350, 180, 320, 170, 290, 170, 260, 180, 230, 200, 200]


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

robot1 = cvs.create_polygon(img1, tag='figure')
mob1 = cvs.create_polygon(img5,tag ='mob1')
mob2 = cvs.create_image(150,150,image = img5, anchor = CENTER, tag = 'mob2')

droneimg1 = cvs.create_polygon(img9,tag = 'drone1')
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

