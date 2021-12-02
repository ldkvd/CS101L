#############################################################################
##
## CS 101 Lab
## Lab 12
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM:
##
## ALGORITHM:
##  1. Start.
##  2. Import Turtle module .
##  3. Create a parent class called Point.
##      a. Create an __init__ method that has parameters self, x, y, and color.
##      b. Set the instance attibutues.
##      c. Create a draw method.
##      d. Create a draw_action method.
##  4. Create a class called Box that inherits from Point.
##      a. Create an __init__ method that has parameters self, x1, y1,
##         width, height, and color. 
##      b. Use a super class. Set the instance attibutues.
##      c. Create a draw_action method that draws the box. 
##  5. Create a class called BoxFilled.
##      a. Create an __init__ method that has parameters self, x1, y1,
##         width, height, color, and fill color. 
##      b. Use a super class. Set the self instance attibutues.
##      c. Create a draw_action method that fills in the box.
##  6. Create a class called Circle that inherits from Point.
##      a. Create an __init__ method that has parameters self, x1, y1,
##      radius, and color. Use a super class.
##      b. Set the instance attibutues.
##      c. Create a draw_action method that draws the cirlce. 
##  7. Create a class called CircleFilled.
##      a. Create an __init__ method that has parameters self, x1, y1,
##         radius, color, and fill color. 
##      b. Use a super class. Set the instance attibutues.
##      c. Create a draw_action method that fills in the circle.
##  8. Test called but calling the object (such as Box or CircleFilled) and the
##     draw method.
##  8. Stop.
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
##############################################################################

import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):

    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        '''Draws a box'''
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):

    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        '''Fills in box'''
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):

    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        '''Draws a circle'''
        turtle.circle(self.radius)

class CircleFilled(Circle):

    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        '''Fills in circle'''
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


# main
p = Point(-100, 100, 'blue')
p.draw()

b = Box(-100, 100, 50, 20, 'blue')
b.draw()

b1 = BoxFilled(1, 2, 100, 200, 'red', 'blue')
b1. draw()

c = Circle(-150, -150, 50, 'green')
c.draw()

c1 = CircleFilled(-250, -250, 50, 'green', 'purple')
c1.draw()
