import turtle
import math
from tkinter import *
import pygame


myWindow = turtle.Screen()
myWindow.bgcolor("black")
myWindow.title("Maze Game")
myWindow.setup(700, 700)

root = Tk()
root.geometry("200x200")
pygame.init()

#music to chill while playing
def play():
    pygame.mixer.music.load("lofi.mp3")
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.load("lofi.mp3")
    pygame.mixer.music.stop()

#Lofi mix
Button(root, width=20, text="Play",command=play).pack()
Button(root, width=20, text= "Pause", command=stop).pack()


# this class holds everything about the maze (walls)
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        # need penup() or else it will show trace
        self.penup()
        self.speed(0)


class Item(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# this class holds everything about the user (player)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

    def is__collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False
        
    # 4 possible directions a player can move
    
    # keeping the x coordinate in place and moving y coordinate up
    def moveUp(self):
        moveXDirection = player.xcor()
        moveYDirection = player.ycor() + 24

        # checks if theres a wall
        if (moveXDirection, moveYDirection) not in walls:
                    self.goto(moveXDirection, moveYDirection)

    # keeping the x coordinate in place and moving y coordinate down
    def moveDown(self):
        moveXDirection = player.xcor()
        moveYDirection = player.ycor() - 24

        # checks if theres a wall
        if (moveXDirection, moveYDirection) not in walls:
                    self.goto(moveXDirection, moveYDirection)
                    
    # moving the x coordinate left and keeping y coordinate in place
    def moveLeft(self):
        moveXDirection = player.xcor() -  24
        moveYDirection = player.ycor() 

        # checks if theres a wall
        if (moveXDirection, moveYDirection) not in walls:
                    self.goto(moveXDirection, moveYDirection)
    # moving the x coordinate right and keeping y coordinate in place
    def moveRight(self):
        moveXDirection = player.xcor() + 24
        moveYDirection = player.ycor() 

        # checks if theres a wall
        if (moveXDirection, moveYDirection) not in walls:
                    self.goto(moveXDirection, moveYDirection)

winPoint = []

# we can make a list of levels if we'd like and put them into the array (right now only using one level)
levels = [""]

# creating my first level (25x25) with X's being the walls and P being player
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X           P           X",
"X XXXX XXXXXXXXXXXXXX XXX",
"X XXXX      XXXXXX      X",
"X    XXXXX  XXXXXX  XXX X",
"XXXX    XX  XXXXXX  X X X",
"XXXXXX  XX  XXXXXX  X X X",
"X    X  XX  XXXXXX  X X X",
"X XXXX  XX          X   X",
"X XXXX  XXXXXXXXXXXXXXXXX",
"X                       X",
"XXXXXXX XXXXXXXXXXXXXXX X",
"XXXXXXX X        XXXXXX X",
"X   XXX XXXXXXX  XXXXXX X",
"X X XXX XX              X",
"X X     XX  XXXXXXXXXXXXX",
"X XXXXXXXX  XXXXXXXXXXXXX",
"X XXTXXXXX              X",
"X XX X   XXXXXXXXXXXXXX X",
"X XX X X                X",
"X XX X XXXXXXXXXXXXXXXXXX",
"X XX X                  X",
"X XX  XXXX XXXXX XXXXXXXX",
"X  XX          X        X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# adding the maze into the list of mazes
levels.append(level_1)

# this definition sets up the maze 
def setupMaze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            # this is just the location on the grid (0,0) being the center
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # this checks if the person is running into a wall (X)
            if character == "X":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                # this adds the coordinates to the wall list
                walls.append((screen_x, screen_y))

            # checks P player
            if character == "P":
                player.goto(screen_x, screen_y)
            
            if character == "T":
                winPoint.append(Item(screen_x, screen_y))

# creating instances
maze = Maze()
player = Player()

# wall list
walls = []

def eraseText(tortoise, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser


text = eraseText(turtle,'YOU WIN!', font = ('Courier', 30, 'italic'), align='CENTER')

def setUp():
    turtle.reset()
    text.clear()
    setupMaze(levels[1])

def exitGame():
    root.destroy()
    turtle.bye()

    
setUp()
Button(root, width=20, text= "Reset", command = setUp).pack()
Button(root, width=20, text= "Exit", command = exitGame).pack()


# For using keyboard instead of buttons
turtle.listen()
turtle.onkey(player.moveLeft, "Left")
turtle.onkey(player.moveRight, "Right")
turtle.onkey(player.moveUp, "Up")
turtle.onkey(player.moveDown, "Down")

# turn off the screen updates


game = True
while game:
    for item in winPoint:
        if player.is__collision(item):
            turtle.hideturtle()
            turtle.color('gold')
            style = ('Courier', 30, 'italic')
            turtle.write('YOU WIN!', font=style, align='CENTER')
            
    
    # updating screen
    myWindow.update()




