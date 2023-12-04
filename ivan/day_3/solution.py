# %%
import os
from collections import namedtuple
from string import punctuation
from typing import List

from dotenv import load_dotenv

import utils.input

# %% Load input
load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=3)
inp = inp.splitlines()
# %% ==PART_1==

Number = namedtuple("Number", ["line_number", "idxs", "number"])
numbers = []

Symbol = namedtuple("Symbol", ["line_number", "index", "symbol"])
symbols = []


for line_n, line in enumerate(inp, 1):
    idxs = []
    number = ""
    for idx, char in enumerate(line, 1):
        if char.isdigit():
            idxs.append(idx)
            number += char
        else:  # this is ugly
            if number and idxs:
                numbers.append(Number(line_n, idxs, number))
                number = ""
                idxs = []
        if char in punctuation.replace(".", ""):
            symbols.append(Symbol(line_n, idx, char))
    else:  # as well as this
        if number and idxs:
            numbers.append(Number(line_n, idxs, number))
            number = ""
            idxs = []


def find_part_numbers(symbols: List[Symbol], numbers: List[Number]):
    valid_numbers = []
    for s in symbols:
        for n in numbers:
            if (
                s.line_number == n.line_number - 1
                or s.line_number == n.line_number
                or s.line_number == n.line_number + 1
            ):
                if s.index - 1 in n.idxs or s.index in n.idxs or s.index + 1 in n.idxs:
                    valid_numbers.append(n)
    return valid_numbers


valid_numbers = find_part_numbers(symbols, numbers)

sum_of_part_numbers = sum([int(n.number) for n in valid_numbers])

print("Part 1: ", sum_of_part_numbers)

# %% ==PART_2==


def find_part_numbers(symbols: List[Symbol], numbers: List[Number]):
    valid_numbers = []
    for s in filter(lambda s: s.symbol == "*", symbols):
        adjacent_numbers = []
        for n in numbers:
            if (
                s.line_number == n.line_number - 1
                or s.line_number == n.line_number
                or s.line_number == n.line_number + 1
            ):
                if s.index - 1 in n.idxs or s.index in n.idxs or s.index + 1 in n.idxs:
                    adjacent_numbers.append(n)
        if len(adjacent_numbers) == 2:
            valid_numbers.append(adjacent_numbers)
    return valid_numbers


valid_numbers = find_part_numbers(symbols, numbers)

from math import prod

gear_ratios = [prod(int(n.number) for n in pair) for pair in valid_numbers]

print("Part 2: ", sum(gear_ratios))
