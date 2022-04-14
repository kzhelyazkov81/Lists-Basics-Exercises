events = input().split('|')
current_energy = 100
coins = 100
day_completed = True

for event in events:
    event = event.split('-')
    event_type = event[0]
    event_value = int(event[1])
    if event_type == 'rest':
        if (current_energy + event_value) > 100:
            gained_energy = 100 - current_energy
            current_energy = 100
        else:
            current_energy += event_value
            gained_energy = event_value
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')
    elif event_type == 'order':
        if current_energy >= 30:
            current_energy -= 30
            coins += event_value
            print(f'You earned {event_value} coins.')
        else:
            current_energy += 50
            if current_energy > 100:
                current_energy = 100
            print('You had to rest!')
    else:
        if event_value <= coins:
            coins -= event_value
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            day_completed = False
            break

if day_completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {current_energy}')
