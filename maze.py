#!/usr/bin/python

import curses

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
# Define the person sprites.
#

person1 = ["    (#)    ",
           "   .nHn.   ",
           "   HHHHH.  ",
           "   `HH(*N  ",
           "    HHH  * ",
           "    NNN    ",
           "    N/*    ",
           "    N H    ",
           "    N      ",
           "    q,     "]

person2 = ["    (#)    ",
           "   .nHn.   ",
           "  .HHHHH   ",
           "  N*)\HH'   ",
           " *  HHH    ",
           "    NNN    ",
           "    *\N    ",
           "    H N    ",
           "      N    ",
           "     ,q    "]

person = [person1,person2]
  
  
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
    return y, w-x+1

#
# Rotate a position to the right
# 
def rotatePositionRight(x,y,w,h):
    return h-y+1, x

#
#  Print a row of blocks
#
def printRow(top,left,height,width,sizes,statesLeft,statesRight,position):
    front = -1
    if position == 0:
        beforeLeft = 0
        beforeRight = 0
    else:
        beforeLeft = statesLeft[position-1];
        beforeRight = statesRight[position-1];
        
    
    size = 10#sizes[0]-1;
    
    x=0;
    right=left+width
    
    j=0;
    maxpos = position+5;
    if maxpos > len(statesLeft):
        maxpos = len(statesLeft)
        
    for i in range(position, maxpos):
        front=size-1;    
        size=sizes[j]
        j+=1;
        if ((i+1) >= maxpos):
            afterLeft = 0;
            afterRight = 0;
        else:
            afterLeft = statesLeft[i+1]
            afterRight = statesRight[i+1]
            
        #stdscr.addstr(3+j,20, "j(%d) Before(%d), After(%d)" % (j,beforeLeft, afterLeft))

        if statesLeft[i] == 1:
            printBlock(top, left+x, height, size, beforeLeft, afterLeft, front,1)
        if statesRight[i] == 1:
            printBlock(top, right-x, height, size, beforeRight, afterRight, front,-1)
            
        if i < maxpos-1:
            beforeLeft = statesLeft[i]
            beforeRight = statesRight[i]
            top = top + size
            x = x + size
            height = height - 2*size;
        #else:
            #if maxpos == len(statesLeft)-1:
            #stdscr.addstr(top-size, x+size*2, "******")
    
    # draw the person
    for i,line in enumerate(person[position%2]):
        stdscr.addstr(25+i,10+width/2,line);
        
    stdscr.move(1,1)


#
#  Print a block on the given side of the screen
#
def printBlock(top,x,height,width,before,after,front,mirror):
    h1 = height
    h2 = h1 - width*2+2
    
    blockFront = "_"
    blockSide = "]" if mirror == 1 else "["
    blockTop = "\\" if mirror == 1 else "/"
    blockBottom = "/" if mirror == 1 else "\\"
    # blockSide, blockTop, BlockBottom = map['left']
    
    # there is a space in front of the block
    if before == 0:
        # print the front lines
        for i in range(front):
            stdscr.addstr(top-2, x-i*mirror, blockFront)
            stdscr.addstr(top+h1-2, x-i*mirror, blockFront)
        # print the side line at the front
        for i in range(h1):
            stdscr.addstr(top+i-1, x, blockSide)

    # block top
    for i in range(width-1):
        stdscr.addstr(top+i-1, x+(i+1)*mirror, blockTop)

    if after == 0:
        # far side
        for i in range(h2):
            stdscr.addstr(top+width-2+i, x+width*mirror, blockSide)
    else:
        # far side bottom and top
        stdscr.addstr(top+width-2, x+width*mirror, blockTop)
        stdscr.addstr(top+h1-width-1, x+width*mirror, blockBottom)
        
    # block bottom
    for i in range(width-1):
        stdscr.addstr(top+h1-2-i, x+(i+1)*mirror, blockBottom)
        

#
# initalise curses
#
stdscr = curses.initscr()
curses.noecho() 
curses.curs_set(0) 
stdscr.keypad(1)
stdscr.refresh()

#
#  Size of blocks, decreasing as the block gets further away
#
sizes = [5,4,3,3,2]

#
#  Maze location and size on the screen
#

x = 15
y = 5
width = 60
height = 35

#
# Person start position
#
xPos = 2
yPos = 2

#
#  list of block states
#
statesLeft = matrix[yPos-1];
statesRight = matrix[yPos+1];

#
#  Initialise the maze on the screen
#
printRow(y,x,height, width, sizes, statesLeft,statesRight, xPos) 
stdscr.move(1,1)

while True:
    #stdscr.addstr(2,2, "xPos(%d), yPos(%d), width(%d), height(%d)" % (xPos,yPos,len(matrix),len(matrix)))
    c = stdscr.getch()
    if c == curses.KEY_UP:
        if xPos < len(statesLeft)-1:
            xPos+=1
            stdscr.clear();
            printRow(y,x,height, width, sizes, statesLeft,statesRight, xPos) 
    if c == curses.KEY_DOWN:
        if xPos > 0:
            xPos-=1
            stdscr.clear();
            printRow(y,x,height, width, sizes, statesLeft,statesRight, xPos) 
    if c == curses.KEY_LEFT:
        matrix = rotateMatrixLeft(matrix)
        xPos,yPos = rotatePositionLeft(xPos,yPos,10,10)
        #stdscr.addstr(2,2, "xPos(%d), yPos(%d), l(%d), width(%d), height(%d)" % (xPos,yPos,l,len(matrix),len(matrix)))
        #stdscr.refresh()
        statesLeft = matrix[yPos-1]
        statesRight = matrix[yPos+1];
        stdscr.clear();
        printRow(y,x,height, width, sizes, statesLeft,statesRight, xPos) 
    if c == curses.KEY_RIGHT:
        matrix = rotateMatrixRight(matrix)
        xPos,yPos = rotatePositionRight(xPos,yPos,10,10)
        #stdscr.addstr(2,2, "xPos(%d), yPos(%d), width(%d), height(%d)" % (xPos,yPos,len(matrix),len(matrix)))
        statesLeft = matrix[yPos-1]
        statesRight = matrix[yPos+1];
        stdscr.clear();
        printRow(y,x,height, width, sizes, statesLeft,statesRight, xPos) 
    else:
        if c == 113: # 'q'
            curses.echo()
            curses.endwin()
            exit()
