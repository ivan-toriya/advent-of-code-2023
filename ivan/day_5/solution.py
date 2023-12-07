# %% Load input
import os

from dotenv import load_dotenv

import utils.input

load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=5)
# inp = inp.splitlines()
# inp

# %%

seeds = tuple([int(num) for num in inp.split("\n\n")[0].split(":")[1].split()])

# %%
# import pprint

almanac = {}
for n, line in enumerate(inp.split("\n\n")[1:]):
    name_values = line.split(":")
    almanac[n] = {}
    almanac[n]["values"] = [tuple([int(num) for num in v.split()]) for v in name_values[1].splitlines() if v]
    almanac[n]["source"] = name_values[0].split("-")[0]
    almanac[n]["destination"] = name_values[0].split("-")[2].split()[0]

# pprint.pprint(almanac)
# %%

# seed = seeds[0]


def get_location_for_seed(seed: int, source: str):
    # print("seed: ", seed)

    if source == "location":
        # print("Seed location: ", seed)
        return seed

    a_map = []
    for k, v in almanac.items():
        if v["source"] == source:
            a_map.extend(v["values"])
            destination = v["destination"]
            # print("source: ", source, "destination: ", destination)

    for dest_r, source_r, length in a_map:
        # print(dest_r, source_r, length)
        # ranges = zip(range(source_r, source_r + length), range(dest_r, dest_r + length))
        if seed >= source_r and seed < source_r + length - 1:
            # print("seed in range", dest_r, source_r, length)
            next_dest_id = dest_r + seed - source_r
            break
        else:
            next_dest_id = seed
            # print("seed not in range")

    return get_location_for_seed(next_dest_id, destination)


# get_location_for_seed(seed, "seed")

closest_location = min([get_location_for_seed(seed, "seed") for seed in seeds])

print("Part 1: ", closest_location)
# %%

#

# seeds = [int(num) for num in inp.split("\n\n")[0].split(":")[1].split()]

# seed_ranges = zip(seeds[::2], seeds[1::2])

# locations = set()

# for start, finish in seed_ranges:
#     for seed in range(start, start + finish - 1):
#         locations.add(get_location_for_seed(seed, "seed"))

# print("Part 2: ", min(locations))
