from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.fill_order(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        transposed_graph = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def dfs_scc(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_scc(neighbor, visited, result)

    def strongly_connected_components(self):
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        transposed_graph = self.transpose()

        visited = [False] * self.V
        scc_list = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                scc = []
                transposed_graph.dfs_scc(v, visited, scc)
                scc_list.append(scc)

        return scc_list

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:", g.strongly_connected_components())
