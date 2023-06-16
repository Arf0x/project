#https://www.youtube.com/watch?v=V6H1qAeB-l4
#

from collections import defaultdict
import heapq


class Graph:
    # create adjacency list first to present the graph
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    #
    def add_edge(self, src, dest, weight):

        # from source to destination vertex
        self.adjacencyList[src].append((dest, weight))
        # from destinationa vertex to another vertex
        self.adjacencyList[dest].append((src, weight))

    def dijkstra(self, src, vertices):

        # initial configuration
        # source to source is always 0
        pq = [(0, src)]

        # create an array to store the distance
        # set all the element size to infinite value
        dist = [float("inf") for i in range(vertices)]

        # set the distance of source to itself = 0
        dist[src] = 0

        # iteration within the heap/ priority queue
        while pq:
            # pop the node with least distance from the heap
            dis, node = heapq.heappop(pq)

            # updates the distance if the dis + new edgeWeight is lesser than
            # original distance
            for x in self.adjacencyList[node]:
                edgeWeight = x[1]
                adjNode = x[0]

                # compare the new distance and the previously acquired distance
                if dis + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dis + edgeWeight
                    heapq.heappush(pq, (dist[adjNode], adjNode))
        return dist

    print("Vertex   Distance from Source")

    def print_output(self, dist):
        for i in range(len(dist)):
            print(f"{i}          {dist[i]}")


# graph creation
g = Graph()
# number of vertices
V = 6
# source node
S = 0


# adjacency node 0
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)

# adjacency node 1
g.add_edge(1, 0, 4)
g.add_edge(1, 2, 2)

# adjacency node 2
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 4, 1)
g.add_edge(2, 5, 6)

# adjacency node 3
g.add_edge(3, 2, 3)
g.add_edge(3, 5, 2)

# adjacency node 4
g.add_edge(4, 2, 1)
g.add_edge(4, 5, 3)


# adjacency node 5
g.add_edge(5, 2, 6)
g.add_edge(5, 3, 2)
g.add_edge(5, 4, 3)


distances = g.dijkstra(S, V)
g.print_output(distances)
