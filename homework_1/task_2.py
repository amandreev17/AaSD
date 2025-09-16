 n = int(input())
 numbers = [1]
 pow_2 = 0
 pow_3 = 0
 pow_5 = 0
 while len(numbers) < n:
     next_number_1 = numbers[pow_2] * 2
     next_number_2 = numbers[pow_3] * 3
     next_number_3 = numbers[pow_5] * 5
     next_number = min(next_number_1, next_number_2, next_number_3)
     numbers.append(next_number)
     if next_number == next_number_1:
         pow_2 += 1
     if next_number == next_number_2:
         pow_3 += 1
     if next_number == next_number_3:
         pow_5 += 1
     print(next_number)
