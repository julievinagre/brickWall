from pickle import GLOBAL
import turtle
brick_size = 80

def square(x, y, width, color):
    turtle.penup()           
    turtle.goto(x, y)         
    turtle.fillcolor(color)   
    turtle.pendown()          
    turtle.begin_fill()       
    for count in range(4):    
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         

def drawRectangule(x, y, width, color):
    turtle.penup()            
    turtle.goto(x, y)         
    turtle.fillcolor(color)   
    turtle.pendown()          
    turtle.begin_fill()       
    for count in range(2):    
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()         

def drawBrickRow(x, y, widthBrick, color):
    turtle.penup()            
    turtle.goto(x, y)         
    turtle.fillcolor(color)   
    turtle.pendown()          
    turtle.begin_fill()       
    for i in range(6):    
        drawRectangule (x,y,widthBrick, color)
        x += widthBrick
    turtle.end_fill()         

def drawOfBrickRow(x, y, brick_size, color):
    turtle.penup()            
    turtle.goto(x, y)         
    turtle.fillcolor(color)                        
    turtle.pendown()          
    turtle.begin_fill()      
    for i in range(5):    
        drawRectangule (x,y,brick_size, color)
        x += brick_size

    turtle.end_fill() 

def main():
    _width = 480   
    color = 'white'
    global brick_size
    x = -250
    y=-220
    turtle.speed(0)
    square (x, y, _width, color)
    for i in range (11):
       y += 40
       drawRectangule (-250, y, _width,'white')      
    y = -220
    for i in range (6):
        drawBrickRow(x, y, brick_size, color)
        y +=80
    x = -210
    y= -180
    for i in range (6):
        drawOfBrickRow (x, y, brick_size, color)
        y += brick_size 
    
main()

turtle.done()

