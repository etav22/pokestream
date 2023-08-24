import unittest
from unittest.mock import Mock, patch

from pokestream.core import get_pokemon


class TestGetPokemon(unittest.TestCase):
    @patch("pokestream.core.requests.get")
    def test_valid_id(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"name": "pikachu", "id": 25}
        mock_get.return_value = mock_response

        result = get_pokemon(25)

        assert result["name"] == "pikachu"
        assert result["id"] == 25
        mock_get.assert_called_once_with(url="https://pokeapi.co/api/v2/pokemon/25", timeout=5)

    @patch("pokestream.core.requests.get")
    def test_valid_name(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"name": "bulbasaur", "id": 1}
        mock_get.return_value = mock_response

        result = get_pokemon("bulbasaur")

        assert result["name"] == "bulbasaur"
        assert result["id"] == 1
        mock_get.assert_called_once_with(url="https://pokeapi.co/api/v2/pokemon/bulbasaur", timeout=5)

    @patch("pokestream.core.requests.get")
    def test_invalid_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_pokemon(1000)

        assert result == {}
        mock_get.assert_called_once()
