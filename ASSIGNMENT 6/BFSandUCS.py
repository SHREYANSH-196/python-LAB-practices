import heapq
import matplotlib.pyplot as plt
import numpy as np
import time

def create_grid(rows, cols, obstacles):
    grid = np.zeros((rows, cols))
    for obs in obstacles:
        grid[obs[0]][obs[1]] = 1
    return grid

def a_star(grid, start, goal, heuristic="manhattan"):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if heuristic == "euclidean":
        directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def calculate_heuristic(current, goal):
        if heuristic == "manhattan":
            return abs(current[0] - goal[0]) + abs(current[1] - goal[1])
        elif heuristic == "euclidean":
            return ((current[0] - goal[0])**2 + (current[1] - goal[1])**2)**0.5

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: calculate_heuristic(start, goal)}

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
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + calculate_heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def bfs(grid, start, goal):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [start]
    came_from = {start: None}

    while queue:
        current = queue.pop(0)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    return None

def uniform_cost_search(grid, start, goal):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (new_cost, neighbor))

    return None

def visualize(grid, path, title):
    plt.imshow(grid, cmap="binary")
    for (x, y) in path:
        plt.plot(y, x, "ro")
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    rows, cols = 10, 10
    obstacles = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3)]
    grid = create_grid(rows, cols, obstacles)
    start, goal = (0, 0), (7, 7)

    for algorithm in ["A*", "BFS", "UCS"]:
        print(f"Running {algorithm}...")
        start_time = time.time()
        
        if algorithm == "A*":
            path = a_star(grid, start, goal, heuristic="manhattan")
        elif algorithm == "BFS":
            path = bfs(grid, start, goal)
        elif algorithm == "UCS":
            path = uniform_cost_search(grid, start, goal)
        
        elapsed_time = time.time() - start_time
        if path:
            visualize(grid, path, f"{algorithm} Path")
            print(f"{algorithm}: Path found with cost {len(path)} in {elapsed_time:.4f} seconds")
        else:
            print(f"{algorithm}: No path found in {elapsed_time:.4f} seconds")
