# %%
import os
from collections import namedtuple
from string import punctuation
from typing import List

from dotenv import load_dotenv

import utils.input

# %% Load input
load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=4)
inp = inp.splitlines()

# %% ==PART_1==
total_points = 0
for line in inp:
    card = line.split(": ")
    id = card[0].split()[1]
    numbers = card[1].split(" | ")
    winning_numbers = set(numbers[0].split())
    my_numbers = set(numbers[1].split())
    matching = winning_numbers & my_numbers
    total_points += 2 ** (len(matching) - 1) if matching else 0

print(total_points)


# %%
