cards = input().split(' ')
a_players = 11
b_players = 11
cards_received = []
terminated = False

for card in cards:
    if card not in cards_received:
        cards_received.append(card)
        card.split('-')
        if card[0] == 'A':
            a_players -= 1
        elif card[0] == 'B':
            b_players -= 1
        if a_players < 7 or b_players < 7:
            terminated = True
            break

print(f'Team A - {a_players}; Team B - {b_players}')
if terminated:
    print('Game was terminated')
