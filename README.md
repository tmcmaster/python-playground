# python-playground
 place to play with python

## Install the curses library

```bash
brew install homebrew/dupes/ncurses
```

## Run the maze demo

The following is a demo, where a little guy walks around a maze, which is rendered as 3D ascii art.

```bash
./maze.py
```

This maze is generated from a 2 dimensional array of numbers, where '1' represent walls, and the '0' represent passages.

```python
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
```
