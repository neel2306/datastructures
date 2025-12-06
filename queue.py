from typing import Any

class Queue:
    def __init__(self):
        
        self.array = []
        self.head = None
        self.tail = None
    
    def enqueue(self, element: Any) -> None:

        self.array.append(element)
        
        if self.array:
            self.head = self.array[0]
            self.tail = self.array[-1]
    
    def dequeue(self) -> None:

        if self.array:
            dequeued_element = self.array.pop(0)
            print(f"Removed element {dequeued_element} from the queue")
            if len(self.array) > 0:
                self.head = self.array[0]
                self.tail = self.array[-1]
            else:
                self.head = None
                self.tail = None
        else:
            raise ValueError("Queue is empty!")
    
    def isEmpty(self) -> None:

        if self.array:
            print(False)
        else:
            print(True)

    def peek(self) -> None:

        if self.array:
            first_element = self.head
            print(f"First element on the queue is: {first_element}; there are {len(self.array)} items left")
        
        else:
            raise ValueError("Queue is empty!")

    def clearQueue(self):
        print("Cleared queue!")
        self.array = []
    
    def viewQueue(self):
        print(self.array)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(67)
    queue.enqueue("World!")
    queue.enqueue("888")
    queue.viewQueue()
    queue.dequeue()
    queue.dequeue()
    queue.clearQueue()
    queue.viewQueue()
