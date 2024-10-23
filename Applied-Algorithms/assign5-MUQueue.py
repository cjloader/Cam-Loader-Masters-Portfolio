class MUQueue:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None 
        self.end = None 
        self._size = 0     # Keep track of the size

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.end is None:
            # Queue is empty
            self.head = self.end = new_node
        else:
            # Add new node at the end and update end
            self.end.next = new_node
            self.end = new_node
        self._size += 1

    def dequeue(self):
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            # If the queue is now empty, update end as well
            self.end = None
        self._size -= 1
        return removed_data

    def size(self):
        return self._size

    def peek(self):
        return self.head.data


menu = True
queue = MUQueue()
while menu:
   print("1. Add item.")
   print("2. Delete item.")
   print("3. Quit.")

   userInput = input("Please select an option above: ")
   if userInput == '1':
      data = input("Please enter a value to add to the Queue: ")
      queue.enqueue(data)

   if userInput == '2':
      queue.dequeue()
   
   if userInput == '3':
      menu = False