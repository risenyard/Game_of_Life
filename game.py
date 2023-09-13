import sys

def load_grid_from_file(input_file):
    # Read the grid dimensions
    width, height = map(int, input_file.readline().split())
    # Initialize an empty grid
    grid = []
    # Read positions of living cells and update the grid
    for line in input_file:
        row= line.split()
        row = list(map(int, row))
        grid.append(row)

    return grid, width, height

def save_grid_to_file(output_file, grid):
    for row in grid:
        for cell in row:
            output_file.write('1' if cell else '0')
        output_file.write('\n')

def count_live_neighbors(grid, x, y, width, height):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx]==1:
            count += 1

    return count

def update_grid(grid, width, height):
    new_grid = [[0] * width for _ in range(height)]

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

def run_game(input_name, output_name, generations):
    with open(input_name, 'r') as input_file:
        grid, width, height = load_grid_from_file(input_file)

    for _ in range(generations):
        grid = update_grid(grid, width, height)

    with open(output_name, 'w') as output_file:
        save_grid_to_file(output_file, grid)

## main function
def main():
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

    # input_name = "input.txt"
    # output_name = "output.txt"
    # generations = 5
    run_game(input_name, output_name, generations)
    print("Finish")

if __name__ == "__main__":
        main()