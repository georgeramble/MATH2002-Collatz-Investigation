import matplotlib.pyplot as plt

from core_lib.collatz_functions import collatz_simulations



N_values = [1000, 2000, 5000, 10000]



def summary_values(N):
    n_val, stop_t, max_x = collatz_simulations(N)

    max_stopping = max(stop_t)
    n_at_max_stopping = n_val[stop_t.index(max_stopping)]

    max_exc = max(max_x)
    n_at_max_exc = n_val[max_x.index(max_exc)]

    avg_stopping = sum(stop_t) / len(stop_t)

    print("Maximum stopping time:", max_stopping, "at n =", n_at_max_stopping)
    print("Maximum excursion:", max_exc, "at n =", n_at_max_exc)
    print("Average stopping time:", avg_stopping)



def plot_stopping_time(N):
    ns, ts, _ = collatz_simulations(N)
    plt.figure()
    plt.plot(ns, ts)
    plt.xlabel("n")
    plt.ylabel("Total stopping time")
    plt.title(f"Total stopping time for 1 ≤ n ≤ {N}")
    plt.show()



def plot_max_excursion(N):
    ns, _, mx = collatz_simulations(N)
    plt.figure()
    plt.plot(ns, mx)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.yscale("log")
    plt.title(f"Maximum excursion for 1 ≤ n ≤ {N} (log scale)")
    plt.show()


if __name__ == "__main__":
    plot_stopping_time(2000)
    plot_max_excursion(2000)