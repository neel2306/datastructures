from typing import Any, List, Generator

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, nodes: List[Any]) -> None:
        self.nodes = nodes.copy() # To track head
        self.head = None
        self.tail = None

        if nodes is not None:
            node = Node(value=nodes.pop(0)) # Beginning of the linked list
            self.nodes.pop(0)
            self.head = node

            if len(nodes) == 0: # If there is only one node
                self.tail = node
                node.next = None

            for value in nodes:
                node.next = Node(value=value) # Referencing the next value to the next node
                node = node.next # Defining the next node
                if len(self.nodes) == 1:
                    self.tail = node
                    node.next = None
                self.nodes.pop(0)
                    
    def insert_at_beginning(self, value: Any) -> None:

        new_node = Node(value=value)
        # Assign current head node as the next of the new node
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, value: Any) -> None:

        new_node = Node(value=value)
        # Assign next of current tail to the new node
        self.tail.next = new_node
        new_node.next = None
        self.tail = new_node
    
    def insert_at_index_x(self, value: Any, position: int) -> None:
        
        new_node = Node(value=value)
        if self.head is None:
            raise ValueError("Empty linked list")
        
        node = self.head

        if position == 0:
            self.insert_at_beginning(value=value)
        
        if position == -1:
            self.insert_at_end(value=value)

        counter = 1
        # Loop through
        while node.next is not None:
            if counter == position:
                new_node.next = node.next
                node.next = new_node
                break
            node = node.next
            counter += 1
    
    def delete_at_beginning(self) -> None:

        self.head = self.head.next
    
    def delete_at_end(self) -> None:

        node = self.head

        while node.next is not None:
            previous_node = node
            next_node = node.next
            node = next_node
        
        self.tail = previous_node
        self.tail.next = None
    
    def delete_at_value_x(self, target_value: Any) -> None:

        if self.head is None:
            raise ValueError("Empty linked list")
        
        node = self.head

        if self.head.value == target_value:
            self.delete_at_beginning()
        elif self.tail.value == target_value:
            self.delete_at_end()

        while node.next is not None:
            previous_node = node
            next_node = node.next

            if next_node.value == target_value:
                previous_node.next = next_node.next
                break
            node = next_node

    def __iter__(self) -> Generator[Any]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

if __name__ == "__main__":
    linked_list = LinkedList(nodes=["a", 1, "b", 2])
    linked_list.insert_at_beginning("first")
    linked_list.insert_at_end("last")
    linked_list.insert_at_index_x(value="index", position=-1)
    linked_list.delete_at_beginning()
    linked_list.delete_at_end()
    linked_list.delete_at_value_x(target_value="b")

    for node in linked_list:
        print(node.value)
