from typing import Dict
from models import GameConfig

GAMES: Dict[str, GameConfig] = {
    "9/6_JOB": GameConfig(
        payouts=[800, 50, 25, 9, 6, 4, 3, 2, 1, 0],
        probabilities=[
            0.00002476,
            0.00010931,
            0.00236255,
            0.01151221,
            0.01101451,
            0.01122937,
            0.07444870,
            0.12927890,
            0.21458503,
            0.54543467,
        ],
    ),
    "8/5_JOB": GameConfig(
        payouts=[800, 50, 25, 8, 5, 4, 3, 2, 1, 0],
        probabilities=[
            0.00002489,
            0.00010766,
            0.00236289,
            0.01151368,
            0.01090156,
            0.01123512,
            0.07446275,
            0.12929841,
            0.21507064,
            0.54502239,
        ],
    ),
    "7/5_JOB": GameConfig(
        payouts=[800, 50, 25, 7, 5, 4, 3, 2, 1, 0],
        probabilities=[
            0.00002489,
            0.00010766,
            0.00236289,
            0.01151368,
            0.01090156,
            0.01123512,
            0.07446275,
            0.12929841,
            0.21507064,
            0.54502239,
        ],
    ),
    "baccarrat_player_8deck": GameConfig(
        payouts=[0, 2, 1],  # [lose, win, tie]
        probabilities=[
            0.458597,
            0.446247,
            0.095156,
        ],
    ),
    "baccarrat_banker_8deck": GameConfig(
        payouts=[1.95, 0, 1],  # [win, lose, tie]
        probabilities=[
            0.458597,
            0.446247,
            0.095156,
        ],
    ),
    "baccarat_player_and_banker_8deck": GameConfig(
        payouts=[0.975, 1, 1],  # [banker win, player wins, tie]
        probabilities=[
            0.458597,  # banker wins
            0.446247,  # player wins
            0.095156,  # tie
        ],
    ),
}
