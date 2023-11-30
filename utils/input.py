import requests


def get(session_cookie: str, year: int, day: int) -> requests.Response.text:
    """Gets the input for a given year and day from the Advent of Code website.

    Args:
        session_cookie (str): Your Advent of Code session cookie.
        year (int): The year of the puzzle. Format: YYYY
        day (int): The day of the puzzle. Format: DD
    """
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session_cookie})
    return response.text
