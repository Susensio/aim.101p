graph_not_bipartite = {
    'A': [],
    'B': ['C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'F'],
    'E': ['D'],
    'F': ['D', 'G', 'H', 'I'],
    'G': ['F', 'H'],
    'H': ['F', 'G'],
    'I': ['F'],
}
graph_bipartite = {
    'A': [],
    'B': ['C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'F'],
    'E': ['D'],
    'F': ['D', 'G', 'H', 'I'],
    'G': ['F'],
    'H': ['F'],
    'I': ['F'],
}


class NotBipartite(Exception):
    pass


def bipartite(graph: dict):
    colored_graph = {}
    try:
        for node in graph:
            if node not in colored_graph:
                color_branch(graph, colored_graph, node)
    except NotBipartite:
        return False
    else:
        return colored_graph


def color_branch(graph, colored_graph, node, current_color=False):
    if node not in colored_graph:
        colored_graph[node] = current_color
        current_color = not current_color
        for child in graph[node]:
            color_branch(graph, colored_graph, child, current_color)
    else:
        if colored_graph[node] != current_color:
            raise NotBipartite()


def test_bipartite():
    colors = bipartite(graph_bipartite)
    color1 = colors['B']
    color2 = colors['C']
    assert all(colors[k] == color1 for k in ('B', 'D', 'G', 'H', 'I'))
    assert all(colors[k] == color2 for k in ('C', 'F', 'E'))
    assert colors['A'] in (color1, color2)


def test_not_bipartite():
    assert bipartite(graph_not_bipartite) is False


if __name__ == "__main__":
    print(bipartite(graph_bipartite))
    print(bipartite(graph_not_bipartite))
