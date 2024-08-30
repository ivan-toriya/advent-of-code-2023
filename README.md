# advent-of-code-2023

## How to get input programmatically

1. Install local utils package into your .venv 

```sh
pip install -e path/to/workdir  # where setup.py is located
```

2. Import the package and use the `get` function

```python
import os
import utils.input

my_input = utils.input.get(session_cookie=os.environ["SESSION_COOKIE"], year=2023, day=1)
```

> **_NOTE:_** You can find your session cookie by logging into the advent of code website and inspecting the page (F12) Application -> Cookies.
