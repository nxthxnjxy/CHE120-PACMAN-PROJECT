# Nathan Jayasena (N.J.), Ali Riaz (A.R.), Jacob Finch (J.F), Blake Pedersen (B.P.)


"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

from random import choice
# (A.R.) Imports the choice function from the random module.
from turtle import *
# (A.R.) Imports everything from the turtle module.
from freegames import floor, vector
# (A.R) Imports functions "floor" and "vector" from a custom module named freegames.

# (N.J.) Initialize the game state with a dictionary 'state' containing the current score, starting at 0.
state = {'score': 0}

# (N.J.) Create a Turtle object 'path' to represent the game board visually. This Turtle is set as invisible ('visible=False') as it is solely used for drawing and doesn't need to be displayed during gameplay.

path = Turtle(visible=False)

# (N.J.) Create a Turtle object 'writer' to display relevant information, such as the player's score.
# (N.J.) Similar to 'path', this Turtle is set as invisible ('visible=False') since it's not meant to be seen during gameplay.

writer = Turtle(visible=False)

# (N.J.) Define the initial direction for movement ('aim') with a vector (5, 0), indicating movement to the right at a speed of 5 units per step.

aim = vector(5, 0)

# (N.J.) Set the initial position of the Pacman character to (-40, -80), representing its starting point on the game board.

pacman = vector(-40, -80)

# (N.J.) Initialize the positions and movement directions of four ghosts in the game.
# (N.J.) Each ghost is represented as a list containing a vector for its starting position and another vector for its initial movement direction.
# (N.J.) The direction vector is given by an x and y value represented by (x,y). If x is positive, the direction is right, if x is negative, the direction is left. If y is positive, the direction is up, if y is negative, the direction is down.

ghosts = [
    [vector(-180, 160), vector(5, 0)],    # (N.J.) Ghost 1 starting position and initial movement direction, right.
    [vector(-180, -160), vector(0, 5)],   # (N.J.) Ghost 2 starting position and initial movement direction, up.
    [vector(100, 160), vector(0, -5)],    # (N.J.) Ghost 3 starting position and initial movement direction, down.
    [vector(100, -160), vector(-5, 0)],   # (N.J.) Ghost 4 starting position and initial movement direction, left.
]

# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on
# (A.R.) A list representing the layout of the game world. It uses a flattened representation of a 20x20 grid, where 0 represents a wall, 1 represents a dot, and 2 represents an empty space.

def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
# (A.R.) Draws a square at the specified coordinates using the path turtle

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index
# (A.R.) Calculates the offset of a point in the tiles list.

def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0
# (A.R.) Checks if a given point is valid in the game world (as not a wall).

def world():
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')
#(A.R.) Draws the entire game world using the path turtle. It uses the square function and sets the background color to black.

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    """Move pacman and all ghosts."""
# (A.R.) Handles the movement of Pacman and ghosts. It updates the positions, checks for collisions, and continues the game loop
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


def change(x, y):
    # (N.J.) Change pacman aim if valid.
    # (N.J.) The function 'change' modifies the direction of Pacman's movement based on the changes in the x and y coordinates (x, y) given as parameters. It checks if the new position obtained by adding the vector (x, y) to the current Pacman position is valid using the 'valid' function.
    if valid(pacman + vector(x, y)):
        # (N.J.) If the new position is valid, update the 'aim' vector with the new x and y values.
        aim.x = x
        aim.y = y


# (N.J.) Set up the game window with dimensions 420x420 and an initial window position at (370, 0).
setup(420, 420, 370, 0)

# (N.J.) Hide the default turtle cursor for a cleaner appearance.
hideturtle()

# (N.J.) Turn off animation rendering to improve performance by updating the screen only after the entire frame is drawn.
tracer(False)

# (N.J.) Position the 'writer' Turtle at coordinates (160, 160), set its color to white, and display the initial score.
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])

# (N.J.) Enable the program to respond to keyboard inputs.
listen()

# (N.J.) Set up keyboard bindings to associate arrow key presses with corresponding calls to the 'change' function, modifying Pacman's aim vector based on the desired direction.
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

# (N.J.) Initialize the game environment.
world()

# (N.J.) Initiate the game loop, handling Pacman and ghost movement, collision detection, and score updates.
move()

# (N.J.) Conclude the execution of the program, allowing the user to close the game window.
done()
