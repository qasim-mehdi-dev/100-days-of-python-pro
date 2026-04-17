Reeborg's World: Maze Challenge

Project Overview
The Maze Challenge is the final boss of the Reeborg's World "Hurdles" series. Unlike
previous levels where the hurdles were predictable or had a fixed floor, the Maze
requires a truly dynamic algorithm that can navigate an enclosed space to find the
exit (the flag).

The Logic: Following the Right Wall
To solve any simple maze, a classic algorithmic approach is the "Right-Hand Rule." If
you keep your right hand on a wall and never let go, you will eventually find the exit.

Key Logic Constraints:
Right is Clear: This is the priority. If you can turn right, you must! This
prevents the robot from just going in a straight line forever.
Front is Clear: If you can't turn right, but you can move forward, do it.
Dead End: If you can't go right or forward, you must turn left to find a new
path.

Core Implementation

def turn_right():
turn_left()
turn_left()
turn_left()
while not at_goal():
if right_is_clear():
turn_right()
•

•
•

move()
elif front_is_clear():
move()
else:
turn_left()

Edge Cases & Refinement
In some specific starting positions, a simple "turn right" loop can cause the robot to
move in a circle. To prevent this, you can add an initial check to find a wall before
starting the main logic loop.
Refined Loop:

# Finding the first wall to avoid infinite loops in open space
while front_is_clear():
move()
turn_left()
# Main Navigation Loop
while not at_goal():
if right_is_clear():
turn_right()
move()
elif front_is_clear():
move()
else:
turn_left()

Key Concepts Learned
Control Flow: Using if/elif/else within a while loop.
Boolean Logic: Negating conditions with the not operator.
Dry Coding: Defining helper functions