import sys


class Node:
    def __init__(self, key: int, value, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BinaryTreeSearch:
    def __init__(self):
        self.__root = None

    def add(self, key, value):
        prev_node = None
        node = self.__root
        while node is not None:
            prev_node = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return False
        new_node = Node(key, value, prev_node)
        if prev_node is None:
            self.__root = new_node
            return True
        elif key < prev_node.key:
            prev_node.left = new_node
            return True
        else:
            prev_node.right = new_node
            return True

    def set(self, key, value):
        node = self.search(key)
        if node is not None:
            node.value = value
            return True
        return False

    def search(self, key):
        current_node = self.__root
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return current_node
        return current_node

    def delete(self, key: int):
        node = self.search(key)
        if node is not None:
            self.__delete_recursion(node)
            return True
        return False

    def __delete_recursion(self, root):
        if root.left is None and root.right is None:
            self.__change(root, None)
        elif root.left is None:
            self.__change(root, root.right)
        elif root.right is None:
            self.__change(root, root.left)
        else:
            max_left = self.__find_max(root.left)
            root.key = max_left.key
            root.value = max_left.value
            self.__delete_recursion(max_left)

    def __change(self, node, child):
        if node.parent:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        if child:
            child.parent = node.parent
        if node == self.__root:
            self.__root = child

    def __find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current

    def min(self):
        current = self.__root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current

    def max(self):
        current = self.__root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current

    def print(self):
        if self.__root is None:
            print("_")
            return
        result = []
        current_level = [self.__root]
        while any(x is not None for x in current_level):
            result.append(current_level)
            next_level = []
            for node in current_level:
                if node is not None:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.append(None)
                    next_level.append(None)
            current_level = next_level
        for level in result:
            for node in level:
                if node is not None:
                    if node.parent is not None:
                        print(f"[{node.key} {node.value} {node.parent.key}]", end=' ')
                    else:
                        print(f"[{node.key} {node.value}]", end='')
                else:
                    print("_", end=' ')
            print()
        return


tree = BinaryTreeSearch()
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
            key = int(input_command[1])
            value = input_command[2]
            if not(tree.add(key, value)):
                raise ValueError("error")
        elif command == "delete":
            key = int(input_command[1])
            if not(tree.delete(key)):
                raise ValueError("error")
        elif command == "search":
            key = int(input_command[1])
            node = tree.search(key)
            if node is not None:
                print(f"1 {node.value}")
            else:
                print("0")
        elif command == "set":
            key = int(input_command[1])
            value = input_command[2]
            if not(tree.set(key, value)):
                raise ValueError("error")
        else:
            raise ValueError("error")
    except Exception:
        print("error")
