def ways(maze, x, y, n):
    if x == n - 1 and y == n - 1:
        return 1
    if x >= n or y >= n or maze[x][y] == 0:
        return 0
    return ways(maze, x + 1, y, n) + ways(maze, x, y + 1, n)
maze = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]
n = len(maze)
print("Ways the rat can escape:", ways(maze, 0, 0, n))