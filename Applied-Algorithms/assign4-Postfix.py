#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class MUStack:
    def __init__(self):
        self.head = Node(None)  
        self.size = 0           

    def pop(self):
        # Remove the top node
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value
    
    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def peek(self):
        return self.head.next.value

    def size(self):
        return self.size
    
    def evaluate(self, exp, myStack):
    # Split the expression into tokens
      tokens = exp.split()
    
      for token in tokens:
            if token.isdigit():  
                myStack.push(int(token))  # Convert to int and push onto the stack
            else:
                # Pop two numbers from the stack
                secNum = myStack.pop()
                firstNum = myStack.pop()
                
                # Perform the operation
                if token == '+':
                    myStack.push(firstNum + secNum)
                elif token == '-':
                    myStack.push(firstNum - secNum)
                elif token == '*':
                    myStack.push(firstNum * secNum)
                elif token == '/':
                    myStack.push(firstNum / secNum)
        
      return myStack.pop()  # The final result will be the last item in the stack




menu = True   
while menu:
  postfixStr = input("Enter a space delimited postfix string or Q to exit: ")
  mystack = MUStack()
  if postfixStr == 'Q':
      menu = False
  else:
      print("The answer is: "+ str(mystack.evaluate(postfixStr,mystack)))