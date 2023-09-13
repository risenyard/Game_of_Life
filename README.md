# Game of the Life
This is an implementation of Conway's Game if Life

## Description
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead.

Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any **live** cell with fewer than two live neighbours dies, as if by underpopulation.
* Any **live** cell with two or three live neighbours lives on to the next generation.
* Any **live** cell with more than three live neighbours dies, as if by overpopulation.
* Any **dead** cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Implementations
* Our script will get the input file name, output file name, and the number of generations as arguments.
* It will load the initial pattern of the grid from the input file.
* It will spply the rules for the number of generations.
* It will store the final gird to the output file.

## File format
* Grid will be read form the text file
* The lines will indicate the position of the living cells. Each line will have the horizontal and vertical position of the living cells.
    1. The position id based on zero-indexing, i.e. top left cell is 0 0
    2. Horizontal index increases from left to right.
    3. Vertical index increases from top to bottom.
* The digit 1 meand the cell is alive; 0 means the cell is dead.

## Example
```
python game.py test_data/input.txt test_data/output.txt 2
```