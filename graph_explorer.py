# BFS shortest path
# #Graph structure
class graph_explorer:
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

    def shortest_path(self):
        #breadth first search
        #returns the path chosen
        pass