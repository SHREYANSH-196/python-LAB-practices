import heapq

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def misplaced_tiles(state, goal):
    return sum(1 for i in range(len(state)) for j in range(len(state[i])) if state[i][j] != 0 and state[i][j] != goal[i][j])

def manhattan_distance_sum(state, goal):
    positions = {value: (i, j) for i, row in enumerate(goal) for j, value in enumerate(row)}
    total_distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                goal_pos = positions[state[i][j]]
                total_distance += manhattan_distance((i, j), goal_pos)
    return total_distance

def find_blank_tile(state):
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def a_star_8_puzzle(start, goal, heuristic):
    rows, cols = len(start), len(start[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, start, []))
    visited = set()
    nodes_explored = 0
    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)
        nodes_explored += 1
        if current == goal:
            return path, nodes_explored, g
        visited.add(tuple(tuple(row) for row in current))
        blank_i, blank_j = find_blank_tile(current)
        for di, dj in moves:
            ni, nj = blank_i + di, blank_j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                neighbor = [list(row) for row in current]
                neighbor[blank_i][blank_j], neighbor[ni][nj] = neighbor[ni][nj], neighbor[blank_i][blank_j]
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited:
                    h = heuristic(neighbor, goal)
                    f = g + 1 + h
                    heapq.heappush(priority_queue, (f, g + 1, neighbor, path + [(ni, nj)]))
    return None, nodes_explored, -1

initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

path_h1, explored_h1, depth_h1 = a_star_8_puzzle(initial_state, goal_state, misplaced_tiles)
print("H1 (Misplaced Tiles):")
print(f"Path: {path_h1}, Nodes Explored: {explored_h1}, Solution Depth: {depth_h1}")

path_h2, explored_h2, depth_h2 = a_star_8_puzzle(initial_state, goal_state, manhattan_distance_sum)
print("\nH2 (Manhattan Distance):")
print(f"Path: {path_h2}, Nodes Explored: {explored_h2}, Solution Depth: {depth_h2}")