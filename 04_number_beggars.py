strings = input()
count_of_beggars = int(input())

list_integers = strings.split(', ')
earns = []

for i in range(count_of_beggars):
    earns.append(int(0))

while list_integers:
    for i in range(count_of_beggars):
        earns[i] += int(list_integers[0])
        list_integers.remove(list_integers[0])
        if not list_integers:
            break

print(earns)
