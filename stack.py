from typing import Any

class Stack:
    def __init__(self):
        # Initialize an empty array
        self.array = []
    
    def push(self, element: Any) -> None:

        # Add an element to the end of the stack
        self.array.append(element)

    def pop(self) -> Any:

        # Remove the last element
        popped_element = self.array.pop()
        print(f"Removed element {popped_element}, stack now has {len(self.array)} elements")
    
    def peek(self) -> Any:
        # To view the last element of a stack
        if self.array:
            last_element = self.array[-1]
            print(f"Last element in the stack: {last_element}")
        
        else:
            raise ValueError("The stack is currently empty!")

if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push("Hello")
    stack.push("1234")
    stack.pop()
    stack.peek()
    stack.pop()
    stack.pop()
    stack.peek()