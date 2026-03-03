# Section 1 : First look into behaviour of the Collatz Sequence

# Import Python Libraries
import matplotlib.pyplot as plt
import numpy as np

# Import Pre-Defined Functions
from core_lib.collatz_functions import collatz_simulations

# --- ---

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

# Outputs:

N_values = [50, 100, 200, 500, 1000]
# Values of N we will consider up to (e.g. collatz_sequence(n), from 1 to N)

for N in N_values:

    print("\n-----------------------------")
    print("Running for N =", N)

    summary_values(N)

    plot_stopping_time(N)
    plot_max_excursion(N)
    stopping_vs_excursion(N)

# to run in terminal : & "C:\Users\georg\anaconda3.0\python.exe" -m sections.section1_standard_behaviour

# Note - need to write up about the comparison
# No relation between max exc and stopping times