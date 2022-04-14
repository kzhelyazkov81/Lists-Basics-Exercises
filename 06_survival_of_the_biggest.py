numbers = input().split(' ')
count = int(input())

copy_numbers = list(map(int, numbers))

for i in range(count):
    min_number = min(copy_numbers)
    copy_numbers.remove(min_number)

numbers = list(map(str, copy_numbers))
print(', '.join(numbers))
