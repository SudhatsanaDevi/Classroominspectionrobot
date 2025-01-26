import turtle
import random


screen = turtle.Screen()
screen.title("Classroom Inspection Robot")
screen.bgcolor("white")


robot = turtle.Turtle()
robot.shape("turtle")
robot.color("blue")
robot.speed(1)  


camera = turtle.Turtle()
camera.shape("triangle")
camera.color("red")
camera.speed(0)  
camera.penup()
camera.goto(0, 20)  


def move_forward():
    robot.forward(10)


def rotate_camera():
    camera.right(10)  


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(rotate_camera, "a")


objects = []
for _ in range(5):
    obj = turtle.Turtle()
    obj.shape("circle")
    obj.color("green")
    obj.penup()
    obj.goto(random.randint(-200, 200), random.randint(-200, 200))
    objects.append(obj)


while True:
    for obj in objects:
        if robot.distance(obj) < 20:  
            robot.color("red")  
            camera.color("black")  
            break
    else:
        robot.color("blue")  
        camera.color("red")  

    robot.forward(1)  
    camera.setheading(robot.heading())  

    
    camera.right(1)

   
    if robot.xcor() > 300 or robot.xcor() < -300 or robot.ycor() > 300 or robot.ycor() < -300:
        robot.right(180) # Turn the robot around if it hits the boundary

screen.mainloop()
