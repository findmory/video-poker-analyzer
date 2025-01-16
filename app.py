import argparse
from typing import Optional
from utils import get_game, validate_game_config
import numpy as np
import matplotlib.pyplot as plt
from data import GAMES

# SETUP HERE #
# num_bets = 100000
# initial_balance = 0
# num_simulations = 2
results = []


def create_game_picker() -> str:
    """
    Create an interactive picker for selecting a game.

    Returns:
        str: Selected game name
    """
    print("\nAvailable Games:")
    print("-" * 30)

    # Create numbered list of games
    for idx, game_name in enumerate(sorted(GAMES.keys()), 1):
        print(f"{idx}. {game_name}")

    while True:
        try:
            choice = input("\nSelect a game (enter number): ")
            game_idx = int(choice) - 1
            game_names = sorted(GAMES.keys())

            if 0 <= game_idx < len(game_names):
                return game_names[game_idx]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def run_simulation(game_data, num_bets=100000):
    # Set up the payoffs and probabilities
    payoffs = np.array(game_data.payouts)
    probabilities = np.array(game_data.probabilities)

    # Initialize tracking variables
    balance = 0
    highest_balance = balance
    lowest_balance = balance
    balance_history = [balance]

    # Run simulation
    for _ in range(num_bets):
        # Make a bet (costs 1 unit)
        balance -= 1

        # Determine outcome using numpy's random choice
        outcome = np.random.choice(payoffs, p=probabilities)

        # Add winnings to balance
        balance += outcome

        # Update highest and lowest points
        highest_balance = max(highest_balance, balance)
        lowest_balance = min(lowest_balance, balance)

        # Store balance for history
        balance_history.append(balance)

    return {
        "final_balance": balance,
        "highest_point": highest_balance,
        "lowest_point": lowest_balance,
        "balance_history": balance_history,
    }


def plot_simulation_results(results, expected_value, game_name):
    plt.figure(figsize=(15, 10))

    # Plot individual simulation paths
    for i, result in enumerate(results):
        plt.plot(
            result["balance_history"], alpha=0.3, label=f"Simulation {i+1}"
        )

    # Add horizontal line at y=0
    plt.axhline(y=0, color="r", linestyle="--", alpha=0.5)

    # Customize the plot
    plt.title(
        f"Balance Over Time - Multiple Monte Carlo Simulations - {game_name}\n"
        f"Expected value: {expected_value:.4f}"
    )
    plt.xlabel("Number of Bets")
    plt.ylabel("Balance")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Show the plot
    plt.show()


def analyze_game(
    game_name: Optional[str] = None,
    num_bets: int = 100000,
    num_simulations: int = 2,
) -> None:
    """
    Analyze a game's configuration and print results.

    Args:
        game_name: Optional name of game to analyze. If None, will use picker.
    """
    if game_name is None:
        game_name = create_game_picker()
    # Get a specific game configuration
    game_data = get_game(game_name)
    print(f"Payouts for {game_name}: {game_data.payouts}")

    # Validate a game configuration
    is_valid = validate_game_config(game_data)
    print(f"Is game config valid? {is_valid}")

    # Calculate expected value
    expected_value = sum(
        p * v for p, v in zip(game_data.probabilities, game_data.payouts)
    )
    print(f"Expected value: {expected_value:.4f}")

    for i in range(num_simulations):
        result = run_simulation(
            game_data,
            num_bets=num_bets,
        )
        results.append(result)
        print(f"\nSimulation {i+1} Results:")
        print(f"Final Balance: {result['final_balance']:.2f} units")
        print(f"Highest Point: {result['highest_point']:.2f} units")
        print(f"Lowest Point: {result['lowest_point']:.2f} units")

    # Calculate average results
    avg_final = sum(r["final_balance"] for r in results) / num_simulations
    avg_highest = sum(r["highest_point"] for r in results) / num_simulations
    avg_lowest = sum(r["lowest_point"] for r in results) / num_simulations

    print("\nAverage Results Over All Simulations:")
    print(f"Average Final Balance: {avg_final:.2f} units")
    print(f"Average Highest Point: {avg_highest:.2f} units")
    print(f"Average Lowest Point: {avg_lowest:.2f} units")

    # Plot the results
    plot_simulation_results(results, expected_value, game_name)


def main():
    parser = argparse.ArgumentParser(description="Game Configuration Analyzer")
    parser.add_argument(
        "--game",
        "-g",
        help="Name of game to analyze (optional, will show picker if not provided)",
    )

    parser.add_argument(
        "--bets",
        "-b",
        type=int,
        default=100000,
        help="Number of bets to simulate (default: 100000)",
    )
    parser.add_argument(
        "--sims",
        "-s",
        type=int,
        default=2,
        help="Number of simulations to run (default: 2)",
    )

    args = parser.parse_args()
    analyze_game(args.game, args.bets, args.sims)


if __name__ == "__main__":
    main()
