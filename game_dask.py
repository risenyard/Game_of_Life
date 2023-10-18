import numpy as np
import time
import sys
import dask.array as da
from dask.distributed import Client

# Read the grid in the text file
def load_grid_from_file(input_file):
    with open(input_file) as f:
        width, height = map(int, f.readline().split())
        # Make a grid with size of height and width
        grid = []
        for r in range(height):
            grid.append([0] * width)
        # Read the index into the grid
        for line in f: 
            value= line.split() 
            if len(value) >= 2:
                y, x = map(int, value[:2])
                grid[y][x] = 1
            else:
                print("Line doesn't contain two values, check for floating lines at the bottom of file")
        grid = np.array(grid)
    return grid

# save the grid to the text file
def save_grid_to_file(output_file, grid):
    with open(output_file, "w") as f:
        height = len(grid)
        width = len(grid[0])
        f.write(f"{width} {height}\n")
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    f.write(f"{y} {x}\n")

# to calculate the alive neighbors
def count_live_neighbors(grid, x, y, width, height):
    # the neighbor matrix
    neighbors = np.array([
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ])
    # initialize the count
    count = 0
    # loop all possible neighbors
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        # if its neighbor doesn't go beyond the boundary and is alive 
        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx]==1:
            count += 1

    return count

# update the gird
def update_grid(grid):
    # Get height and width
    height = len(grid)
    width = len(grid[0])
    new_grid = np.array([[0] * width for _ in range(height)])

    #apply the rule
    for y in range(height):
        for x in range(width):
            live_neighbors = count_live_neighbors(grid, x, y, width, height)

            if grid[y][x] == 1:
                # Live cell
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[y][x] = 1
            else:
                # Dead cell
                if live_neighbors == 3:
                    new_grid[y][x] = 1

    return new_grid


# run the game
def run_game(input_name, output_name, generations, chunksize):
    grid = load_grid_from_file(input_name)
    # start = time.time()
    # Dask compute
    client = Client()
    grid_da = da.from_array(grid, chunks=(chunksize[0], chunksize[1]))
    for _ in range(generations):   
        grid_da = grid_da.map_overlap(update_grid, depth=1, boundary="none")
        # print("{} seconds elapsed for {} generations.".format(round(time.time() - start, 5), _))
    # Dask compute
    grid = grid_da.compute(scheduler='distributed')
    client.shutdown()
    save_grid_to_file(output_name, grid)
    return grid



## main function
def main():
    # read the input, output and generation from system arguments
    try:
        input_name = sys.argv[1]
    except IndexError:
        sys.exit("No input filename.")

    try:
        output_name = sys.argv[2]
    except IndexError:
        sys.exit("No output filename.")

    try:
        generations = int(sys.argv[3])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")
    
    try:
        a = int(sys.argv[4])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")
    
    try:
        b = int(sys.argv[5])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")
    

    chunksize=[a,b]
    run_game(input_name, output_name, generations, chunksize)
    print("Finish")

if __name__ == "__main__":
        main()

