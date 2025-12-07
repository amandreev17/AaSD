import sys
import copy


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Heap:
    def __init__(self):
        self.__array = []
        self.__dict = {}

    def heapify_down(self, index: int):
        left = 2 * index + 1
        right = 2 * index + 2
        heap_size = len(self.__array)
        if left < heap_size and self.__array[left].key < self.__array[index].key:
            minimum = left
        else:
            minimum = index
        if right < heap_size and self.__array[right].key < self.__array[minimum].key:
            minimum = right
        if minimum != index:
            self.__array[index], self.__array[minimum] = self.__array[minimum], self.__array[index]
            self.__dict[self.__array[index].key] = index
            self.__dict[self.__array[minimum].key] = minimum
            self.heapify_down(minimum)
        return

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and (self.__array[parent].key > self.__array[index].key):
            self.__array[index], self.__array[parent] = self.__array[parent], self.__array[index]
            self.__dict[self.__array[index].key] = index
            self.__dict[self.__array[parent].key] = parent
            index = parent
            parent = (index - 1) // 2
        return

    def add(self, key, value):
        try:
            return self.__dict[key]
        except:
            heap_size = len(self.__array)
            node = Node(key, value)
            self.__array.append(node)
            self.__dict[key] = heap_size
            self.heapify_up(heap_size)
        return

    def print(self):
        heap_size = len(self.__array)
        if heap_size == 0:
            print("_")
            return
        print(f'[{self.__array[0].key} {self.__array[0].value}]')
        width_level = 2
        count = 0
        for i in range(1, heap_size):
            print(f'[{self.__array[i].key} {self.__array[i].value} {self.__array[(i - 1) // 2].key}] ', end='')
            count += 1
            if count == width_level:
                count = 0
                width_level *= 2
                print()
            if i == heap_size - 1 and count != 0:
                print("_ " * (width_level - count - 1), end='')
                print("_")
        return

    def set(self, key, value):
        check = self.__dict[key]
        self.__array[self.__dict[key]].value = value
        return

    def extract(self):
        heap_size = len(self.__array)
        if heap_size == 0:
            return None
        else:
            extract_el = copy.deepcopy(self.__array[0])
            self.__array[0] = self.__array.pop(heap_size - 1)
            self.__dict[self.__array[0].key] = 0
            self.__dict.pop(extract_el.key, None)
            self.heapify_down(0)
            return extract_el

    def delete(self, key):
        check = self.__dict[key]
        heap_size = len(self.__array)
        if heap_size == 1:
            self.__array.clear()
            self.__dict.clear()
            return
        new_el = self.__array[heap_size - 1]
        if new_el.key == key:
            self.__array.pop(heap_size - 1)
            self.__dict.pop(new_el.key, None)
            return
        extract_el = copy.deepcopy(self.__array[self.__dict[key]])
        self.__array[self.__dict[key]] = self.__array.pop(heap_size - 1)
        self.__dict[self.__array[self.__dict[key]].key] = self.__dict[key]
        self.__dict.pop(extract_el.key, None)
        self.heapify_down(self.__dict[new_el.key])
        self.heapify_up(self.__dict[new_el.key])

    def min(self):
        heap_size = len(self.__array)
        if heap_size == 0:
            return None
        else:
            return self.__array[0]

    def max(self):
        heap_size = len(self.__array)
        if heap_size == 0:
            return None, None
        else:
            last_el = heap_size - 1
            node_max = last_el
            while last_el >= heap_size // 2:
                if self.__array[last_el].key > self.__array[node_max].key:
                    node_max = last_el
                last_el -= 1
        return self.__array[node_max], node_max

    def search(self, key):
        try:
            check = self.__dict[key]
            return self.__array[check], check
        except:
            return None, None


heap = Heap()
for line in sys.stdin:
    input_command = line.strip().split(' ')
    command = input_command[0]
    try:
        if command == '':
            continue
        elif command == "max":
            node, index = heap.max()
            if node is None:
                raise ValueError("error")
            print(f'{node.key} {index} {node.value}')
        elif command == "min":
            node = heap.min()
            if node is None:
                raise ValueError("error")
            print(f'{node.key} {0} {node.value}')
        elif command == "print":
            heap.print()
        elif command == "add":
            if len(input_command) == 2:
                key = int(input_command[1])
                value = ""
            elif len(input_command) == 3:
                key = int(input_command[1])
                value = input_command[2]
            else:
                raise ValueError("error")
            if heap.add(key, value):
                raise ValueError("error")
        elif command == "delete":
            if len(input_command) != 2:
                raise ValueError("error")
            key = int(input_command[1])
            heap.delete(key)
        elif command == "search":
            if len(input_command) != 2:
                raise ValueError("error")
            key = int(input_command[1])
            el, index = heap.search(key)
            if el:
                print(f"1 {index} {el.value}")
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
            heap.set(key, value)
        elif command == "extract":
            node = heap.extract()
            if node:
                print(f'{node.key} {node.value}')
            else:
                raise ValueError("error")
        else:
            raise ValueError("error")
    except Exception:
        print("error")
