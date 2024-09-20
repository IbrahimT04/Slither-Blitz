from tkinter import *
import random


class Snake:
    def __init__(self):
        self.body_size = 4
        self.squares = []
        self.coordinates = []

        for i in range(0, 4):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,
                                             y,
                                             x + 10,
                                             y + 10,
                                             fill="#00FF00",
                                             tag="SNAKE")
            self.squares.append(square)


class Food:
    def __init__(self):
        location_X = random.randint(0, 24) * 10
        location_Y = random.randint(0, 24) * 10

        self.coordinates = [location_X, location_Y]

        canvas.create_oval(location_X,
                           location_Y, (location_X + 10), (location_Y + 10),
                           fill="#000000",
                           tag="Food")


def next_turn(my_snake, my_food):
    global score
    global StartSpeed
    x, y = my_snake.coordinates[0]

    if direction == "up":
        y -= 10
    elif direction == "down":
        y += 10
    elif direction == "left":
        x -= 10
    elif direction == "right":
        x += 10

    my_snake.coordinates.insert(0, (x, y))

    square1 = canvas.create_rectangle(x, y, x + 10, y + 10, fill="#00FFFF")

    my_snake.squares.insert(0, square1)

    if x == my_food.coordinates[0] and y == my_food.coordinates[1]:

        StartSpeed -= 1
        StartSpeed *= 0.95

        score += 1

        canvas.delete("Food")

        my_food = Food()

    else:

        del my_snake.coordinates[-1]

        canvas.delete(my_snake.squares[-1])

        del my_snake.squares[-1]

    if check_collisions(my_snake):
        game_over()

    else:
        NewSpeed = int(StartSpeed) + 1
        canvas.after(NewSpeed, next_turn, my_snake, my_food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(my_snake):
    x, y = my_snake.coordinates[0]

    if x < 0 or x >= 250:
        return True
    elif y < 0 or y >= 250:
        return True

    for body_part in my_snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def g_exit():
    screen.destroy()


def restart():
    canvas.delete(ALL)
    btnRestart.destroy()
    btnExit.destroy()
    global btnRestart_Pressed
    btnRestart_Pressed = True
    global HighScore
    global NewScore
    if NewScore >= HighScore:
        NewScore = HighScore
    global score
    score = 0
    global direction
    direction = "down"
    global StartSpeed
    StartSpeed = 125
    global snake
    snake.coordinates.clear()
    snake.squares.clear()
    for i in range(0, 4):
        snake.coordinates.append([0, 0])

    for x, y in snake.coordinates:
        square = canvas.create_rectangle(x,
                                         y,
                                         x + 10,
                                         y + 10,
                                         fill="#00FF00",
                                         tag="SNAKE")
        snake.squares.append(square)

    location_X = random.randint(0, 24) * 10
    location_Y = random.randint(0, 24) * 10

    food.coordinates = [location_X, location_Y]

    canvas.create_oval(location_X,
                       location_Y, (location_X + 10), (location_Y + 10),
                       fill="#000000",
                       tag="Food")

    next_turn(snake, food)
    screen.update()


def game_over():
    global HighScore
    global score
    global btnRestart_Pressed
    global NewScore

    canvas.delete(ALL)

    if btnRestart_Pressed:
        if score >= NewScore:
            NewScore = score

            canvas.create_text(125,
                               125,
                               font=('arial', 20),
                               text="!!!HIGH SCORE!!!",
                               fill="red",
                               tag="Gameover")

            canvas.create_text(125,
                               90,
                               font=('arial', 15),
                               text=NewScore,
                               fill="blue",
                               tag="gameover")

        else:

            canvas.create_text(125,
                               125,
                               font=('arial', 20),
                               text="!!!GAME OVER!!!",
                               fill="red",
                               tag="Gameover")
            canvas.create_text(125,
                               90,
                               font=('arial', 15),
                               text=score,
                               fill="blue",
                               tag="gameover")
    else:
        Highscore = score

        canvas.create_text(125,
                           125,
                           font=('arial', 20),
                           text="!!!HIGH SCORE!!!",
                           fill="red",
                           tag="Gameover")

        canvas.create_text(125,
                           90,
                           font=('arial', 15),
                           text=score,
                           fill="blue",
                           tag="gameover")

    canvas.create_text(125,
                       175,
                       font=('arial', 15),
                       text="Final Score:",
                       fill="blue",
                       tag="gameover")

    canvas.create_text(125,
                       65,
                       font=('arial', 15),
                       text="High Score:",
                       fill="blue",
                       tag="gameover")

    canvas.create_text(125,
                       200,
                       font=('arial', 15),
                       text=score,
                       fill="blue",
                       tag="gameover")

    global btnRestart
    btnRestart = Button(screen, text='Restart')
    btnRestart.config(command=restart)
    btnRestart.pack()

    global btnExit
    btnExit = Button(screen, text='Exit')
    btnExit.config(command=g_exit)
    btnExit.pack()


screen = Tk()

screen.title("!!! SNAKE GAME !!!")
screen.resizable(False, False)

score = 0
StartSpeed = 125.0
direction = "down"
btnRestart_Pressed = False
HighScore = 0
NewScore = 0

canvas = Canvas(screen, bg="#F0F0F0", height=250, width=250)
canvas.pack()

screen.update()

screen.bind('<Left>', lambda event: change_direction('left'))
screen.bind('<Right>', lambda event: change_direction('right'))
screen.bind('<Up>', lambda event: change_direction('up'))
screen.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

screen.mainloop()
