# Section 3: Variants of the Collatz rule

# Import Python libraries
import matplotlib.pyplot as plt
import os

# Create plot folder
os.makedirs("figures/section3", exist_ok=True)

# --- --- --- --- --- --- ---

# Core functions:

def validate_input(n):
    '''
    Checks if input is valid
    '''
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")


def variant_step(n, a, b):
    '''
    Does one step of a Collatz-type rule
    '''
    validate_input(n)

    if n % 2 == 0:
        return n // 2
    else:
        return a * n + b


def variant_sequence(start, a, b, max_steps=100, cap=10**6):
    '''
    Generates a full sequence for a Collatz-type rule
    '''
    validate_input(start)

    sequence = [start]
    seen = {start}
    n = start
    status = "iteration_limit_reached"

    for i in range(max_steps):
        if n == 1:
            status = "reached_1"
            break

        n = variant_step(n, a, b)
        sequence.append(n)

        if n > cap:
            status = "too_large"
            break

        if n in seen:
            status = "cycle"
            break

        seen.add(n)

    return sequence, status


def variant_simulations(N, a, b, max_steps=100, cap=10**6):
    '''
    Runs the variant for all starting values from 1 to N
    '''
    validate_input(N)

    starting_values = []
    lengths = []
    max_values = []
    statuses = []

    for n in range(1, N + 1):
        seq, status = variant_sequence(n, a, b, max_steps=max_steps, cap=cap)

        starting_values.append(n)
        lengths.append(len(seq) - 1)
        max_values.append(max(seq))
        statuses.append(status)

    return starting_values, lengths, max_values, statuses

# --- --- --- --- --- --- ---

# Functions to summarise and visualise results:

def summary_variant(name, N, a, b, max_steps=100, cap=10**6):
    n_val, lengths, max_vals, statuses = variant_simulations(N, a, b, max_steps=max_steps, cap=cap)

    reached_1 = 0
    cycles = 0
    too_large = 0
    iteration_limit_reached = 0

    for status in statuses:
        if status == "reached_1":
            reached_1 += 1
        elif status == "cycle":
            cycles += 1
        elif status == "too_large":
            too_large += 1
        elif status == "iteration_limit_reached":
            iteration_limit_reached += 1

    print(name)
    print("Reached 1:", reached_1)
    print("Cycles:", cycles)
    print("Grew too large:", too_large)
    print("Iteration limit reached:", iteration_limit_reached)
    print("Proportion reaching 1:", round(reached_1 / len(statuses), 3))


def plot_variant_lengths(name, label, N, a, b, max_steps=100, cap=10**6):
    n_val, lengths, max_vals, statuses = variant_simulations(N, a, b, max_steps=max_steps, cap=cap)

    plt.figure()
    plt.plot(n_val, lengths, marker='o', markersize=3, linewidth=0.8)
    plt.xlabel("Starting value")
    plt.ylabel("Sequence length")
    plt.title(name + " : sequence length")
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section3/lengths_" + label + "_N" + str(N) + ".png")
    plt.show()


def plot_variant_max_values(name, label, N, a, b, max_steps=100, cap=10**6):
    n_val, lengths, max_vals, statuses = variant_simulations(N, a, b, max_steps=max_steps, cap=cap)

    plt.figure()
    plt.plot(n_val, max_vals, marker='o', markersize=3, linewidth=0.8)
    plt.xlabel("Starting value")
    plt.ylabel("Maximum value reached")
    plt.title(name + " : maximum value")
    plt.yscale("log")
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section3/max_values_" + label + "_N" + str(N) + ".png")
    plt.show()

# --- --- --- --- --- --- ---

# Plots and outputs:

variants = [
    ("Standard Collatz (3n+1)", "3n1", 3, 1),
    ("Variant 5n+1", "5n1", 5, 1),
    ("Variant 5n+3", "5n3", 5, 3)]

start = 7
N = 50
max_steps = 100
cap = 10**6

for name, label, a, b in variants:
    print("\n-----------------------------")
    summary_variant(name, N, a, b, max_steps=max_steps, cap=cap)

    plot_variant_lengths(name, label, N, a, b, max_steps=max_steps, cap=cap)
    plot_variant_max_values(name, label, N, a, b, max_steps=max_steps, cap=cap)