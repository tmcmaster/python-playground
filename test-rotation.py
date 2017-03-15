#!/usr/bin/python

from copy import copy, deepcopy

#
# The maze map
#
matrix = [
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 0, 0, 1, 0, 0, 0, 0, 1, 1 ],
            [ 1, 1, 0, 1, 0, 1, 1, 0, 1, 1 ],
            [ 1, 1, 0, 0, 0, 0, 1, 0, 1, 1 ],
            [ 1, 1, 1, 1, 0, 1, 1, 0, 0, 1 ],
            [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 1 ],
            [ 1, 0, 1, 0, 0, 1, 1, 1, 0, 1 ],
            [ 1, 0, 0, 0, 1, 1, 0, 0, 0, 1 ],
            [ 1, 1, 1, 0, 0, 0, 0, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
         ]

#
# Person start position
#
xPos = 2
yPos = 2

#
# Maze size
#

w = 10
h = 10;


def printMaze(matrix, xPos, yPos):
    print('---- (' + str(xPos) + ',' + str(yPos) + ')\n')
    for row in matrix:
        print(row);

#
# Rotate a matrix to the left
#
def rotateMatrixLeft(matrix):
    return list(reversed(zip(*matrix)))

#
# Rotate a matrix to the right
#
def rotateMatrixRight(matrix):
    return list(zip(*reversed(matrix)))

#
# Rotate a position to the left
#
def rotatePositionLeft(x,y,w,h):
    return y, w-x-1

#
# Rotate a position to the right
#
def rotatePositionRight(x,y,w,h):
    return h-y-1, x

printMaze(matrix, xPos, yPos)
print('\n')
xPos,yPos = rotatePositionRight(xPos,yPos,10,10)
matrix = rotateMatrixRight(matrix)
printMaze(matrix, xPos, yPos)
