# A linked list node
class Node:
    def __init__(self, x):
        # Constructor to initialize a new node with data
        self.data = x
        self.next = None

# Given the head of a list and an int, appends
# a new node at the end and returns the head.
def insertAtEnd(head, x):
    # Create a new node
    newNode = Node(x)

    # If the Linked List is empty, make
    # the new node as the head and return
    if head is None:
        return newNode

    # Store the head reference in a temporary variable
    last = head

    # Traverse till the last node
    while last.next is not None:
        last = last.next

    # Change the next pointer of the last node 
    # to point to the new node
    last.next = newNode

    # Return the head of the list
    return head

# This function prints the contents 
# of the linked list starting from the head
def printList(node):
    while node is not None:
        print(node.data, end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

if __name__ == "__main__":
    # Create a linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = insertAtEnd(head, 6)

    printList(head)