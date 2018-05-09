import random

# make the deck
deck = list(range(1, 14))

# the amount of cards to draw
NUM_TO_DRAW = 6

# a list of all the cards to remove from the deck
pickedCards = []

# repeat forever until we have enough cards
while len(pickedCards) < NUM_TO_DRAW:
    # pick a card to remove from the deck
    cardToAdd = random.randint(1, len(deck))

    # catch errors when trying to remove a card that already exists in the deck
    try:
        deck.remove(cardToAdd)
    except ValueError as e:
        pass
    else:
        # add the card to our picked selectoin
        pickedCards.append(cardToAdd)

print("Picked these cards: ", pickedCards)
print("Lowest card: ", min(pickedCards))
