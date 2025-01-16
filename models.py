from typing import List, NamedTuple


class GameConfig(NamedTuple):
    payouts: List[int]
    probabilities: List[float]
