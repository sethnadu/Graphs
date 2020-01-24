"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        # Check if v1 and v2 are in self.vertices
        # Add v2 to v1 set if so
        """

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # raise IndexError("That vertex does not exist")
            print("That vertex does not exist")
            return

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        # Return the vertex's set(...edges)
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        # Get a queue/stack as appropriate
        # Put the starting point in that 
        # Make a set to keep track of where you been
        # While there is stuff in queue/stack
        #   pop the first item
        #   if not visited:
        #       Do the thing
        #       Add to visited
        #       For each eedge in the item
        #           Add that edge to the queue/stack
        """

        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        visited_list = []

        while queue.size() > 0:
           v = queue.dequeue()
           if v not in visited:
                visited.add(v)
                visited_list.append(v)
                # print(v)
                for next_v in self.get_neighbors(v):
                    queue.enqueue(next_v)
        return visited_list

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        # Get a queue/stack as appropriate
        # Put the starting point in that 
        # Make a set to keep track of where you been
        # While there is stuff in queue/stack
        #   pop the first item
        #   if not visited:
        #       Do the thing
        #       Add to visited
        #       For each eedge in the item
        #           Add that edge to the queue/stack
        """
        stack = Stack()
        visited = set()
        visited_list = []
        stack.push(starting_vertex)

        while stack.size() > 0:
           v = stack.pop()
           if v not in visited:
                visited.add(v)
                visited_list.append(v)
                # print(v)
                for next_v in self.get_neighbors(v):
                    stack.push(next_v)
        return visited_list

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None: 
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                self.dft_recursive(i, visited)      
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]
            if v not in visited:
                if v is destination_vertex:
                    return path
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    shortest_path = list(path)
                    shortest_path.append(next_v)
                    queue.enqueue(shortest_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # stack = Stack()
        # visited = set()
        # stack.push([starting_vertex])
        # while stack.size() > 0:
        #     path = stack.pop()
        #     print("path", path)
        #     v = path[-1]
        #     print("v -1", v)
        #     if v not in visited:
        #         if v is destination_vertex:
        #             return path
        #         visited.add(v)
        #         for next_v in self.vertices[v]:
        #             shortest_path = list(path)
        #             shortest_path.append(next_v)
        #             stack.push(shortest_path)

        #  Code reviewed from class
        stack = Stack()
        visited = set()
        # Enstack Build a path with list []!
        stack.push([starting_vertex])

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_v in self.get_neighbors(vertex):
                # Add to the end make a copy of path, to avoid pass by reference bug
                    new_path = list(path)  #Make a copy rather than reference
                    new_path.append(next_v)
                    stack.push(new_path)
                    


    def dfs_recursive(self, starting_vertex,  target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    print("get neighbors", graph.get_neighbors(4))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs", graph.bfs(1, 6))
    graph.bfs(1, 6)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs", graph.dfs(1, 6))
    graph.dfs(1, 6)
    print("dfs recursive", graph.dfs_recursive(1, 6))
    graph.dfs_recursive(1, 6)
