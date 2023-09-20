import sys
import time
import random

# Generate random grid
def generate_random_grid(width, height, alive):

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive")
    
    grid = []
    if width > 0 and height > 0:   
        for y in range(height):
            grid.append([0] * width)

    if alive < 0 or alive > 1.0:
        raise ValueError("Invalid alive percentage.")
    
    m = round(width * height * alive)
    skip = {}

    while m > 0:
        x, y = random.randrange(width), random.randrange(height)
        idx = y * width + x
        if idx not in skip:
            grid[y][x] = 1
            skip[idx] = True
            m -= 1

    return grid

# save the grid to the text file
def save_grid_to_file(output_file, grid):
    for row in grid:
        for cell in row:
            output_file.write(str(cell)+" ")
        output_file.write('\n')

# to calculate the alive neighbors
def count_live_neighbors(grid, x, y, width, height):
    # the neighbor matrix
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    # initialize the count
    count = 0
    # loop all possible neighbors
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        # if its neighbor doesn't go beyond the boundary and is alive 
        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx]==1:
            count += 1

    return count

@profile
# update the gird
def update_grid(grid, width, height):
    new_grid = [[0] * width for _ in range(height)]

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
def run_game(output_name, generations, width, height, alive):
    grid = generate_random_grid(width, height, alive)

    output_grid_path =output_name.split(".")[0]+"_original_grid.txt"
    with open(output_grid_path, 'w') as output_file:
        save_grid_to_file(output_file, grid)

    start = time.time()
    for _ in range(generations):
        grid = update_grid(grid, width, height)
        print("{} seconds run for {} generations.".format(round(time.time() - start, 5), _+1))

    with open(output_name, 'w') as output_file:
        save_grid_to_file(output_file, grid)

## main function
def main():
    # read the inpur, output and generation from system arguments
    try:
        output_name = sys.argv[1]
    except IndexError:
        sys.exit("No input filename.")

    try:
        generations = int(sys.argv[2])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")
    
    try:
        width = int(sys.argv[3])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")
    
    try:
        height = int(sys.argv[4])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")

    try:
        alive = float(sys.argv[5])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")

    run_game(output_name, generations, width, height, alive)
    print("Finish")

if __name__ == "__main__":
        main()