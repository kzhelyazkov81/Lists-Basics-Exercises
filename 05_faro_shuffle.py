cards = input()
shuffles = int(input())

deck = cards.split(' ')
deck_a = []
deck_b = []

for i in range(shuffles):
    deck_a = deck[0:(len(deck)//2)]
    deck_b = deck[(len(deck)//2)::]
    deck.clear()
    for j in range(len(deck_a)):
        deck.append(deck_a[j])
        deck.append(deck_b[j])

print(deck)
