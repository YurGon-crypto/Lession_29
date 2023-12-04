from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def all_pairs_shortest_path(self):
        shortest_paths = {}

        for i in range(self.V):
            shortest_paths[i] = self.bfs_shortest_path(i)

        return shortest_paths

    def bfs_shortest_path(self, start):
        visited = [False] * self.V
        distance = [-1] * self.V

        queue = deque()
        queue.append(start)
        visited[start] = True
        distance[start] = 0

        while queue:
            current_vertex = queue.popleft()

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    distance[neighbor] = distance[current_vertex] + 1

        return distance

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

shortest_paths = g.all_pairs_shortest_path()
print("All-Pairs Shortest Paths:")
for vertex in shortest_paths:
    print(f"From vertex {vertex}: {shortest_paths[vertex]}")
