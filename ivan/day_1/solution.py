# %%
import os
from string import ascii_letters

from dotenv import load_dotenv

import utils.input

# %% Load input
load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=1)
inp = inp.splitlines()
# %% ==PART_1==

numbers = []
for l in inp:
    l = l.strip(ascii_letters)
    numbers.append(int(l[0] + l[-1]))

print(sum(numbers))

# %% ==PART_2==

spelled_numbers = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]


def find_all(subs: str, a_str: str):
    found_idxs = []
    start = 0
    while True:
        idx = a_str.find(subs, start)
        if idx == -1:
            return found_idxs
        found_idxs.append(idx)
        start = idx + 1


calibration_values = []

for l in inp:
    numbers = []
    for n in spelled_numbers:
        for i in find_all(n[0], l):
            numbers.append((i, n[1]))
        for i in find_all(str(n[1]), l):
            numbers.append((i, n[1]))

    numbers.sort(key=lambda x: x[0])

    calibration_values.append(int(f"{numbers[0][1]}{numbers[-1][1]}"))

print(sum(calibration_values))
