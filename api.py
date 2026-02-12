# api.py

import requests


BASE_URL = "https://wordle.votee.dev:8000"


def guess_random(guess: str, seed: int = None, size: int = 5):
    """
    Send a guess to /random endpoint
    """
    url = f"{BASE_URL}/random"
    params = {
        "guess": guess,
        "size": size
    }

    if seed is not None:
        params["seed"] = seed

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}, {response.text}")

    return response.json()
