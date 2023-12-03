def is_valid_coloring(graph, coloring):
    for vertex, edges in graph.items():
        for neighbor in edges:
            if coloring[vertex] == coloring[neighbor]:
                return False
    return True

def brute_force_3_coloring(graph):
    nodes = list(graph.keys())
    for color1 in range(1, 4):
        for color2 in range(1, 4):
            for color3 in range(1, 4):
                # Criar todas as combinações possíveis de cores
                for coloring in itertools.product([color1, color2, color3], repeat=len(nodes)):
                    if is_valid_coloring(graph, dict(zip(nodes, coloring))):
                        return dict(zip(nodes, coloring))
    return None

# Exemplo de uso
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
print(brute_force_3_coloring(graph))
