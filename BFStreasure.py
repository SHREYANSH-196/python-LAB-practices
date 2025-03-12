def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def best_first_search(grid, start, goal):
    from queue import PriorityQueue
   
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()

    while not queue.empty():
        _, current = queue.get()
        
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return f"Treasure found at {current}!"

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and neighbor not in visited:
                queue.put((manhattan_distance(neighbor, goal), neighbor))

    return "Treasure not found!"

if __name__ == "__main__":
    grid = [[0] * 5 for _ in range(5)]
    start = (0, 0)
    goal = (2, 2)

    print(best_first_search(grid, start, goal))