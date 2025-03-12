import heapq

def manhattan_distance(x1, y1, x2, y2):
  """Calculates the Manhattan distance between two points."""
  return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(grid, start, treasure):
  """Performs Best-First Search to find the treasure."""
  rows, cols = len(grid), len(grid[0])


  priority_queue = []
  heapq.heappush(priority_queue, (0, start))

  visited = set()

  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  while priority_queue:
    _, (current_x, current_y) = heapq.heappop(priority_queue)

    if (current_x, current_y) == treasure:
      return f"Treasure found at {treasure}"

    if (current_x, current_y) in visited:
      continue

    visited.add((current_x, current_y))


    for dx, dy in directions:
      neighbour_x, neighbour_y = current_x + dx, current_y + dy


      if 0 <= neighbour_x < rows and 0 <= neighbour_y < cols and (neighbour_x, neighbour_y) not in visited:
        heuristic = manhattan_distance(neighbour_x, neighbour_y, treasure[0], treasure[1])
        heapq.heappush(priority_queue, (heuristic, (neighbour_x, neighbour_y)))

  return "Treasure not found"


grid = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 0]
]

start = (0, 0)
treasure = (3, 3)

result = best_first_search(grid, start, treasure)
print(result)