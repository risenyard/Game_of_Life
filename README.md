# Game of the Life
This is an implementation of Conway's Game if Life
(with and without DASK implementation)

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
* It will spply the rules for the number of generations (For DASK version, the grids will be spllit into DASK array and be applied the rules).
* It will store the final gird to the output file.

## File format
* Grid will be read form the text file
* The first line includes the width and height of the grid as unsigned integer values separated by a space.
* The other lines will indicate the position of the living cells. Each line will have the vertical (first) and horizental (sencond) position of the living cells.
    1. The position id based on zero-indexing, i.e. top left cell is 0 0
    2. Vertical index increases from top to bottom. The valid vertical coordinate values range between 0 - (height-1)
    3. Horizontal index increases from left to right. The valid horizontal coordinate values range between 0 - (width-1)

## Example (without DASK, Python version) 
The first parameter is the path of input file. The second parameter is the path of output file. The third parameter is the number of generation.
```
python game_no_dask.py test_data/input.txt test_data/output.txt 10
```
Input:
```
5 5
0 1
0 2
1 4
2 2
3 1
3 4
4 1
4 2
```
[input.txt](test_data/input.txt)

Output:
```
5 5
0 3
1 2
1 4
2 1
2 4
3 0
3 4
4 1
4 2
4 3
4 4
```
[output.txt](test_data/output.txt)

## Example (with DASK, Python version) 
The first parameter is the path of input file. The second parameter is the path of output file. The third parameter is the number of generation. The fourth parameter is the height of DASK chunk. The last parameter is the width of DASK chunk.
```
python game_dask.py test_data/input.txt test_data/output.txt 10 2 2
```
Input:
```
5 5
0 1
0 2
1 4
2 2
3 1
3 4
4 1
4 2
```
[input.txt](test_data/input.txt)

Output:
```
5 5
0 3
1 2
1 4
2 1
2 4
3 0
3 4
4 1
4 2
4 3
4 4
```
[output.txt](test_data/output.txt)