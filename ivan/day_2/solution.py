# %%
import os

from dotenv import load_dotenv

import utils.input

# %% Load input
load_dotenv()

inp: str = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=2)
inp = inp.splitlines()

# %% ==PART_1==

bag_contents = {
    "r": 12,
    "g": 13,
    "b": 14,
}

# {
#   game_id: {
#       possible: True,
#       sets: {
#           set_n: {r: n, g: n, b: n},
#           set_n: {r: n, g: n, b: n}
#       }
#     },
#   game_id: {
#       possible: False,
#       sets: {
#           set_n: {r: n, g: n, b: n},
#           set_n: {r: n, g: n, b: n}
#       }
#     },
# }
games = {}
for line in inp:
    game = line.split(": ")
    id = int(game[0].split("Game ")[1])
    games[id] = {}
    sets = game[1].split("; ")
    games[id]["sets"] = {}

    for set_n, set in enumerate(sets):
        cubes = set.split(", ")
        games[id]["sets"][set_n] = {}

        for cube in cubes:
            cube = cube.split()
            amount = int(cube[0])
            color = cube[1][0]
            games[id]["sets"][set_n][color] = amount

            if games[id].get("possible") == False:
                continue
            elif bag_contents[color] < amount:
                games[id]["possible"] = False
            else:
                games[id]["possible"] = True

ids_sum = sum([game_id for game_id, game in games.items() if game["possible"]])

print(ids_sum)

# %% ==PART_2==

from math import prod

# {
#     game_id: {
#         "r": n,
#         "g": n,
#         "b": n,
#     }
# }

games = {}
for line in inp:
    game = line.split(": ")
    id = int(game[0].split("Game ")[1])
    games[id] = {}
    sets = game[1].split("; ")
    for set in sets:
        cubes = set.split(", ")
        for cube in cubes:
            cube = cube.split()
            amount = int(cube[0])
            color = cube[1][0]
            if games[id].get(color):
                if games[id][color] < amount:
                    games[id][color] = amount
            else:
                games[id][color] = amount


powers = [prod(colors.values()) for colors in games.values()]
total_sum = sum(powers)

print(total_sum)
