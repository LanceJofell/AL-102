import heapq
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Initialize distances dictionary with all vertices having infinite distance from the start
    distances = {vertex: float('inf') for vertex in graph}
    # Distance from start to start is 0
    distances[start] = 0
    
    # Priority queue to store vertices and their corresponding distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If the distance to the current vertex is already shorter than the one in the queue, skip it
        if current_distance > distances[current_vertex]:
            continue
        
        # Check the distances to neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # If the distance to the neighbor through the current vertex is shorter than the recorded distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add the neighbor and its distance to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def visualize_graph(graph):
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            plt.plot([vertex[0], neighbor[0]], [vertex[1], neighbor[1]], 'bo-')
            plt.text((vertex[0] + neighbor[0]) * 0.5, (vertex[1] + neighbor[1]) * 0.5, str(weight))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph Visualization')
    plt.grid(True)
    plt.show()

# Example usage:
graph = {
    (0, 0): {(0, 1): 4, (1, 1): 1, (1, 0): 2},
    (0, 1): {(0, 0): 4, (1, 1): 3},
    (1, 0): {(0, 0): 2, (1, 1): 5},
    (1, 1): {(0, 0): 1, (0, 1): 3, (1, 0): 5}
}

print("Shortest distances from (0, 0) to other vertices:")
print(dijkstra(graph, (0, 0)))

visualize_graph(graph)
