
import numpy as np

def flood_fill(grid, x, y, color):
    rows, cols = grid.shape
    if grid[x][y] != 0:
        return

    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if grid[cx][cy] == 0:
            grid[cx][cy] = color
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    stack.append((nx, ny))

def process_grid(grid, start_x, start_y):
    color = 2
    flood_fill(grid, start_x, start_y, color)
    color += 1

    while True:
        found = False
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] == 0:
                    flood_fill(grid, i, j, color)
                    color += 1
                    found = True
        if not found:
            break
    return grid

def main():
    grid = np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ])

    start_x, start_y = 0, 0

    print("Grid inicial:")
    print(grid)

    result = process_grid(grid.copy(), start_x, start_y)

    print("\nGrid preenchido:")
    print(result)

if __name__ == "__main__":
    main()
