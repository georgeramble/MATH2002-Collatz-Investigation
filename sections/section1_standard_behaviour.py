# --------------------------------
# Section 1 : Standard behaviour
# --------------------------------

import matplotlib.pyplot as plt
import numpy as np

from core_lib.collatz_functions import collatz_simulations


def plot_stopping_time(n_val, stop_t, N):
    '''
    Function to plot the stopping time
    '''
    plt.figure()
    plt.plot(n_val, stop_t, linestyle='-', marker='x', markersize=3, linewidth=0.8)
    plt.xlabel("n")
    plt.ylabel("Total stopping time")
    plt.grid(True, alpha=0.3)
    plt.title("Stopping time for 1 ≤ n ≤ " + str(N))
    plt.savefig("figures/section1/stopping_time_N" + str(N) + ".png")
    plt.show()


def plot_max_excursion(n_val, stop_t, N):
    '''
    Function to plot maximum excursion
    '''
    plt.figure()
    plt.plot(n_val, max_exc, linestyle='-', marker='x', markersize=3, linewidth=0.8)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.grid(True, alpha=0.3)

    ymax = np.percentile(max_exc, 95)  # zoom into plot to make more readable
    plt.ylim(1, ymax)

    plt.title("Maximum excursion for 1 ≤ n ≤ " + str(N))
    plt.savefig("figures/section1/max_excursion_N" + str(N) + ".png")
    plt.show()


def stopping_vs_excursion(n_val, stop_t, N):
    '''
    Function to plot stopping time against maximum excursion
    '''
    plt.figure()
    plt.scatter(stop_t, max_exc, s=8)
    plt.xlabel("Total stopping time")
    plt.ylabel("Maximum excursion")
    plt.yscale("log")
    plt.grid(True, alpha=0.3)

    ymax = np.percentile(max_exc, 95)
    plt.ylim(1, ymax)

    plt.title("Stopping time vs max excursion (1 ≤ n ≤ " + str(N) + ")")
    plt.savefig("figures/section1/stopping_vs_excursion_N" + str(N) + ".png")
    plt.show()


# Outputs:
N_values = [50, 100, 200, 500, 1000]

for N in N_values:

    print("\n-----------------------------")
    print("Running for N =", N)

    n_val, stop_t, max_exc = collatz_simulations(N)

    max_stop = max(stop_t)
    n_stop = n_val[stop_t.index(max_stop)]

    max_excursion = max(max_exc)
    n_exc = n_val[max_exc.index(max_excursion)]

    print("Largest stopping time:", max_stop, "at n =", n_stop)
    print("Largest maximum excursion:", max_excursion, "at n =", n_exc)
    print("Average stopping time:", round(sum(stop_t)/len(stop_t), 3))
    print("Range of stopping times:", min(stop_t), "to", max(stop_t))
    print("Range of maximum excursions:", min(max_exc), "to", max(max_exc))

    plot_stopping_time(n_val, stop_t, N)
    plot_max_excursion(n_val, max_exc, N)
    stopping_vs_excursion(stop_t, max_exc, N)







# to run in terminal : & "C:\Users\georg\anaconda3.0\python.exe" -m sections.section1_standard_behaviour

# Note - need to write up about the comparison
# No relation between max exc and stopping times