# %%
import os
from collections import namedtuple
from typing import List

from dotenv import load_dotenv

import utils.input

# %% Load input
load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=4)
inp = inp.splitlines()

# %% ==PART_1==

Card = namedtuple("Card", "id, copies")

cards = []

total_points = 0
for line in inp:
    card = line.split(": ")
    id = int(card[0].split()[1])
    numbers = card[1].split(" | ")
    winning_numbers = set(numbers[0].split())
    my_numbers = set(numbers[1].split())
    matching = winning_numbers & my_numbers
    total_points += 2 ** (len(matching) - 1) if matching else 0

    cards.append(Card(id, len(matching)))

print("Part 1: ", total_points)

# %% ==PART_2==


def calc_won_copies(deck: List[Card], cache={}):
    if deck == []:
        return 0

    copies = []
    for card in deck:
        if not card.copies:
            continue
        if card not in cache:
            won = deck[card.id : card.id + card.copies]
            cache[card] = won
        else:
            won = cache[card]
        copies.extend(won)
    return len(copies) + calc_won_copies(copies)


print("Part 2: ", calc_won_copies(cards) + len(cards))
