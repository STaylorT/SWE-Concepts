from collections import defaultdict

# this class represented an undirected graph
class Graph: 
    
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, neighbor):
        self.graph[vertex].append(neighbor)
        self.graph[neighbor].append(vertex)

    def DFSUtil(self, vertex, visited):
        visited.add(vertex)
        print("visited ", vertex, " ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, start_vertex):
        visited = set()

        self.DFSUtil(start_vertex, visited)

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

    print("The following is the DFS starting from vertex 2")
    g.DFS(2)
