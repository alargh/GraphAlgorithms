class MaxFlowGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices + 1)]
        self.flow_network = [[0] * (vertices + 1) for _ in range(vertices + 1)]

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity])
        self.graph[v].append([u, 0])

    def bfs_path(self, source, sink, parent):
        visited = [False]*(self.V + 1)
        parent[source] = -1
        Q = [source]
        visited[source] = True
        while Q:
            v = Q.pop(0)
            for u, c in self.graph[v]:
                residual_capacity = c - self.flow_network[v][u]
                if residual_capacity > 0 and not visited[u]:
                    Q.append(u)
                    visited[u] = True
                    parent[u] = v
                    if u == sink:
                        return True
        return False

    def ford_fulkerson_bfs(self, source, sink):
        max_flow = 0
        parent = [-1 for _ in range(self.V + 1)]

        while self.bfs_path(source, sink, parent):
            current_flow = float("inf")

            u = sink

            while u != source:
                for v, c in self.graph[parent[u]]:
                    if v == u:
                        current_flow = min(current_flow, c - self.flow_network[parent[u]][u])
                u = parent[u]

            u = sink
            while u != source:
                self.flow_network[parent[u]][u] += current_flow
                self.flow_network[u][parent[u]] -= current_flow
                u = parent[u]
            max_flow += current_flow

        return max_flow

    def dfs_path(self, source, sink, parent):
        visited = [False] * (self.V + 1)

        def dfs(u):
            visited[u] = True
            if u == sink:
                return True
            for v, c in self.graph[u]:
                residual_capacity = c - self.flow_network[u][v]
                if not visited[v] and residual_capacity > 0:
                    parent[v] = u
                    if dfs(v):
                        return True

            return False
        return dfs(source)


    def ford_fulkerson_dfs(self, source, sink):
        max_flow = 0
        parent = [-1 for _ in range(self.V + 1)]

        while self.dfs_path(source, sink, parent):
            current_flow = float("inf")

            u = sink

            while u != source:
                for v, c in self.graph[parent[u]]:
                    if v == u:
                        current_flow = min(current_flow, c - self.flow_network[parent[u]][u])
                u = parent[u]

            u = sink
            while u != source:
                self.flow_network[parent[u]][u] += current_flow
                self.flow_network[u][parent[u]] -= current_flow
                u = parent[u]
            max_flow += current_flow

        return max_flow

def max_flow_bfs(file_name, source, sink):

    V, E = loadWeightedGraph(file_name)
    graph = MaxFlowGraph(V)

    for u, v, w in E:
        graph.add_edge(u, v, w)

    return graph.ford_fulkerson_bfs(source, sink)


def max_flow_dfs(file_name, source, sink):
    V, E = loadWeightedGraph(file_name)
    graph = MaxFlowGraph(V)

    for u, v, w in E:
        graph.add_edge(u, v, w)

    return graph.ford_fulkerson_dfs(source, sink)


def loadWeightedGraph(file_name):
    if file_name == "example1.txt":
        V = 4
        E = [(1, 2, 3), (1, 3, 3), (2, 3, 1), (2, 4, 2), (3, 4, 2)]
        return V, E
    elif file_name == "example2.txt":
        V = 6
        E = [(1, 2, 10), (1, 3, 10), (2, 4, 5), (3, 4, 15), (4, 5, 10)]
        return V, E
    return 0, []

def test_max_flow_bfs():
    source = 1
    sink = 4
    file_name = "example1.txt"
    max_flow = max_flow_bfs(file_name, source, sink)
    print(f"Max flow using BFS: {max_flow}")

def test_max_flow_dfs():
    source = 1
    sink = 4
    file_name = "example1.txt"
    max_flow = max_flow_dfs(file_name, source, sink)
    print(f"Max flow using DFS: {max_flow}")

test_max_flow_bfs()
test_max_flow_dfs()
