import pygame

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

class Snake:
    # Snake() produces a Snake with only the head
    # __init__: None -> Snake
    def __init__(self, x, y):
        self.head = Node(x, y)
        self.tail = Node(x, y)
        self.length = 1
        self.color = (0, 0, 255)
    
    # make_new(self,data) consumes data and produces nothing
    # but adding a new node to the end of the list
    # make_new: Any -> None
    # need to make sure the number of x and y connects
    def grow(self, direction):
        if direction == "up":
            x = self.tail.x
            y = self.tail.y + 20
        elif direction == "down":
            x = self.tail.x
            y = self.tail.y - 20
        elif direction == "left":
            x = self.tail.x + 20
            y = self.tail.y
        elif direction == "right":
            x = self.tail.x - 20
            y = self.tail.y 

        new_body = Node(x, y)
        self.tail.next = new_body
        self.tail = self.tail.next
        self.length += 1

    # move(self, x, y) moves the snake by x and y
    def move(self, x, y):
        curr = self.head
        for i in range(self.length):
            curr.x += x
            curr.y += y
            if curr.next == None:
                self.tail = curr
            curr = curr.next

    # visualize(self) consumes a Snake, and returns a string for human to read and debug
    def visualize (self):
        curr = self.head
        st = ""
        for i in range(self.length):
            st += "[" + str(curr.x) + "," + str(curr.y) + "]" + "->"
            curr = curr.next
        return st