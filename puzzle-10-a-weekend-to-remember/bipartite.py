# Programming for the Puzzled -- Srini Devadas
# A Weekend to Remember
# This puzzle deals with the problem of inviting friends to dinner over two days
# such that no two of your friends who dislike each other are invited on the same
# day.  This can be done if the graph is a bipartite graph.

# The code determines if a graph is bipartite or not. If the graph can be colored
# using two colors, it is bipartite, else it is not.

graph = {'B': ['C'],
         'C': ['B', 'D'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'F': ['D', 'G', 'H', 'I'],
         'G': ['F'],
         'H': ['F'],
         'I': ['F']}

graph2 = {'F': ['D', 'I', 'G', 'H'],
          'B': ['C'],
          'D': ['C', 'E', 'F'],
          'E': ['D'],
          'H': ['F'],
          'C': ['D', 'B'],
          'G': ['F'],
          'I': ['F']}

gra3 = {'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']}

grap = {'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['D', 'B'],
        'D': ['A', 'C']}

graph_disconnected = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C', 'E', 'F'],
    'E': ['D'],
    'F': ['D', 'G', 'H', 'I'],
    'G': ['F'],
    'H': ['F'],
    'I': ['F']
}

graphc = {'A': ['B', 'D', 'C'],
          'B': ['C', 'A', 'B'],
          'C': ['D', 'B', 'A'],
          'D': ['A', 'C', 'B']}


def bipartiteGraphColor(graph, start, coloring, color, cycle=[], first_vertex=True):

    if start not in graph:
        return False, {}

    if start not in coloring:
        coloring[start] = color
    elif coloring[start] != color:
        cycle.append(start)
        return False, {}
    else:
        return True, coloring

    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'

    for vertex in graph[start]:
        val, coloring = bipartiteGraphColor(
            graph, vertex, coloring, newcolor, cycle, False)
        if val is False:
            cycle.append(start)
            if first_vertex:
                print(
                    f"Here is a cyclic path that cannot be colored {cycle[::-1]}")
            return False, {}

    return True, coloring


def full_bipartite(graph):
    coloring = {}
    color = 'Sha'
    for node in graph:
        if node not in coloring:
            is_bipartite, coloring = bipartiteGraphColor(
                graph, node, coloring, color)
            if is_bipartite is False:
                return False, {}
    return is_bipartite, coloring


def find_path(graph, start, end, traversed=set(), path=[]):
    if start in traversed:
        return False, []

    traversed.add(start)
    path.append(start)

    if start == end:
        return True, path

    for vertex in graph[start]:
        found, _ = find_path(graph, vertex, end, traversed, path)
        if found is True:
            return True, path

    path.remove(start)
    return False, []


if __name__ == "__main__":
    # print(bipartiteGraphColor(gra3, 'A', {}, 'Sha'))
    # print(bipartiteGraphColor(graph, 'B', {}, 'Sha'))
    # print(bipartiteGraphColor(graph2, 'B', {}, 'Sha'))
    # print(bipartiteGraphColor(grap, 'A', {}, 'Sha'))

    # print(full_bipartite(graph_disconnected))

    # print(bipartiteGraphColor(graphc, 'A', {}, 'Sha'))

    print(find_path(graph, 'B', 'I'))
