# MazeMaker (WIP)
Maze data generator

Simple to use maze data factory function

import MazeMaker

my_maze = MazeMaker.factory.create_maze(1, 50, 4, 20, (5, 40))


The resulting maze will have one main path (containing entrance/exit portals), 
50 dead branches with a length between 5 and 40 rooms, and each branch having 
at most 20 branches extending from each other and each room having a maximun 
of 4 adjasent rooms.
