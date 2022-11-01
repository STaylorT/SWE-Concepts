from collections import defaultdict

# this class represents an undirected graph
class Graph: 
    
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, neighbor):
        self.graph[vertex].append(neighbor)
        self.graph[neighbor].append(vertex)

    def BFS(self, start_vertex):
        # collection of visited vertices
        visited = set()

        # queue of vertices to visit
        queue = list()

        # we begin with the given start vertex
        queue.append(start_vertex)

        while (queue): # continue until the queue is empty
            # get the next vertex from the queue, then "visit" it
            curr_vertex = queue.pop(0)
            visited.add(curr_vertex)
            print(curr_vertex)

            # look at all neighbors of the current vertex (single depth level)
            for neighbor in self.graph[curr_vertex]:
                # add neighbors to the queue that haven't been visited AND are not already in the queue
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 6)

    g.BFS(2)
