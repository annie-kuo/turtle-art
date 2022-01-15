# Annie Kuo

# This program creates an artwork by drawing a simple scenery.
# The scenery is composed of a rainbow, a sun, and a flower.
# Some details are decided by the user's inputs.


# import modules to be used
import turtle
import random as r
        
# define some useful functions that will help create artwork

def draw_flower(radius, num_of_petals):
    """ (int,int) -> NoneType

    The function takes in an int representing the radius of the petals
    and an int representing the number of petals of the flower that the function will draw.
    
    """
    # create turtle object and set properties
    stem = turtle.Turtle()
    stem.speed(10)
    stem.color("darkseagreen")
    stem.fillcolor("darkseagreen")

    petal = turtle.Turtle()
    petal.speed("fastest")
    petal.color("pink")
    petal.fillcolor("crimson")
    
    # Part 1: Draw the stem of the flower
    stem.right(125)
    stem.circle(200,75)
    
    # Part 2: Draw the leaf on the stem
    stem.begin_fill()
    stem.left(50)
    stem.circle(80,120)
    stem.left(60)
    stem.circle(80,120)
    stem.end_fill()
    
    # Part 3: Draw the ground
    stem.penup()
    stem.goto(-425,-242)
    stem.pendown()
    
    stem.begin_fill()
    stem.left(120)
    for i in range(31):
        stem.forward(25)
        stem.right(120)
        stem.forward(25)
        stem.left(120)
    stem.goto(425,-242)
    stem.end_fill()
    
    stem.hideturtle()
    
    # Part 4: Draw head of the flower
    petal.begin_fill()
    
    for num in range(num_of_petals):
        petal.circle(radius,60)
        petal.left(120)
        petal.circle(radius,60)
        petal.left(360/num_of_petals)
        
    petal.end_fill()
    petal.hideturtle()



def draw_rainbow(x,y):
    """ (int,int) -> NoneType

    The function takes in two integers x and y representing the position
    (x,y) at which a rainbow will be drawn.
    
    """
    # create turtle objects and set properties
    rainbow = turtle.Turtle()
    rainbow.speed(10)
    
    clouds= turtle.Turtle()
    clouds.speed(10)
    clouds.color("LightSkyBlue")
    clouds.fillcolor("LightSkyBlue")
    
    # Part 1: Draw rainbow arcs
    
    # initial radius and position
    radius = 120
    rainbow.penup()
    rainbow.goto(x,y)
    rainbow.pendown()
    
    # draw arc in each color with decreasing radius each time
    rainbow_colors=["red","orange","yellow","green","blue","indigo","violet","white"]
       
    for color in rainbow_colors:
        rainbow.color(color)
        rainbow.fillcolor(color)
        rainbow.begin_fill()
        
        rainbow.left(90)
        rainbow.circle(radius,180)
        rainbow.left(90)
        rainbow.end_fill()
        
        # come back to initial position with a gap of 10 pixels
        rainbow.penup()
        rainbow.forward(2*radius - 10)
        rainbow.pendown()
        radius -= 10
    rainbow.hideturtle()
    
    # Part 2: Draw clouds
    
    # draw first cloud
    clouds.penup()
    clouds.goto(-175 +x ,-35 +y)
    clouds.pendown()
    
    clouds.begin_fill()
    for cloud_bump in range(6):
        cloud_radius = 20
        clouds.circle(cloud_radius,225)
        clouds.right(165)
    clouds.end_fill()
    
    # draw second cloud
    clouds.penup()
    clouds.goto(x,-35 +y)
    clouds.pendown()
    
    clouds.begin_fill()
    for loop in range(6):
        cloud_radius = 20
        clouds.circle(cloud_radius,225)
        clouds.right(165)
    clouds.end_fill()
    
    clouds.hideturtle()
    


def draw_sun():
    """ () -> NoneType

    The function draws a sun with 3 different colors at the top right corner.
    
    """
    # create turtle object and set properties
    sun= turtle.Turtle()
    sun.speed("fastest")
    
    # Part 1: Draw the most spread-out sunshine
    sun.color("khaki")
    sun.penup()
    sun.goto(375,145)
    sun.pendown()
    
    for i in range(100):
        sun.left(115)
        sun.forward(250)
        
    # Part 2: Draw the second level of sunshine
    sun.color("gold")
    sun.penup()
    sun.goto(323,135)
    sun.pendown()
    
    for i in range(100):
        sun.left(115)
        sun.forward(200)  
        
    # Part 3: Draw the sun
    sun.color("yellow")
    sun.penup()
    sun.goto(277,145) #277,145
    sun.pendown()
    
    for i in range(75):
        sun.left(115)
        sun.forward(150)



def signature():
    """ () -> NoneType

    This function draws the letter A as a signature with a thickness of 5 pixels
    
    """
    # create turtle objects and set properties    
    sign= turtle.Turtle()
    sign.color("grey")
    
    # draw the letter A
    
    # go to initial position
    sign.penup()
    sign.goto(415,-210)
    sign.pendown()
    
    # draw the letter 5 times with a horizontal translation of 1 pixel to create thickness
    thickness = 1
    while thickness <5:
        # draw letter a
        sign.right(160)
        sign.forward(45)
        sign.circle(8,240)
        sign.forward(50)
        sign.right(155)
        sign.forward(50)
        sign.circle(8,90)
        sign.forward(10)
        
        # move to next position
        sign.penup()
        sign.goto(415+thickness,-210)
        sign.right(15)
        sign.pendown()
        thickness += 1
        
    sign.hideturtle()
    


# create function that calls other functions to create artwork

def my_artwork():
    """ () -> NoneType

    This function calls other functions as necessary to draw a simple scenery.
    The scenery is composed of a rainbow at the top left corner, a sun at the top right corner,
    and a flower with a number of petals determined by the user's input,
    and whose petals have a random radius.
    The function adds a signature ('A') at the bottom right corner.
    
    """
    # greet user
    print("Hi there! We will be drawing a simple scenery composed of a flower, a rainbow, and a sun! The artist will sign at the end. \n")

    # draw a flower with the user's choice of number of petals
    # and with a random size of petals that will fit within the window
    random_petal_size= r.randint(50,200)
    
    print("You get to choose how many petals you want the flower to have!")
    print("For best aesthetic results, choose a multiple of 15 (eg. 15, 45, 90).")
    print("Note that some integers, such as some divisors of 360 (eg. 3, 30, 60) and some of their multiples (eg. 75), will draw overlapping, indistinguishable petals.")
    
    num_of_petals= int(input("Enter your desired number of petals here: "))
    draw_flower(random_petal_size, num_of_petals)

    # draw the rainbow
    draw_rainbow(-185,200)

    # draw the sun
    draw_sun()

    # add signature (A)
    signature()
    
    # announce the completion of the artwork
    print("\nOur artwork has been created! Voilà!")
