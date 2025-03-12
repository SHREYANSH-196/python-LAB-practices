from collections import deque

def bidirectional_bfs(graph, start, target):
    # Error handling for invalid nodes
    if start not in graph or target not in graph:
        return {"error": "Start or target node does not exist in the graph."}

    if start == target:
        return {"path": [start], "nodes_explored": 0, "path_length": 0}

    # Initialize frontiers and queues
    front_start = {start: None}
    front_target = {target: None}
    queue_start = deque([start])
    queue_target = deque([target])

    # Node exploration counter
    nodes_explored = 0

    # Perform Bi-Directional BFS
    while queue_start and queue_target:
        # Expand from the start side
        if expand_frontier(queue_start, front_start, front_target, graph):
            path = build_path(front_start, front_target, queue_start[0])
            return {"path": path, "nodes_explored": nodes_explored, "path_length": len(path) - 1}

        # Expand from the target side
        if expand_frontier(queue_target, front_target, front_start, graph):
            path = build_path(front_start, front_target, queue_target[0])
            return {"path": path, "nodes_explored": nodes_explored, "path_length": len(path) - 1}

        # Increment nodes explored (for each expansion round)
        nodes_explored += 1

    # If no path exists
    return {"error": "No path exists between the given nodes."}

def expand_frontier(queue, this_front, other_front, graph):
    current = queue.popleft()

    for neighbor in graph[current]:
        if neighbor not in this_front:
            this_front[neighbor] = current
            queue.append(neighbor)

            if neighbor in other_front:  # Intersection found
                return True
    return False

def build_path(front_start, front_target, meeting_point):
    path_start = []
    path_target = []

    # Trace path from start to the meeting point
    while meeting_point:
        path_start.append(meeting_point)
        meeting_point = front_start[meeting_point]
    path_start.reverse()

    # Trace path from meeting point to the target
    meeting_point = front_target[path_start[-1]]
    while meeting_point:
        path_target.append(meeting_point)
        meeting_point = front_target[meeting_point]

    return path_start + path_target

# Example Graph
city_map = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Input nodes
start = "A"
target = "F"

# Execute Bi-Directional BFS
result = bidirectional_bfs(city_map, start, target)

# Output Result
if "error" in result:
    print(result["error"])
else:
    print(f"Shortest Path: {result['path']}")
    print(f"Nodes Explored: {result['nodes_explored']}")
    print(f"Path Length: {result['path_length']}")