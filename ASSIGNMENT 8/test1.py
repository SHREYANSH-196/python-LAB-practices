import heapq
class TaskSchedulerAStar:
    def __init__(self, tasks):
        self.graph = {}
        self.durations = {}
        self.in_degree = {}

        for task, duration, dependencies in tasks:
            self.graph[task] = dependencies
            self.durations[task] = duration 
            self.in_degree[task] = len(dependencies)

    def heuristic(self, task):
        def dfs(node, visited):
            if node in visited:
                return 0
            visited.add(node)
            return self.durations[node] + max((dfs(child, visited) for child in self.graph if node in self.graph[child]), default=0)

        return dfs(task, set())

    def a_star_search(self):
        pq = []
        start_tasks = [task for task in self.graph if self.in_degree[task] == 0]

        for task in start_tasks:
            heapq.heappush(pq, (self.heuristic(task), 0, task, []))

        best_schedule = []
        while pq:
            _, cost, task, path = heapq.heappop(pq)
            