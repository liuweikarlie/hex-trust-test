import heapq

class Edge:
    def __init__(self, dest, responseTime):
        '''
        dest: neighbor node
        responseTime: use ping to get the responseTime, edge weight
        '''
        self.dest = dest
        self.weight = responseTime

def dijkstra(graph, src):
   
    num_nodes = len(graph)
    dist = {node: float('inf') for node in range(num_nodes)}  # Initialize distances as infinity
    dist[src] = 0  # Distance from source to itself is 0
    pq = []  # Priority queue to store tentative distances

    heapq.heappush(pq, (0, src))  # Start with source vertex

    visited = set()  

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue 

        visited.add(current_node)

        for edge in graph[current_node]:
            neighbor = edge.dest
            new_dist = current_dist + edge.weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))  

    return dist


graph = {
    0: [Edge(1, 21), Edge(2, 4)],
    1: [Edge(2, 3), Edge(3, 6)],
    2: [Edge(0, 4), Edge(3, 8)],
    3: [Edge(1, 11), Edge(4, 5)],
    4: [Edge(3, 5)]
}

source = 0
distances = dijkstra(graph, source)
print(distances)
for node, distance in distances.items():
    if distance == float('inf'):
        print(f"No path from {source} to node {node}")
    else:
        print(f"Distance from {source} to node {node} is {distance}")
