from collections import deque

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, [start])])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nodes_explored = 0

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored

def dfs_explore_all(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    stack = [(start, [start])]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nodes_explored = 0

    while stack:
        (x, y), path = stack.pop()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored 

        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == 1:
                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored 

def compare_search_algorithms(maze, start, end):
    bfs_path, bfs_nodes = bfs_shortest_path(maze, start, end)
    dfs_path, dfs_nodes = dfs_explore_all(maze, start, end)

    print("BFS Shortest Path:", bfs_path)
    print("BFS Nodes Explored:", bfs_nodes)
    print("DFS Valid Path:", dfs_path)
    print("DFS Nodes Explored:", dfs_nodes)
    
    
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

start = (0, 0)
end = (3, 4)

compare_search_algorithms(maze, start, end)