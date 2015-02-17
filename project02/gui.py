import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
square = turtle.Turtle()    # Create a turtle, assign to alex
square.shape("square")
wn.screensize(600,400)
wn.bgpic("grid2.gif")


square.forward(50)          # Tell alex to move forward by 50 units
square.left(90)             # Tell alex to turn by 90 degrees
square.forward(30)          # Complete the second side of a rectangle

turtle.done()