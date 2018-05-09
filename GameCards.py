import random

# make the deck
deck = list(range(1, 14))
NUM_TO_DRAW = 6

pickedCards = []
while len(pickedCards) < NUM_TO_DRAW:
    cardToAdd = random.randint(1, len(deck))
    try:
        deck.remove(cardToAdd)
    except ValueError as e:
        pass
    else:
        pickedCards.append(cardToAdd)

print(pickedCards)
