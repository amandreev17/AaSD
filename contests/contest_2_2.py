import sys
from collections import deque


class Node:
    def __init__(self, key: int, value: str, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class SplayTree:
    def __init__(self):
        self.__root = None

    def left_rotate(self, node_x: Node):
        node_y = node_x.right
        node_x.right = node_y.left
        if node_y.left:
            node_y.left.parent = node_x
        node_y.parent = node_x.parent
        if node_x.parent is None:
            self.__root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y
        node_y.left = node_x
        node_x.parent = node_y
        return

    def right_rotate(self, node_x: Node):
        node_y = node_x.left
        node_x.left = node_y.right
        if node_y.right:
            node_y.right.parent = node_x
        node_y.parent = node_x.parent
        if node_x.parent is None:
            self.__root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y
        node_y.right = node_x
        node_x.parent = node_y
        return

    def splay(self, node: Node):
        while node.parent is not None:
            if node.parent.right == node:
                if node.parent.parent is None:
                    self.left_rotate(node.parent)
                elif node.parent == node.parent.parent.right:
                    self.left_rotate(node.parent.parent)
                    self.left_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)
                    self.right_rotate(node.parent)
            else:
                if node.parent.parent is None:
                    self.right_rotate(node.parent)
                elif node.parent == node.parent.parent.left:
                    self.right_rotate(node.parent.parent)
                    self.right_rotate(node.parent)
                else:
                    self.right_rotate(node.parent)
                    self.left_rotate(node.parent)
        return

    def find(self, key):
        if self.__root is None:
            return None
        prev, current = None, self.__root
        while current:
            prev = current
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return prev

    def add(self, key, value):
        node = self.find(key)
        if node and node.key == key:
            self.splay(node)
            return False
        prev = None
        node_x = self.__root
        new_node = Node(key, value)
        while node_x:
            prev = node_x
            if key < node_x.key:
                node_x = node_x.left
            else:
                node_x = node_x.right
        new_node.parent = prev
        if prev is None:
            self.__root = new_node
        elif key < prev.key:
            prev.left = new_node
        else:
            prev.right = new_node
        self.splay(new_node)
        return True

    def print(self):
        if self.__root is None:
            print("_")
            return
        nodes = deque()
        print(f'[{self.__root.key} {self.__root.value}]')
        if self.__root.left is not None:
            nodes.append([self.__root.left, 0])
        if self.__root.right is not None:
            nodes.append([self.__root.right, 1])
        nums_of_nodes = len(nodes)
        if nums_of_nodes == 0: return
        height = self.height(self.__root)
        current = nodes[0][1]
        for level in range(1, height):
            current_position = 0
            width_level = 2 ** level
            while nums_of_nodes > 0:
                if current_position == current:
                    nums_of_nodes -= 1
                    node = nodes.popleft()[0]
                    if node.left is not None:
                        nodes.append([node.left, 2 * (current + 1) - 2])
                    if node.right is not None:
                        nodes.append([node.right, 2 * (current + 1) - 1])
                    if current != width_level - 1:
                        print(f'[{node.key} {node.value} {node.parent.key}] ', end='')
                    else:
                        print(f'[{node.key} {node.value} {node.parent.key}]', end='')
                    current_position = current + 1
                    if len(nodes) != 0:
                        current = nodes[0][1]
                elif current - current_position != 0:
                    print('_ ' * (current - current_position), end='')
                    current_position = current
                if nums_of_nodes == 0:
                    print('_ ' * (width_level - current_position - 1), end='')
                    if current_position != width_level:
                        print('_', end=' ')
            nums_of_nodes = len(nodes)
            print()

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def search(self, key):
        if self.__root is None:
            return False, None
        node = self.find(key)
        if node is None or node.key != key:
            if node:
                self.splay(node)
                return False, None
        self.splay(node)
        return True, node

    def max(self):
        current = self.__root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        self.splay(current)
        return current

    def min(self):
        current = self.__root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        self.splay(current)
        return current

    def delete(self, key):
        delete_node = self.find(key)
        if delete_node is None:
            return False
        self.splay(delete_node)
        if delete_node.key != key:
            return False
        if delete_node.left is None:
            self.__root = delete_node.right
            if self.__root:
                self.__root.parent = None
            return True
        if delete_node.right is None:
            self.__root = delete_node.left
            if self.__root:
                self.__root.parent = None
            return True
        delete_node.left.parent = None
        new_root = delete_node.left
        while new_root.right:
            new_root = new_root.right
        self.splay(new_root)
        if delete_node.right is not None:
            new_root.right = delete_node.right
            delete_node.right.parent = new_root
        self.__root = new_root
        return True

    def set(self, key, value):
        node = self.find(key)
        if node is None or node.key != key:
            if node:
                self.splay(node)
                return False
        node.value = value
        self.splay(node)
        return True


tree = SplayTree()
for line in sys.stdin:
    input_command = line.strip().split(' ')
    command = input_command[0]
    try:
        if command == '':
            continue
        elif command == "max":
            node = tree.max()
            if node is None:
                raise ValueError("error")
            print(node.key, node.value)
        elif command == "min":
            node = tree.min()
            if node is None:
                raise ValueError("error")
            print(node.key, node.value)
        elif command == "print":
            tree.print()
        elif command == "add":
            if len(input_command) == 2:
                key = int(input_command[1])
                value = ""
            elif len(input_command) == 3:
                key = int(input_command[1])
                value = input_command[2]
            else:
                raise ValueError("error")
            if not(tree.add(key, value)):
                raise ValueError("error")
        elif command == "delete":
            if len(input_command) != 2:
                raise ValueError("error")
            key = int(input_command[1])
            if not(tree.delete(key)):
                raise ValueError("error")
        elif command == "search":
            if len(input_command) != 2:
                raise ValueError("error")
            key = int(input_command[1])
            bool_search, node = tree.search(key)
            if bool_search:
                print(f"1 {node.value}")
            else:
                print("0")
        elif command == "set":
            if len(input_command) == 2:
                key = int(input_command[1])
                value = ""
            elif len(input_command) == 3:
                key = int(input_command[1])
                value = input_command[2]
            else:
                raise ValueError("error")
            if not(tree.set(key, value)):
                raise ValueError("error")
        else:
            raise ValueError("error")
    except Exception:
        print("error")
