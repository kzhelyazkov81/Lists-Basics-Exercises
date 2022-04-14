gifts = input().split(' ')

command = input()

while command != 'No Money':
    command = command.split(' ')
    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'
    elif command[0] == 'Required':
        if int(command[2]) in range(len(gifts)):
            gifts[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    command = input()

for i in range(len(gifts)-1, -1, -1):
    if gifts[i] == 'None':
        gifts.remove('None')

print(' '.join(gifts))
