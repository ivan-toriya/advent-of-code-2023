# %% Load input
import os
from collections import Counter, namedtuple
from enum import Enum

from dotenv import load_dotenv

import utils.input

load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=7)
inp = inp.splitlines()

Hand = namedtuple("Hand", "cards counter bid")

hands = [Hand(hand_bid.split()[0], Counter(hand_bid.split()[0]), int(hand_bid.split()[1])) for hand_bid in inp]

# %% Part 1

strength = Enum("strength", "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2", start=1)


def custom_sort(hand: Hand):
    def define_type_rank():
        cases = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
        card_type = sorted(hand.counter.values(), reverse=True)

        return cases.index(card_type) + 1

    cards_strengths = tuple(strength[card].value for card in hand.cards)

    return define_type_rank(), *cards_strengths


total_winnings = 0
for rank, hand in enumerate(sorted(hands, key=custom_sort, reverse=True), start=1):
    total_winnings += rank * hand.bid

print("Part 1: ", total_winnings)


# %% Part 2

strength = Enum("strength", "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J", start=1)


def custom_sort_2(hand: Hand):
    def define_type_rank():
        cases = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
        card_type = sorted(hand.counter.values(), reverse=True)

        if hand.counter["J"] and hand.counter["J"] != 5:
            num_jokers = hand.counter["J"]
            del hand.counter["J"]
            most_common = hand.counter.most_common()[0][0]
            hand.counter[most_common] += num_jokers
            card_type = sorted(hand.counter.values(), reverse=True)

        return cases.index(card_type)

    cards_strengths = tuple(strength[card].value for card in hand.cards)

    return define_type_rank(), *cards_strengths


sorted_hands = sorted(hands, key=custom_sort_2, reverse=True)

total_winnings = 0
for rank, hand in enumerate(sorted_hands, start=1):
    total_winnings += rank * hand.bid

print("Part 2: ", total_winnings)
