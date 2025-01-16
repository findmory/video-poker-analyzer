# Game Configuration Analyzer

A Python tool for analyzing game configurations, calculating expected values, and running simulations.

## Installation

1. Clone this repository:

```bash
git clone [repository-url]
cd game-analyzer
```

2. Make sure you have Python 3.6+ installed.

## Project Structure

```
game-analyzer/
├── models.py     # Data models and type definitions
├── data.py       # Game configurations data
├── utils.py      # Utility functions for analysis
└── main.py       # CLI interface and main program
```

## Usage

### Basic Usage

Run the interactive picker mode:

```bash
python main.py
```

This will display a list of available games and prompt you to choose one.

### Command Line Options

```
usage: main.py [-h] [--game GAME] [--bets BETS] [--sims SIMS]

options:
  -h, --help            show this help message and exit
  --game GAME, -g GAME  Name of game to analyze (optional, will show picker if not provided)
  --bets BETS, -b BETS  Number of bets to simulate (default: 100000)
  --sims SIMS, -s SIMS  Number of simulations to run (default: 2)
```

### Examples

1. Analyze a specific game:

```bash
python main.py --game 8/5_JOB
```

2. Run analysis with custom number of bets and simulations:

```bash
python main.py --game 8/5_JOB --bets 50000 --sims 5
```

3. Using short form parameters:

```bash
python main.py -g 8/5_JOB -b 50000 -s 5
```

### Sample Output

```
Analyzing game: 8/5_JOB
Running 2 simulation(s) with 100,000 bets each
------------------------------

Payouts:
1.  800 (0.00002489)
2.   50 (0.00010766)
...

Configuration valid: True
Expected value: 0.9534
Return percentage: 95.34%

Simulation parameters:
Number of bets per simulation: 100,000
Number of simulations: 2
```

## Adding New Games

To add a new game, edit `data.py` and add a new entry to the `GAMES` dictionary:

```python
GAMES["NEW_GAME"] = GameConfig(
    payouts=[...],
    probabilities=[...]
)
```

## Features

- Interactive game selection picker
- Configurable number of bets and simulations
- Detailed payout and probability analysis
- Configuration validation
- Expected value calculation
- Return percentage calculation

## Requirements

- Python 3.6+
- No additional dependencies required

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
