import os

from dotenv import load_dotenv

import utils.input

load_dotenv()

i = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=1)
