def create_graph_from_3sat(clauses):
    graph = {}
    # Cada cláusula cria um pequeno grafo (gadget)
    for i, clause in enumerate(clauses):
        # Adiciona vértices e arestas ao grafo baseado na cláusula
        # Esta é uma versão simplificada; a construção real é mais complexa
        graph[f'c{i}_1'] = [f'c{i}_2', f'c{i}_3']
        graph[f'c{i}_2'] = [f'c{i}_1', f'c{i}_3']
        graph[f'c{i}_3'] = [f'c{i}_1', f'c{i}_2']
    
    return graph

def is_3_colorable(graph):
    # Implementação simplificada da verificação de 3-coloração
    # Um algoritmo real seria mais complexo e envolveria backtracking
    return greedy_3_coloring(graph) is not None

# Exemplo de uso
clauses = [
    ('x1', '~x2', 'x3'),
    ('~x1', 'x2', '~x3'),
    # Mais cláusulas podem ser adicionadas aqui
]

graph = create_graph_from_3sat(clauses)
print("O grafo é 3-colorível?" , is_3_colorable(graph))
