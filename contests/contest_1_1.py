import sys
import re


def binary_find(list_numbers: [int], search_number: int, left, right) -> int:
    if left > right:
        return -1
    middle = (right + left) // 2
    if search_number == list_numbers[middle]:
        if middle > left and list_numbers[middle - 1] == search_number:
            return binary_find(list_numbers, search_number, left, middle - 1)
        else:
            return middle
    elif list_numbers[middle] < search_number:
        return binary_find(list_numbers, search_number, middle + 1, right)
    else:
        return binary_find(list_numbers, search_number, left, middle - 1)


numbers = [int(i) for i in re.findall(r'-?\d+', sys.stdin.readline())]
for line in sys.stdin:
    search = int(re.findall(r'-?\d+', line)[0])
    print(binary_find(numbers, search, 0, len(numbers) - 1))
