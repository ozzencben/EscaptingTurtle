import turtle
import random


screen = turtle.Screen()
screen.setup(width=700, height=700)
root = screen.getcanvas().master
root.resizable(width=False, height=False )
screen.tracer(0)

writen_turtle = turtle.Turtle()
writen_turtle.hideturtle()
writen_turtle.penup()
writen_turtle.goto(-50,300)
writen_turtle.write("Score :", align="center", font=("Montserrat", 15,"normal"))

# Skor sayacını tutan değişken ve yazan turtle
counter = 0
counter_turtle = turtle.Turtle()
counter_turtle.hideturtle()
counter_turtle.penup()
counter_turtle.goto(0, 300)
counter_turtle.write(f"{counter}", align="center", font=("montserrat", 15, "normal"))

def update_score():
    counter_turtle.clear()
    counter_turtle.write(f"{counter}", align="center", font=("montserrat", 15, "normal"))

def click_turtle(x, y):
    global counter
    counter += 1
    update_score()

timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(-50, 275)
timer_turtle.write("Time : ", align="center", font=("Montserrat", 15, "normal"))

time_counter_turtle = turtle.Turtle()
time_counter_turtle.hideturtle()

t = 90
def update_counter():
    global t
    time_counter_turtle.clear()
    time_counter_turtle.penup()
    time_counter_turtle.goto(15, 275)
    dakika = t // 60
    saniye = t % 60
    formatted_time = f"{dakika:02d}:{saniye:02d}"
    time_counter_turtle.write(formatted_time, align="center", font=("montserrat", 15, "normal"))
    t -= 1
    if t >= 0:
        screen.ontimer(update_counter, 1000)
    else:
        time_counter_turtle.clear()
        time_counter_turtle.goto(25, 275)
        time_counter_turtle.write("Time is up!", align="center", font=("montserrat", 15, "normal"))
update_counter()
screen.tracer(1)

screen_width = screen.window_width() / 2
screen_height = screen.window_height() / 2

turtle_figure = turtle.Turtle()
turtle_figure.shape("turtle")
turtle_figure.shapesize(2,2,2.5)
turtle_figure.onclick(click_turtle)

move_timer = 0
def move_it():
    global move_timer
    turtle_figure.clear()
    turtle_figure.penup()
    rnd_forward = random.randint(0,300)
    rnd_angle = random.randint(0, 180)
    rnd_return = random.randint(0,300)
    turtle_figure.forward(rnd_forward)
    turtle_figure.right(rnd_angle)
    x, y = turtle_figure.position()

    if not (-screen_width < x < screen_width and -screen_height < y < screen_height):
        return_angle = turtle_figure.towards(rnd_return, rnd_return)
        turtle_figure.setheading(return_angle)
        turtle_figure.goto(rnd_return, rnd_return)
    if t >= 0:
        move_timer = screen.ontimer(move_it, 100)
    else:
        turtle_figure.onclick(None)
        if move_timer is not None:
            move_timer = None

move_it()

turtle.mainloop()

