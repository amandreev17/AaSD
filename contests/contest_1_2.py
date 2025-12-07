import sys


class Deque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = 0
        self.deque = [None] * capacity

    def pushb(self, add_el):
        if self.size == self.capacity:
            return "overflow"
        self.deque[(self.size + self.head) % self.capacity] = add_el
        self.size += 1

    def pushf(self, add_el):
        if self.size == self.capacity:
            return "overflow"
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.deque[self.head] = add_el
        self.size += 1

    def popb(self):
        if self.size == 0:
            return "underflow"
        tail_el = self.deque[(self.head + self.size - 1) % self.capacity]
        self.size -= 1
        return tail_el

    def popf(self):
        if self.size == 0:
            return "underflow"
        head_el = self.deque[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return head_el

    def print(self):
        if self.size == 0:
            print("empty")
        for i in range(self.size):
            if i < self.size - 1:
                print(self.deque[(self.head + i) % self.capacity], end=" ")
            else:
                print(self.deque[(self.head + i) % self.capacity])


deque = None
flag = 0
for line in sys.stdin:
    input_command = line.split(' ')
    if input_command[0] == '\n':
        continue
    command = input_command[0]
    len_input_command = len(input_command)
    if len_input_command > 2:
        print("error")
        continue

    if len_input_command == 1:
        if command[:-1] == "popf" and flag:
            print(deque.popf())
            continue
        if command[:-1] == "popb" and flag:
            print(deque.popb())
            continue
        if command[:-1] == "print" and flag:
            deque.print()
            continue
    if len_input_command == 2:
        number = input_command[1][:-1]
        if command == "set_size" and number.isdigit() and int(number) >= 0 and flag == 0:
            deque = Deque(int(number))
            flag = 1
            continue
        if command == "pushb" and flag:
            if deque.pushb(number) == "overflow":
                print("overflow")
            continue
        if command == "pushf" and flag:
            if deque.pushf(number) == "overflow":
                print("overflow")
            continue
    print("error")
