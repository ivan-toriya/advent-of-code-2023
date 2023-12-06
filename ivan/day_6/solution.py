# %% Load input
import os

from dotenv import load_dotenv

import utils.input

load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=6)
inp = inp.splitlines()
# inp

# %%

# test_inp = """Time:      7  15   30
# Distance:  9  40  200
# """
# inp = test_inp.splitlines()

# %% ==Part 1==
times = [int(num) for num in inp[0].split(":")[1].split()]
distances = [int(num) for num in inp[1].split(":")[1].split()]


def calc_ways_to_beat(time: int, distance: int):
    ways = 0
    for t in range(0, time + 1):
        speed = t
        if speed * (time - t) > distance:
            ways += 1
    return ways


from math import prod

mul = prod([calc_ways_to_beat(t, d) for t, d in zip(times, distances)])
print(mul)

# %% ==Part 2==
times = [num for num in inp[0].split(":")[1].split()]
time = "".join(times)

distances = [num for num in inp[1].split(":")[1].split()]
distance = "".join(distances)

ways = calc_ways_to_beat(int(time), int(distance))
print(ways)
