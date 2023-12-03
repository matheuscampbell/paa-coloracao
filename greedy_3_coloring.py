def greedy_3_coloring(graph):
    coloring = {}
    for node in graph:
        available_colors = {1, 2, 3}
        for neighbor in graph[node]:
            if neighbor in coloring:
                available_colors.discard(coloring[neighbor])
        if available_colors:
            coloring[node] = available_colors.pop()
        else:
            return None
    return coloring

# Exemplo de uso
print(greedy_3_coloring(graph))
