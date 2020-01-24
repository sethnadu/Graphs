from graph import Graph

'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''
'''

connected - has edges, connected components
array/2d
n, s, e, w - neighbors - edges
binary - values
island/ 1 island - connected components
return 1 islands - number of connected components

islands[0][4] is 0

'''

def island_counter(islands_array):
    graph = Graph()

    for i in range(len(islands_array)):
        for j in range(len(islands_array[i])):
            if islands_array[i][j] is 1:
                location = (i, j)
                graph.add_vertex(location)
            # print(islands_array[i][j])
    print("vertices", graph.vertices)

    



islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands)




