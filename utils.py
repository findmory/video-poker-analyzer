from models import GameConfig
from data import GAMES


def get_game(game_name: str) -> GameConfig:
    """
    Retrieve game configuration by name.

    Args:
        game_name: Name of the game to retrieve

    Returns:
        GameConfig with payouts and probabilities

    Raises:
        KeyError: If game_name doesn't exist
    """
    return GAMES[game_name]


def validate_game_config(game_config: GameConfig) -> bool:
    """
    Validate that a game configuration is valid.

    Args:
        game_config: GameConfig to validate

    Returns:
        bool: True if valid, False otherwise
    """
    # Check if probabilities sum to approximately 1
    prob_sum = sum(game_config.probabilities)
    if not (0.99999 <= prob_sum <= 1.00001):
        return False

    # Check if payouts and probabilities have matching lengths
    if len(game_config.payouts) != len(game_config.probabilities):
        return False

    return True
