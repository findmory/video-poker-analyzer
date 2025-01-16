from utils import get_game, validate_game_config
import numpy as np
import matplotlib.pyplot as plt

# SETUP HERE #
num_bets = 100000
initial_balance = 0
num_simulations = 2
game_name = "9/6_JOB"
results = []


def run_simulation(game_data):
    # Set up the payoffs and probabilities
    payoffs = np.array(game_data.payouts)
    probabilities = np.array(game_data.probabilities)

    # Initialize tracking variables
    balance = initial_balance
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


def plot_simulation_results(results, expected_value):
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


def main():
    # Get a specific game configuration
    game_data = get_game("8/5_JOB")
    print(f"Payouts for 8/5 JOB: {game_data.payouts}")

    # Validate a game configuration
    is_valid = validate_game_config(game_data)
    print(f"Is game config valid? {is_valid}")

    # Calculate expected value
    expected_value = sum(
        p * v for p, v in zip(game_data.probabilities, game_data.payouts)
    )
    print(f"Expected value: {expected_value:.4f}")

    for i in range(num_simulations):
        result = run_simulation(game_data)
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
    plot_simulation_results(results, expected_value)


if __name__ == "__main__":
    main()
