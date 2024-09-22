#!/usr/bin/python3

"""Define classes Node and SingLinkedList for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/Set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get/Set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList. """
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list depending
        on it value in ascending order.

        Args:
            value (Node): The new Node to insert.
        """
        NewNode = Node(value)
        if self.__head is None:
            self.__head = NewNode
            return

        current = self.__head
        prev = None
        while current is not None:
            if current.data > NewNode.data:
                NewNode.next_node = current
                if prev is not None:
                    prev.next_node = NewNode
                else:
                    self.__head = NewNode
                break
            prev = current
            current = current.next_node

        if current is None:
            prev.next_node = NewNode

    def print_all(self):
        """Gets the string to print

        Returns:
            str: The string to print
        """

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        nodes = ""
        current = self.__head
        while current is not None:
            nodes += str(current.data)
            nodes += "\n" if current.next_node else ""
            current = current.next_node
        return nodes
