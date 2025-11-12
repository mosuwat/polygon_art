import random, turtle

class Polygon:
    def __init__(self, num_sides = 3, num_inside = 0):
        self.num_sides = num_sides
        self.num_inside = num_inside
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def draw(self):
        self.draw_polygon()
        for i in range (self.num_inside): 
            # specify a reduction ratio to draw a smaller polygon inside the one above
            reduction_ratio = 0.618

            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            self.size *= reduction_ratio

            # draw the second polygon embedded inside the original 
            self.draw_polygon()

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

choice = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")
try:
    choice = int(choice)
    if choice == 1:
        shape_num = random.randint(15, 25)
        for i in range(shape_num):
            shape = Polygon(3, 0)
            shape.draw()
    elif choice == 2:
        shape_num = random.randint(15, 25)
        for i in range(shape_num):
            shape = Polygon(4, 0)
            shape.draw()
    elif choice == 3:
        shape_num = random.randint(15, 25)
        for i in range(shape_num):
            shape = Polygon(5, 0)
            shape.draw()
    else:
        raise ValueError
except:
    print("Please choose an integer between 1-9!")

turtle.done()