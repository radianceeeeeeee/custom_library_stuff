class Grid:
    def __init__(self, rowCount, colCount, zeroIndex = True, emptyValue = 0):
        self.grid = [[emptyValue for c in range(colCount)] for r in range(rowCount)]
        self.row = rowCount
        self.col = colCount
        self.zeroIndex = zeroIndex
        self.emptyValue = emptyValue

    def change_elem(self, row, col, val):
        self.grid[row][col] = val

    def change_row(self, row, arr):
        if len(arr) > self.col:
            print("Array length is longer than required")
            return
        elif len(arr) < self.col:
            arr = arr + [self.emptyValue] * (self.col - len(arr))

        if not self.zeroIndex:
            row -= 1
        self.grid[row] = arr

    def change_col(self, col, arr):
        if len(arr) > self.row:
            print("Array length is longer than required")
            return
        elif len(arr) < self.row:
            arr = arr + [self.emptyValue] * (self.row - len(arr))

        if not self.zeroIndex:
            col -= 1

        for r in range(self.row):
            self.grid[r][col] = arr[r]

    def print_row(self, row):
        if not self.zeroIndex:
            row -= 1
        print(self.grid[row])

    def print_col(self, col):
        if not self.zeroIndex:
            col -= 1
        
        for r in range(self.row):
            print(self.grid[r][col])

    def print_grid(self):
        for row in self.grid:
            for val in row:
                print(val, end = "")
            print()

class Stack:
    def __init__(self, limit = 65535):
        self.limit = limit
        self.arr = [None] * self.limit
        self.index = 0

    def isEmpty(self):
        return self.index == 0

    def isFull(self):
        return self.index == self.limit

    def peek(self):
        if self.index == 0:
            return "There are no elements in the stack"

        return self.arr[self.index - 1]

    def push(self, value):
        if self.isFull():
            return "Stack overflow! Limit " + str(self.limit)  + " is reached."
        
        self.arr[self.index] = value
        self.index += 1

    def pop(self):
        if self.isEmpty():
            print("Stack underflow! There is no element in the stack.")
            return -1

        self.index -= 1
        return self.arr[self.index]

class Queue:
    def __init__(self, limit = 65535):
        self.limit = limit
        self.arr = [None] * (self.limit + 1)
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return self.front == (self.rear % self.limit) + 1

    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue."

        return self.arr[self.front]

    def enqueue(self, value):
        if self.isFull():
            print("The queue is full")
            return -1
            
        self.arr[self.rear] = value

        self.rear = self.rear + 1
        if self.rear > self.limit:
            self.rear = 0

    def dequeue(self):
        if self.isEmpty():
            print("There are no elements in the queue.")
            return -1

        front = self.arr[self.front]
        self.front = self.front + 1
        if self.front > self.limit:
            self.front = None

        return front

class SLLNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def change_value(self, newValue):
        self.value = newValue

    def show_value(self):
        return self.value

class SinglyLinkedList:
    def __init__(self):
        self.head = SLLNode("root")
        self.currentNode = self.head
        self.size = 0

    def insert(self, node, index = None):
        if index == None or index == self.size:
            self.currentNode.next = node
            self.currentNode = self.currentNode.next
            self.size += 1
            return 0

        if index > self.size:
            print("Index is greater than the length of the linked list. (Length is " + str(self.size) + ")")
            return -1

        i = 0
        currentNode = self.head
        while i < index:
            currentNode = currentNode.next
            i += 1

        node.next = currentNode.next
        currentNode.next = node
        
        self.size += 1
        return 0
                
    def remove_index(self, index = None):
        if index == None:
            index = self.size - 1

        if index > self.size:
            print("Index is greater than the length of the linked list. (" + str(self.size) + ")")
            return -1

        prevNode = self.head
        currentNode = prevNode.next

        while index != 0:
            prevNode = currentNode
            currentNode = currentNode.next
            index -= 1
        prevNode.next = currentNode.next

        self.size -= 1
        return 0

    def search_value(self, value):
        i = 0
        currentNode = self.head.next

        while currentNode != None:
            if currentNode.value == value:
                return i

            currentNode = currentNode.next
            i += 1

        print(value, "is not in the linked list.")
        return -1

    def print_SLL(self):
        currentNode = self.head.next
        while currentNode != None:
            print(currentNode.value, "->", end = " ")
            currentNode = currentNode.next
        print()

    def reverse_SLL(self):
        previousNode = None
        currentNode = self.head.next
        
        while currentNode != None:
            next = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = next

        self.head.next = previousNode

class DLLNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def change_value(self, newValue):
        self.value = newValue

    def show_value(self):
        return self.value

class DoublyLinkedList:
    def __init__(self):
        self.head = DLLNode("root")
        self.currentNode = self.head
        self.size = 0

    def insert(self, node, index = None):
        if index == None or index == self.size:
            node.prev = self.currentNode
            self.currentNode.next = node
            self.currentNode = self.currentNode.next
            self.size += 1
            return 0

        if index > self.size:
            print("Index is greater than the length of the linked list. (Length is " + str(self.size) + ")")
            return -1

        i = 0
        currentNode = self.head
        while i < index:
            currentNode = currentNode.next
            i += 1

        temp = currentNode.next

        currentNode.next = node
        node.prev = currentNode
        node.next = temp
        temp.prev = node
        
        self.size += 1
        return 0

    def remove_index(self, index = None):
        if index == None:
            index = self.size - 1

        if index > self.size:
            print("Index is greater than the length of the linked list. (" + str(self.size) + ")")
            return -1

        prevNode = self.head
        currentNode = prevNode.next

        while index != 0:
            prevNode = currentNode
            currentNode = currentNode.next
            index -= 1
        
        temp = currentNode.next
        prevNode.next = currentNode.next
        temp.prev = prevNode

        self.size -= 1
        return 0

    def search_value(self, value):
        i = 0
        currentNode = self.head.next

        while currentNode != None:
            if currentNode.value == value:
                return i

            currentNode = currentNode.next
            i += 1

        print(value, "is not in the linked list.")
        return -1

    def print_DLL(self, reverse = False):
        if not reverse:
            currentNode = self.head.next
            while currentNode != None:
                print(currentNode.value, "<->", end = " ")
                currentNode = currentNode.next
            print()
            return 0

        currentNode = self.currentNode
        while currentNode.prev != None:
            print(currentNode.value, "<->", end = " ")
            currentNode = currentNode.prev
        print()
        
class BTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def change_value(self, newValue):
        self.value = newValue

    def show_value(self, newValue):
        return self.value

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        print(self.root.value)
        self.print_tree_helper(self.root, 0, 0)

    def print_tree_helper(self, node, level, whitespace):
        if node.left != None:
            symbol = "|" if node.right != None else "+"
            print("   " * whitespace + symbol + "--" + str(node.left.value))
            self.print_tree_helper(node.left, level + 1, whitespace + 1)

        if node.right != None:
            print("   " * whitespace + "+--" + str(node.right.value))
            self.print_tree_helper(node.right, level + 1, whitespace + 1)       

class TreeNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.children = []

    def append(self, node):
        self.children.append(node)
        node.parent = self

    def isLeaf(self):
        if len(self.children):
            return False

        return True

class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        print(self.root.value)
        self.print_tree_helper(self.root, 0, 0)

    def print_tree_helper(self, node, level, whitespace):
        for c in range(len(node.children)):
            symbol = "|" if c < len(node.children) - 1 else "+"
            print("   " * whitespace + symbol + "--" + str(node.children[c].value))
            self.print_tree_helper(node.children[c], level + 1, whitespace + 1)

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, value):
        self.vertices.add(value)
    
    def add_edge(self, v1, v2, undirected = True):
        if v1 in self.edges.keys():
            self.edges[v1].add(v2)
        else:
            self.edges[v1] = {v2}

        if undirected:
            if v2 in self.edges.keys():
                self.edges[v2].add(v1)
            else:
                self.edges[v2] = {v1}            

    def show_neighbors(self, vertex):
        if vertex not in self.edges.keys():
            return set()
        return self.edges[vertex]

    def dfs(self, src, dst):
        s = Stack()
        s.push(src)

        visited = {v: False for v in self.vertices}

        while not s.isEmpty():
            currNode = s.pop()

            if currNode == dst:
                return True

            if not visited[currNode]:
                visited[currNode] = True
                for v in self.edges[currNode]:
                    s.push(v)

        return False

    def bfs(self, src, dst, pred = {}):
        q = Queue()
        q.enqueue(src)

        visited = {v: False for v in self.vertices}
        visited[src] = True

        while not q.isEmpty():
            currNode = q.dequeue()

            for v in self.edges[currNode]:
                if not visited[v]:
                    q.enqueue(v)
                    visited[v] = True
                    pred[v] = currNode

                    if v == dst:
                        return True

        return False

    def shortest_path_helper(self, src, dst):
        predecessors = {v: None for v in self.vertices}

        if not self.bfs(src, dst, predecessors):
            return -1

        path = []
        currNode = dst

        while currNode != src:
            currNode = predecessors[currNode]
            path.append(currNode)

        return path

    def shortest_path(self, src, dst):
        path = self.shortest_path_helper(src, dst)

        for n in path[::-1]:
            print(n, end = " -> ")

        print(dst)

    def shortest_path_length(self, src, dst):
        return len(self.shortest_path_helper(src, dst)) + 1

