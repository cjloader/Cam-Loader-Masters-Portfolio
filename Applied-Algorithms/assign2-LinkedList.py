class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HWLinkedList:
    def __init__(self):
        self.head = None
 
    # Private toString Method
    def __toString(self):
        return 
    # Public toString Method
    def toString(self):
        output = ""
        current = self.head
        while current:
            current.data.toString()
            current = current.next

        return output
            
       
    # Private add Method
    def __add(self, data):
        return
    # Public add Method
    def add(self, data):
        node = Node(data)
        if self.head is None:
           self.head = node
           return
        else:
            node.next = self.head
            self.head = node
        
    def addAtHead(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node
            return

    def searchList(self, value):
        current = self.head
        while current != None:
            if current.data == value:
               return True
            else:
                current = current.next
        return False

   

    def remove(self, data):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
               currentNode = currentNode.next
        if currentNode is None:
            return
        return

class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.next = None

    def __init__(self):
        pass

    def toString(self):
        print("Name: "+self.name+" House: "+self.house)
    
    def isEqual(self, x):
        
            return True

class HWLinkedListTest:
  studentList = HWLinkedList()
  menu = True
  while(menu):
      print("1. Add a new student to the end")
      print("2. Add a new student to the head")
      print("3. Remove a student")
      print("4. Search for a student")
      print("5. Print all students")
      print("6. QUIT")

      option = input("Please choose an option: ")
      if option == '1':
         student = Student()
         name = input("Please enter stundent's name: ")
         house = input("Please enter the house name: ")
         student.name = name
         student.house = house
         studentList.add(student)
         print("Student: "+student.name+ "House: "+student.house+" was added.")
       
      if option == '2':
         student = Student()
         name = input("Please enter stundent's name: ")
         house = input("Please enter the house name: ")
         student.name = name
         student.house = house
         studentList.addAtHead(student)
         print("Student: "+student.name+ "House: "+student.house+" was added to the head.")


      if option == '3':
        name = input("Please enter student's name to remove: ")
        # Create a student object for comparison
        student = Student(name, "")
        studentList.remove(student)
        print(f"Student: {name} was removed.")

      if option == '4':
            name = input("Please enter student's name to search: ")
            student = Student(name, "")
            found = studentList.searchList(student)
            if found:
                print(f"Found {student.name}")
            else:
                print("Not Found")


      if option == '5':
         studentList.toString()

      if option == '6':
         menu = False