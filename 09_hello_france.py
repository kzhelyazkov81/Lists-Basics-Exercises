items = input().split('|')
budget = int(input())
lower = False
income = 0
profit = 0
bought_items = []


for item in items:
    lower = False
    item_info = item.split('->')
    item_type = item_info[0]
    item_price = float(item_info[1])
    if item_type == 'Clothes' and item_price <= 50:
        lower = True
    if item_type == 'Shoes' and item_price <= 35:
        lower = True
    if item_type == 'Accessories' and item_price <= 20.5:
        lower = True
    if lower and budget >= item_price:
        budget -= item_price
        item_new_price = 1.4 * item_price
        income += item_new_price
        profit += 0.4*item_price
        bought_items.append(f'{item_new_price:.2f}')

budget += income
print(' '.join(bought_items))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print('Not enough money.')
