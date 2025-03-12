import heapq
import matplotlib.pyplot as plt
import numpy as np
def create_grid(rows, cols, obstacles):
    grid = np.zeros((rows, cols))
    for obs in obstacles:
        grid[obs[0]][obs[1]] = 1
    return grid

def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def euclidean_distance(current, goal):
    return ((current[0] - goal[0])**2 + (current[1] - goal[1])**2)**0.5

def a_star(grid, start, goal, allow_diagonal=False):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if allow_diagonal:
        directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal) if not allow_diagonal else euclidean_distance(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + (1 if not allow_diagonal else euclidean_distance(current, neighbor))
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + (manhattan_distance(neighbor, goal) if not allow_diagonal else euclidean_distance(neighbor, goal))
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

def visualize(grid, path):
    plt.imshow(grid, cmap="binary")
    for (x, y) in path:
        plt.plot(y, x, "ro")
    plt.show()


if __name__ == "__main__":
    rows, cols = 10, 10
    obstacles = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3)]
    grid = create_grid(rows, cols, obstacles)
    start, goal = (0, 0), (7, 7)

    print("Path using Manhattan distance:")
    path_manhattan = a_star(grid, start, goal, allow_diagonal=False)
    if path_manhattan:
        visualize(grid, path_manhattan)

    print("Path using Euclidean distance:")
    path_euclidean = a_star(grid, start, goal, allow_diagonal=True)
    if path_euclidean:
        visualize(grid, path_euclidean)