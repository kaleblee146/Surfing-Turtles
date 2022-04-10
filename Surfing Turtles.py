# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
import random
win = turtle.Screen()
win.title("Beach Hacks 2022:Surfing Turtles and Snacking Sharks")
win.bgcolor("sky blue")
win.setup(width=800, height=600)
win.tracer(0)

# Surfing Turtle- can start as a green circle, can place circle over an oval to represent surf board
surfer = turtle.Turtle()
surfer.speed(0)
surfer.shape("turtle")
surfer.left(90)
surfer.color("green")
surfer.penup()
surfer.goto(0, 0)

# attributes of shark 1
shark1 = turtle.Turtle()
shark1.speed(0)
shark1.shape("circle")
shark1.color("light blue")
shark1.shapesize(stretch_wid=5, stretch_len=2)
shark1.penup()
shark1Start = random.randint(-(win.window_width()/2), (win.window_width()/2))
shark1.goto(shark1Start, (win.window_height()/2+250))
shark1.dy = .4

# attributes of shark 2
shark2 = turtle.Turtle()
shark2.speed(0)
shark2.shape("triangle")
shark2.color("grey")
shark2.shapesize(stretch_wid=5, stretch_len=2)
shark2.penup()
shark2Start = random.randint(-(win.window_width()/2), (win.window_width()/2))
shark2.goto(shark2Start, (win.window_height()/2+250))
shark2.dy = .6

# attributes of shark 3
shark3 = turtle.Turtle()
shark3.speed(0)
shark3.shape("circle")
shark3.color("grey")
shark3Width = 3
shark3.shapesize(stretch_wid=shark3Width, stretch_len=2)
shark3.penup()
shark3Start = random.randint(-(win.window_width()/2), (win.window_width()/2))
shark3.goto(shark3Start, (win.window_height()/2+250))
shark3.dy = .8

# attributes of shark 4
shark4 = turtle.Turtle()
shark4.speed(0)
shark4.shape("circle")
shark4.color("grey")
shark4Length = 4
shark4.shapesize(stretch_wid=5, stretch_len=shark4Length)
shark4.penup()
shark4Start = random.randint(-(win.window_width()/2), (win.window_width()/2))
shark4.goto(shark4Start, (win.window_height()/2+250))
shark4.dy = .2

# boolean that states that the game isn't over until something happens to the surfer
gameOver = False
resetGame = False

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

# lets surfer go up
def surfer_up():
    y = surfer.ycor()
    y += 20
    surfer.sety(y)

# lets surfer go down
def surfer_down():
    y = surfer.ycor()
    y += -20
    surfer.sety(y)

# lets surfer go left
def surfer_left():
    x = surfer.xcor()
    x += -20
    surfer.setx(x)

# lets surfer go right
def surfer_right():
    x = surfer.xcor()
    x += 20
    surfer.setx(x)

# sets False
def set_false(x):
    x = False
    return x

# leaves the loopo
def leave_loop(x):
    new_x = set_false(x[0])
    x[0] = new_x


# keyboard binding up, down, left, right
win.listen()
win.onkeypress(surfer_up, "Up")
win.onkeypress(surfer_down, "Down")
win.onkeypress(surfer_left, "Left")
win.onkeypress(surfer_right, "Right")

# loops the bring a new result
while True:
    win.update()

    #move sharks

    # border checking
    if surfer.ycor() > 300:
        surfer.sety(300)

    if surfer.ycor() < -300:
        surfer.sety(-300)

    if surfer.xcor() > 380:
        surfer.setx(380)

    if surfer.xcor() < -380:
        surfer.setx(-380)

# randomizes which shark goes down from 1-4
    currentShark = random.randint(1, 4)

# brings shark 1
    if currentShark == 1:
        shark1.sety(shark1.ycor() - shark1.dy)
        if shark1.ycor() < -450:
            shark1Start
            shark1Start = random.randint(-(win.window_width() / 2), win.window_width() / 2)
            shark1.goto(shark1Start, ((win.window_height() / 2) + 250))
            shark1.dy += .1
# brings shark 2
    if currentShark == 2:
        shark2.sety(shark2.ycor() - shark2.dy)
        if shark2.ycor() < -450:
            shark2Start
            shark2Start = random.randint(-(win.window_width() / 2), win.window_width() / 2)
            shark2.goto(shark2Start, ((win.window_height() / 2) + 250))
            shark2.dy += .1
# brings shark 3
    if currentShark == 3:
        shark3.sety(shark1.ycor() - shark3.dy)
        if shark3.ycor() < -450:
            shark3Start
            shark3Start = random.randint(-(win.window_width() / 2), win.window_width() / 2)
            shark3.goto(shark1Start, ((win.window_height() / 2) + 250))
            shark3.dy += .1
# brings shark 4
    if currentShark == 4:
        shark4.sety(shark4.ycor() - shark4.dy)
        if shark4.ycor() < -450:
            shark4Start
            shark4Start = random.randint(-(win.window_width() / 2), win.window_width() / 2)
            shark4.goto(shark4Start, ((win.window_height() / 2) + 250))
            shark4.dy += .1

# if any of the sharks hit the surfer, gameOver returns True ending the game
    #Game Over
    if (shark1.ycor() <= surfer.ycor() + 60) and (shark1.xcor() < surfer.xcor() + 20) and (shark1.xcor() > surfer.xcor() - 20)\
            and (shark1.ycor() >= surfer.ycor()):
        gameOver = True

    if (shark2.ycor() <= surfer.ycor() + 60) and (shark2.xcor() < surfer.xcor() + 20) and (shark2.xcor() > surfer.xcor() - 20)\
            and (shark2.ycor() >= surfer.ycor()):
        gameOver = True

    if (shark3.ycor() <= surfer.ycor() + 10 + (shark3Width*10)) and (shark3.xcor() < surfer.xcor() + 20) and (shark3.xcor() > surfer.xcor() - 20)\
            and (shark3.ycor() >= surfer.ycor()):
        gameOver = True

    if (shark4.ycor() <= surfer.ycor() + 60) and (shark4.xcor() < surfer.xcor() + (10*shark4Length)) and (shark4.xcor() > surfer.xcor() - (10*shark4Length))\
            and (shark4.ycor() >= surfer.ycor()):
        gameOver = True

# stops the sharks from continuing when gameOver, ending title is displayed
    if gameOver:
        shark1.dy = 0
        shark2.dy = 0
        shark3.dy = 0
        shark4.dy = 0
        surfer.hideturtle()
        pen.goto(0, 25)
        pen.write("Game Over", align="center", font=("Courier", 35, "normal"))
        pen.goto(0, -25)
        pen.write("Leave window to exit.", align="center", font=("Courier", 24, "normal"))
        resetGame = True
        gameOverArray = [gameOver]

        #Uncomment when you have the function to SET gameOver FALSE
        win.onkeypress(leave_loop(gameOverArray), "enter")
        gameOver = gameOverArray[0]
        #Also make a function to set the loop to false, if possible. Maybe assign the loop bool to a value we change here
        #win.onkeypress(SETloopFALSE, "escape")

# to start the game again
    else:
        if resetGame:
            pen.clear()
            surfer.showturtle()
            surfer.goto(0,0)
            shark1.dy = .2
            shark2.dy = .3
            shark3.dy = .4
            shark4.dy = .1
            shark1Start = random.randint(-(win.window_width()/2),win.window_width()/2)
            shark2Start = random.randint(-(win.window_width()/2),win.window_width()/2)
            shark3Start = random.randint(-(win.window_width()/2),win.window_width()/2)
            shark4Start = random.randint(-(win.window_width()/2),win.window_width()/2)
            shark1.goto(shark1Start, (win.window_height()/2+250))
            shark2.goto(shark2Start, (win.window_height()/2+250))
            shark3.goto(shark3Start, (win.window_height()/2+250))
            shark4.goto(shark4Start, (win.window_height()/2+250))
            resetGame = False


