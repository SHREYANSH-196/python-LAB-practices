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
    moves = [(-1,0),(1,0),(0,-1),(0,1)]