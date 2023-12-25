Cards = open('day_4\day4_Input.txt').read().split('\n')
Cards_worth = 0
for card in Cards:
    card = card[8:].split(" | ")
    winning = card[0].split()
    numbers = card[1].split()

    count = sum(1 for n in numbers if n in winning)
    if count>0:
        Cards_worth += 2**(count-1)

print(Cards_worth)