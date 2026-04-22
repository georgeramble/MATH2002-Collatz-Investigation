# Section 1 : First look into behaviour of the Collatz Sequence

# Import Python libraries
import matplotlib.pyplot as plt
import numpy as np

# Created a folder to save the plots 
# This is added to prevent the code from breaking when run for the first time
import os
os.makedirs("figures/section1", exist_ok=True)

# --- --- --- --- --- --- ---

# Core functions:

def validate_input(n):
    '''
    Checks if input is valid (researched how to raise TypeError)
    '''
    
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")

    
def one_step(n):
    '''
    Does one step of the Collatz seq
    '''
    validate_input(n)

    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1
    
   
def collatz_sequence(n):
    '''
    Start a Collatz sequence from n
    '''
    validate_input(n)

    seq = [n]

    while seq[-1] != 1:
        seq.append(one_step(seq[-1]))
    return seq


def stopping_time(n):
    '''
    Number of steps needed to reach 1
    '''

    return len(collatz_sequence(n)) - 1


def max_excursion(n):
    '''
    Maximum value reached in the sequence
    '''

    return max(collatz_sequence(n))


def collatz_simulations(N):
    '''
    Run Collatz simulations for 1 <= n <= N.

    Returns three lists:
    - starting values
    - stopping times
    - maximum excursions
    '''
    validate_input(N)

    starting_values = []
    stopping_times = []
    max_values = []

    for n in range(1, N+1):

        starting_values.append(n)
        stopping_times.append(stopping_time(n))
        max_values.append(max_excursion(n))

    return starting_values, stopping_times, max_values

# --- --- --- --- --- --- ---

# Functions to summarise and visualise results
# (using the predefined functions above).

def summary_values(N):
    # Prints basic stats for the 1 to N values

    n_val, stop_t, max_exc = collatz_simulations(N)

    max_stopping = max(stop_t)
    n1 = n_val[stop_t.index(max_stopping)]

    max_exc_value = max(max_exc)
    n2 = n_val[max_exc.index(max_exc_value)]

    average_stopping = sum(stop_t) / len(stop_t)

    print("Maximum stopping time =", max_stopping, "at n =", n1)
    print("Maximum excursion =", max_exc_value, "at n =", n2)
    print("Average stopping time =", round(average_stopping,3))


# Functions to plot Stopping times, Maximum excursion or Both for 'N' values:

def plot_stopping_time(N):
    n_val, stop_t, max_exc = collatz_simulations(N)

    plt.figure()
    plt.plot(n_val, stop_t, linestyle='-', marker='x', markersize=3, linewidth=0.8)
    plt.xlabel("n")
    plt.ylabel("Total stopping time")
    plt.grid(True, alpha=0.3)
    plt.title("Stopping time for 1 ≤ n ≤ " + str(N))
    plt.savefig("figures/section1/stopping_time_N" + str(N) + ".png")
    plt.show()



def plot_max_excursion(N):
    n_val, stop_t, max_exc = collatz_simulations(N)

    plt.figure()
    plt.plot(n_val, max_exc, linestyle='-', marker='x', markersize=3, linewidth=0.8)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.grid(True, alpha=0.3)

    ymax = np.percentile(max_exc, 95)  # zoom into plot to make more readable
    plt.ylim(0, ymax)

    plt.title("Maximum excursion for 1 ≤ n ≤ " + str(N))
    plt.savefig("figures/section1/max_excursion_N" + str(N) + ".png")
    plt.show()



def stopping_vs_excursion(N):
    n_val, stop_t, max_exc = collatz_simulations(N)

    plt.figure()
    plt.scatter(stop_t, max_exc, s=8)
    plt.xlabel("Total stopping time")
    plt.ylabel("Maximum excursion")
    plt.yscale("log")
    plt.grid(True, alpha=0.3)

    ymax = np.percentile(max_exc, 95)
    plt.ylim(0, ymax)

    plt.title("Stopping time vs max excursion (1 ≤ n ≤ " + str(N) + ")")
    plt.savefig("figures/section1/stopping_vs_excursion_N" + str(N) + ".png")
    plt.show()

# --- --- --- --- --- --- ---

# Plots and outputs:

N_values = [50, 200, 500]
# Values of N we will consider up to (e.g. collatz_sequence(n), from 1 to N)

for N in N_values:

    print("\n-----------------------------")
    print("Running for N =", N)

    summary_values(N)

    plot_stopping_time(N)
    plot_max_excursion(N)
    stopping_vs_excursion(N)