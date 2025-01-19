from typing import Tuple, List

class Node:
  def __init__(self):
    self.edges = {}
    self.merged_vertecies  = {self}
    self.active = True

  def addEdge(self, to, weight):
    self.edges[to] = self.edges.get(to, 0) + weight

  def delEdge(self, to):
    if to in self.edges:
        del self.edges[to]

class Graph:
    def __init__(self, V, edges):
        self.nodes = [Node() for _ in range(V)]
        self.n = V
        for (x, y, c) in L:
            x -= 1
            y -= 1
            self.nodes[x].addEdge(y, c)
            self.nodes[y].addEdge(x, c)

    def merge_vertecies(self, v1, v2):

        for v3, w in self.nodes[v2].edges.items():
            if v3 != v1:
                self.nodes[v1].addEdge(v3, w)
                self.nodes[v3].addEdge(v1, w)

                self.nodes[v3].delEdge(v2)
                self.nodes[v1].delEdge(v2)

        self.nodes[v1].merged_vertecies.update(self.nodes[v2].merged_vertecies)

        self.nodes[v2].active = False
        self.nodes[v2].edges.clear()
        self.n -= 1

    def get_active_vertecies(self):
        return [v for v, node in enumerate(self.nodes) if node.active]

def minimumCutPhase(G):
    Vertecies = G.get_active_vertecies()
    if len(Vertecies) <= 1:
        return float('inf')

    a = Vertecies[0]
    S = {a}
    weights = {v: 0 for v in Vertecies}

    for v, w in G.nodes[a].edges.items():
        if G.nodes[v].active:
            weights[v] = w

    cut_order = [a]
    last_cut = 0

    while len(S) != len(Vertecies):
        max_weight = -(float)('inf')

        current_vertex = None
        for v in Vertecies:
            if weights[v] > max_weight and v not in S:
                max_weight = weights[v]
                current_vertex = v

        if current_vertex is None:
            break

        for v, w in G.nodes[current_vertex].edges.items():
            if v not in S and G.nodes[v].active:
                weights[v] += w

        cut_order.append(current_vertex)
        S.add(current_vertex)

    last_cut = max_weight

    if len(cut_order) <= 1:
        return float('inf')

    last_v = cut_order[-1]
    pre_last_v = cut_order[-2]
    G.merge_vertecies(last_v, pre_last_v)

    return last_cut

def stoerWagner(V, L):
    G = Graph(V, L)
    min_cut = float('inf')

    while G.n > 1:
        current_cut = minimumCutPhase(G)
        min_cut = min(min_cut, current_cut)

    return min_cut

def loadWeightedGraph() -> Tuple[int, List[Tuple[int, int, int]]]:
    V = 4
    L = [
        (1, 2, 4),
        (1, 3, 5),
        (2, 3, 7),
        (2, 4, 10),
        (3, 4, 3)
    ]
    return V, L

V: int
L: Tuple[int, int, int]

(V, L) = loadWeightedGraph()
result = stoerWagner(V, L)
print(result)