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
            path = path + [task]
            best_schedule.append((task, cost))

            for successor in self.graph:
                if task in self.graph[successor]:
                    self.in_degree[successor] -= 1
                    if self.in_degree[successor] == 0:
                        new_cost = cost + self.durations[task]
                        heapq.heappush(pq, (new_cost + self.heuristic(successor), new_cost, successor, path))

        return best_schedule

    def greedy_schedule(self):
        """Greedy approach: Always pick the shortest available task."""
        available_tasks = sorted(self.durations.items(), key=lambda x: x[1])
        return [(task, duration) for task, duration in available_tasks]

tasks = [
    ("A", 3, []), 
    ("B", 2, ["A"]), 
    ("C", 1, ["A"]), 
    ("D", 4, ["B", "C"]), 
    ("E", 2, ["D"])
]

scheduler = TaskSchedulerAStar(tasks)

optimal_schedule = scheduler.a_star_search()
print("A* Task Schedule:", optimal_schedule)

greedy_schedule = scheduler.greedy_schedule()
print("Greedy Task Schedule:", greedy_schedule)