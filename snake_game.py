import turtle
import time
import random

delay = 100
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Tutorial")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"
wn.update()

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
wn.update()

segments = []

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 24, "normal"))

#Function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keybinds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Game
def game():
    global score, high_score, delay
    wn.update()

    # Food Moves
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase Speed After Eating
        delay = int(100 * (0.97 ** len(segments)))
        delay = max (40, delay)
        
        # Increase Score
        score += 10
        
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))    

    # Keep segments attached
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move Segment to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Teleport Segments Off Screen
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear Segments
        segments.clear()

        # Reset Delay
        delay = 100

        # Reset Score
        score = 0
        pen.clear()
        pen.write("score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal")) 

    # Collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Teleport Segments Off Screen
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear Segments
            segments.clear()

            # Reset Delay
            delay = 100
        
            # Reset Score
            score = 0
            pen.clear()
            pen.write("score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal")) 
    wn.ontimer(game, delay)

game()  
wn.mainloop()