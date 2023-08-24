from typing import Dict

import requests
from loguru import logger


def get_pokemon(id_or_name: str | int) -> Dict[str, dict]:
    """Get a pokemon from the pokeapi.

    Args:
    ----
        id_or_name (str | int): The id or name of the pokemon.

    Returns:
    -------
        Dict[str, dict]: A dictionary containing the pokemon's information.
    """
    # Set the endpoint and make request
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{id_or_name!s}"
        response = requests.get(url=url, timeout=5)
        if response.status_code != 200:
            logger.error("Pokemon not found.")
            return {}
        logger.info("Successfully retrieved pokemon from pokeapi.")
        return response.json()
    except requests.exceptions.JSONDecodeError:
        logger.error("Pokemon not found.")
        return {}
