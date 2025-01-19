class Node:
  def __init__(self, idx):
    self.idx = idx
    self.out = set()

  def connect_to(self, v):
    self.out.add(v)

def create_graph(G):
    (V, L) = loadWeightedGraph(G)

    G = [None] + [Node(i) for i in range(1, V+1)]

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)

    return G


def LEX_BFS(graph):
    n = len(graph)
    all_sets = [{graph[i].idx for i in range(1, n)}]
    result = []
    while all_sets:
        current_sets = []
        e = all_sets[-1].pop()
        result.append(e)
        for S in all_sets:
            if not S:
                continue

            R = S & graph[e].out
            L = S - R
            if L:
                current_sets.append(L)
            if R:
                current_sets.append(R)
        all_sets = current_sets
    return result


def checkLexBFS(G, vs):
  n = len(G)
  pi = [None] * n
  for i, v in enumerate(vs):
    pi[v] = i

  for i in range(n-1):
    for j in range(i+1, n-1):
      Ni = G[vs[i]].out
      Nj = G[vs[j]].out

      verts = [pi[v] for v in Nj - Ni if pi[v] < i]
      if verts:
        viable = [pi[v] for v in Ni - Nj]
        if not viable or min(verts) <= min(viable):
          return False
  return True


def is_chordal(G):
    a = LEX_BFS(G)
    a.reverse()
    return checkLexBFS(G, a)


def loadWeightedGraph(G):
    V = 5
    L = [
        (1, 2, 1), (1, 3, 1),
        (2, 4, 1), (2, 5, 1),
        (3, 4, 1), (4, 5, 1)
    ]
    return V, L


G = []
graph = create_graph(G)

result = is_chordal(graph)
print("Is the graph chordal?", result)
