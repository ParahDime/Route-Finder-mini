import heapq #used for heap queues

# BFS shortest path
# #Graph structure
class GraphExplorer:
    def init(self):
        self.graph = {}

    def build_graph(self, locations, connections):
        #create a dict
        for location in locations:
            self.graph[location] = []

        #add connections
        for loc1, loc2, distance in connections:
            self.graph[loc1].append((loc2, distance))
            self.graph[loc2].append((loc1, distance))

    def shortest_path(self, start, end):
        #Priority queue
        prioqu = [(0, start)]

        #distances to a node
        distances = {location: float("inf") for location in self.graph}
        distances[start] = 0

        #path reconstruction
        previous = {location: None for location in self.graph}


        while prioqu:
            current_distance, current_location = heapq.heappop(prioqu)

            #destination node reached
            if current_location == end:
                break

            #if better path found
            if current_distance > distances[current_location]:
                continue

            #explore adjacent nodes
            for neighbor, weight in self.graph[current_location]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_location
                    heapq.heappush(prioqu, (new_distance, neighbor))

        #Build the path
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path, distances[end]