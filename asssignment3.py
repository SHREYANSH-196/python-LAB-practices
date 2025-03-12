from collections import deque

def bidirectional_bfs(graph, start, target):
    if start == target:
        return [start]
    front_start = {start: None}
    front_target = {target: None}
    queue_start = deque([start])
    queue_target = deque([target])

    while queue_start and queue_target:
        if expand_frontier(queue_start, front_start, front_target, graph):
            return build_path(front_start, front_target, front_start[queue_start[0]])
        if expand_frontier(queue_target, front_target, front_start, graph):
            return build_path(front_start, front_target, queue_target[0])
    return None

def expand_frontier(queue, this_front, other_front, graph):
    current = queue.popleft()

    for neighbor in graph[current]:
        if neighbor not in this_front:
            this_front[neighbor] = current
            queue.append(neighbor)
            
            if neighbor in other_front:
                return True
    return False

def build_path(front_start, front_target, meeting_point):
    path_start = []
    path_target = []
    while meeting_point:
        path_start.append(meeting_point)
        meeting_point = front_start[meeting_point]
    path_start.reverse()

    meeting_point = front_target[path_start[-1]]
    while meeting_point:
        path_target.append(meeting_point)
        meeting_point = front_target[meeting_point]

    return path_start + path_target

city_map = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C", "E"]
}

start = "A"
target = "F"
path = bidirectional_bfs(city_map, start, target)
print("Shortest Path:", path)