from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in range(len(ancestors)):
        graph.add_vertex(ancestors[i][0])
        graph.add_vertex(ancestors[i][1])
    for i in range(len(ancestors)):
        graph.add_edge(ancestors[i][1], ancestors[i][0])
    if len(graph.get_neighbors(starting_node)) == 0:
        return -1
    print(graph.bft(starting_node)[-1])
    return graph.bft(starting_node)[-1]
    # poss = graph.bft(starting_node)
    # print(poss)
    # answer = list(poss)
    # no_parents = []
    # for i in range(len(answer)):
    #     if len(graph.vertices[answer[i]]) == 0:
    #         no_parents.append(answer[i])
    #     else:
    #         return answer[-1]
    # if len(no_parents) == 1:
    #     return answer[-1]
    # if len(no_parents) > 1:
    #     no_parents.sort()
    #     return no_parents[0]




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 2)

# print("answer", earliest_ancestor(test_ancestors, 1))
# print("answer", earliest_ancestor(test_ancestors, 2))
# print("answer", earliest_ancestor(test_ancestors, 3))
# print("answer", earliest_ancestor(test_ancestors, 4))
# print("answer", earliest_ancestor(test_ancestors, 5))
# print("answer", earliest_ancestor(test_ancestors, 6))
# print("answer", earliest_ancestor(test_ancestors, 7))
# print("answer", earliest_ancestor(test_ancestors, 8))
# print("answer", earliest_ancestor(test_ancestors, 9))
# print("answer", earliest_ancestor(test_ancestors, 10))
# print("answer", earliest_ancestor(test_ancestors, 11))

# earliest_ancestor(test_ancestors, 1)
# earliest_ancestor(test_ancestors, 2)
# earliest_ancestor(test_ancestors, 3)
# earliest_ancestor(test_ancestors, 4)
# earliest_ancestor(test_ancestors, 5)
# earliest_ancestor(test_ancestors, 6)
# earliest_ancestor(test_ancestors, 7)
# earliest_ancestor(test_ancestors, 8)
# earliest_ancestor(test_ancestors, 9)
# earliest_ancestor(test_ancestors, 10)
# earliest_ancestor(test_ancestors, 11)