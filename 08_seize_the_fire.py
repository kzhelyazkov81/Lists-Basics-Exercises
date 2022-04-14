fires = input().split('#')
water = int(input())
effort = 0
valid = False
cells = []
total_fire = 0

for i in range(len(fires)):
    valid = False
    current_fire = fires[i]
    fire_info = current_fire.split(' = ')
    fire_level = fire_info[0]
    fire_value = int(fire_info[1])
    if fire_level == 'High' and 81 <= fire_value <= 125:
        valid = True
    elif fire_level == 'Medium' and 51 <= fire_value <= 80:
        valid = True
    elif fire_level == 'Low' and 1 <= fire_value <= 50:
        valid = True
    if valid and water >= fire_value:
        water -= fire_value
        effort += 0.25*fire_value
        cells.append(fire_value)
        total_fire += fire_value

print('Cells:')
for i in range(len(cells)):
    print(f' - {cells[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
