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
# (J.F.) Tiles variable describes the map on which the game is played. The 1's represent the places where pacman can move and pellets are present. The zero are the walls where pacman cannot pass.
# (J.F.) There can also be 2's on the map. These would represents spots where pacman can move but there is no pellets. Later in the code, we see that when pacman eats a pellet, the ones become twos.
# (J.F.) This variable is defined as an array, with each row being one line blocks on the actual map.
# fmt: on

# (A.R.) A list representing the layout of the game world. It uses a flattened representation of a 20x20 grid, where 0 represents a wall, 1 represents a dot, and 2 represents an empty space.

def square(x, y): # (A.R.) Draws a square at the specified coordinates using the path turtle
    
    """Draw square using path at (x, y)."""
    path.up()  #(J.F.) Allows to move to a new position to redraw the a specific square in the new position.
    path.goto(x, y) # (J.F) Moves to specified x, y coordinates to redraw that square.
    path.down() # (J.F) Goes back down, which allows to draw the new square. (Cancels the path.up which is for moving)
    path.begin_fill() # (J.F) Begin filling the shape with the current color.


    for count in range(4): # (J.F) This function repeats 4 times because it needs to draw all four sides of each square
        path.forward(20) # (J.F) Moves fowrard by 20 units, the length of a square
        path.left(90) # (J.F) Moves left by 90 degrees, to change sides.

    path.end_fill() # (J.F.) Ends the filling of the shape, completing the square.


def offset(point): # (A.R.) Calculates the offset of a point in the tiles list.
    """Return offset of point in tiles.""" 
    x = (floor(point.x, 20) + 200) / 20 # (A.R.) Rounds down the x-coordinate of the point to the nearest multiple of 20.
    y = (180 - floor(point.y, 20)) / 20 # (A.R.) Rounds down the y-coordinate of the point to the nearest multiple of 20.
    index = int(x + y * 20) # (A.R.) Combines the x and y offsets to calculate the index within a width of 20 tiles.
    return index # (A.R.) Return the index calculated above


def valid(point): # (A.R.) Checks if a given point is valid in the game world (as not a wall).
    """Return True if point is valid in tiles."""
    index = offset(point) # (B.P.) Calculates the index of the given point using the offset function above.

    if tiles[index] == 0: # (B.P.) Checks if the tile at the calculated index is 0 (indicating a wall, as shown on the map). 
        return False # (B.P.) If the point is considered invalid (if the statement above is true), the statement returns False.

    index = offset(point + 19) # (B.P.) Calculates the index of the point shifted by 19 units (to check a point near the bottom-right corner of a 20x20 tile) using the offset function above.

    if tiles[index] == 0: # (B.P.) Checks if the seconf tile at the calculated index is 0 (indicating a wall, as shown on the map). 
        return False # (B.P.)# (B.P.) If the point is considered invalid (if the statement above is true), the statement returns False.

    return point.x % 20 == 0 or point.y % 20 == 0 # (B.P) Checks if the point is on the grid lines (either the x or y coordinate is a multiple of 20). If true, the point is considered valid.


def world(): #(A.R.) Draws the entire game world using the path turtle. It uses the square function and sets the background color to black and the path color to blue.
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')


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


def move():  # (J.F.) This function helps with the movement of pacman, the ghosts, the score and removes the pellets once pacman has passed over them.)
    """Move pacman and all ghosts."""
# (A.R.) Handles the movement of Pacman and ghosts. It updates the positions, checks for collisions, and continues the game loop
    writer.undo()  # (J.F.) This undoes the previous score after pacman moves.
    writer.write(state['score']) #(J.F.) This writes the new score after pacman moves (which is increased by one if he captured a pellet.
    

    clear() #(J.F.) Clear removes the previous positions of Pacman, ghosts, and other elements on the screen before updating their positions in the next frame.

    if valid(pacman + aim):  #(J.F.) This is checking if the new position of Pacman, obtained by adding the aim vector to the current position (pacman + aim), is valid, meaning that Pacman can move there (there is no wall). Uses the valid function above.
        pacman.move(aim) #(J.F.) If the new pacman position is valid, pacman moves to that new position.

    index = offset(pacman) #(J.F.) The index variable is assigned to the value returned by the offset function, which calculates the index of Pacman's position.

    # (J.F.) Overall, the if statement above checks if pacman can move to the new desired position, and if so, pacman moves to that position. Then, it checks the index of the new position.
    
    if tiles[index] == 1: #(J.F.) This if statement checks if the spot pacman wants to move towards contains a pellet. It says one because 1 represents the spots with pellets on the map.
        tiles[index] = 2 #(J.F.) If the spot where pacman moves is a pellet (1), it becomes a spot where pacman can move but there is no pellet (2).
        state['score'] += 1 #(J.F.) Because pacman has eaten a pellet (because the if statement is true) the score is increased by one.
        x = (index % 20) * 20 - 200 #(J.F.) This calculates the x coordinate of pacman's position.
        y = 180 - (index // 20) * 20 #(J.F.) This calculates the y coordinate of pacman's position.
        square(x, y) #(J.F.) Uses the square function above to redraw and add the correct changes for the square pacman has passed.

    up() #(J.F.) Allows to move to a new position to redraw pacman in the new position.
    goto(pacman.x + 10, pacman.y + 10) #(J.F.) Indicates the new coordinates where pacman needs to be drawn.
    dot(20, 'yellow') #(J.F.) This draws pacman in the new position. 20 is the radius and yellow is the color.

    for point, course in ghosts: #(J.F.) This for loop goes for each ghost, where point is the current position of the ghost, and course is the vector representing its current movement direction.
        if valid(point + course): #(J.F.) This checks if the new position for the ghost is valid using the valid function from above. Similarly to for pacman above.
            point.move(course) #(J.F.) If the new position for the ghost is valid, he moves to that new position.
            #(J.F.) The if statement above means that if there is nothing blocking a ghost, he will always continue to move forward and will never unnecessarily turn.
        else:
            options = [ #(J.F.) If the ghost cannot continue on its path, a direction is chosen from the ones below for 
                vector(5, 0), #(J.F.) The ghost could move towards the right.
                vector(-5, 0), #(J.F.) The ghost could move towards the left.
                vector(0, 5), #(J.F.) The ghost could move towards the top.
                vector(0, -5), #(J.F.) The ghost could move towards the bottom.
            ]
            plan = choice(options) #(J.F.) The choice function from the random module is used to randomly select one vector from the options list. This selected vector is assigned to the variable plan.
            course.x = plan.x #(J.F.) The x coordinate of the randomly chosen option is added to the ghosts plan.
            course.y = plan.y #(J.F.) The y coordinate of the randomly chosen option is added to the ghosts plan.

        up() #(J.F.) Allows to move to a new position to redraw the ghosts in the new position.
        goto(point.x + 10, point.y + 10) #(J.F.)Indicates the new coordinates where the ghosts needs to be drawn.
        dot(20, 'red') #(J.F.) This draws the ghosts in the new positions. 20 is the radius and red is the color.

    update() #(J.F.) The update() function is called to update the screen with the new positions and drawings.

    for point, course in ghosts: #(J.F.) This for loop goes for each ghost, where point is the current position of the ghost, and course is the vector representing its current movement direction.
        if abs(pacman - point) < 20: #(J.F.) The condition checks whether the absolute distance between Pacman (pacman) and the current ghost (point) is less than 20 units. If this is true, it means Pacman is close enough to the ghost to be eaten.
            return #(J.F.) If a collision is detected, the return statement is used to exit the move function, effectively stopping the movement of Pacman and ghosts.

    ontimer(move, 100) #(J.F.) After checking for collisions, the ontimer function schedules the next call to the move function after a delay of 100 milliseconds. This creates a continuous loop for updating the game state.


def change(x, y):
    # (N.J.) Change pacman aim if valid.
    # (N.J.) The function 'change' modifies the direction of Pacman's movement based on the changes in the x and y coordinates (x, y) given as parameters. It checks if the new position obtained by adding the vector (x, y) to the current Pacman position is valid using the 'valid' function.
    if valid(pacman + vector(x, y)):
        # (N.J.) If the new position is valid, update the 'aim' vector with the new x and y values.
        aim.x = x # (J.F) The new x position for the aim vector is defined.
        aim.y = y # (J.F) The new y position for the aim vector is defined.


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
