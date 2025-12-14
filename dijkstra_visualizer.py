"""
Dijkstra's Algorithm - Step Based Implementation
------------------------------------------------
This implementation is designed for algorithm visualization and
educational purposes as part of a Design and Analysis of Algorithms project.

Features:
- Step-by-step execution tracking
- Distance table updates
- Visited node tracking
- Visualization-friendly data structure

Time Complexity: O((V + E) log V)
Space Complexity: O(V)
"""

import heapq


class DijkstraVisualizer:
    def __init__(self, graph):
        """
        Initialize the graph.

        Parameters:
        graph (dict): Adjacency list representation of the graph
        Example:
        {
            'A': {'B': 4, 'C': 1},
            'B': {'A': 4, 'C': 2, 'D': 5},
            'C': {'A': 1, 'B': 2, 'D': 8},
            'D': {'B': 5, 'C': 8}
        }
        """
        self.graph = graph
        self.steps = []

    def run(self, start_node):
        """
        Execute Dijkstra's Algorithm from the start node.

        Parameters:
        start_node (str): Starting node for the algorithm

        Returns:
        distances (dict): Shortest distance from start_node to all nodes
        steps (list): Step-by-step execution data for visualization
        """

        # Initialize distances
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0

        visited = set()
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            # Record current step
            self.steps.append({
                "action": "visit_node",
                "current_node": current_node,
                "distances": distances.copy(),
                "visited_nodes": list(visited)
            })

            # Relax edges
            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = current_distance + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))

                        # Record relaxation step
                        self.steps.append({
                            "action": "relax_edge",
                            "from": current_node,
                            "to": neighbor,
                            "updated_distance": new_distance,
                            "distances": distances.copy()
                        })

        return distances, self.steps


# Example execution (for testing purposes)
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 1},
        'B': {'A': 4, 'C': 2, 'D': 5},
        'C': {'A': 1, 'B': 2, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }

    visualizer = DijkstraVisualizer(graph)
    final_distances, execution_steps = visualizer.run('A')

    print("Final Shortest Distances:")
    for node, distance in final_distances.items():
        print(f"{node}: {distance}")

    print("\nExecution Steps:")
    for step in execution_steps:
        print(step)
