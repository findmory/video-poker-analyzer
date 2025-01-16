from typing import Dict, List, NamedTuple


class GameConfig(NamedTuple):
    payouts: List[int]
    probabilities: List[float]


GAMES: Dict[str, GameConfig] = {
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
}
