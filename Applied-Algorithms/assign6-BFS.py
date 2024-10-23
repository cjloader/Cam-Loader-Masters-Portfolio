from operator import index
from pickle import TRUE

class Vertex:
    def __init__(self, index):
        self.visited = False
        self.index = index

    def get_visited(self):
        return self.visited

    def get_index(self):
        return self.index

    def set_visited(self, visited):
        self.visited = visited

class Searches:
   def BFS(self, myVertex, adjacency, n, start):
         if start not in self.vertices:
            return []

        # Queue for BFS
         queue = deque()
         visited_order = []
        
        # Start with the initial vertex
         start_vertex = self.vertices[start]
         queue.append(start_vertex)
         start_vertex.set_visited(True)

         while myQueue:
            current_vertex = myQueue.dequeue()
            visited_order.append(current_vertex.get_index())

            for neighbor in current_vertex.adjacency_list:
                if not neighbor.get_visited():
                    neighbor.set_visited(True)
                    queue.append(neighbor)

         return visited_order
       

myQueue = MUQueue()

myQueue

FALSE = "FALSE"
TRUE = "TRUE"
adjacencyMatrix = [[FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE],
                        [TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,TRUE,FALSE,FALSE],
                        [FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE,TRUE],
                        [TRUE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE],
                        [FALSE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE],
                        [FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,FALSE],
                        [FALSE,TRUE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE],
                        [FALSE,TRUE,FALSE,FALSE,TRUE,FALSE,TRUE,TRUE,FALSE,FALSE],
                        [FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE],
                        [FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE]]