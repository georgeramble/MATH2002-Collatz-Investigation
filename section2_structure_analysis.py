# Section 2: Related sequences and further sequence analysis

# Import Python libraries
import matplotlib.pyplot as plt
import numpy as np
import os

# Create plot folder
os.makedirs("figures/section2", exist_ok=True)

# --- --- --- --- --- --- ---

# Core functions:

def collatz(n):
    seq = [n]

    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)

    return seq


def colplot(n):
    plt.figure()
    plt.plot(collatz(n))
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.title("Collatz sequence starting from n = " + str(n))
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section2/collatz_sequence_n" + str(n) + ".png")
    plt.show()


def stoptime(n):
    return len(collatz(n)) - 1


def stoptimeplot(n):
    x = list(range(1, n + 1))
    y = []

    for i in range(1, n + 1):
        y.append(stoptime(i))

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("n")
    plt.ylabel("Stopping time σ(n)")
    plt.grid(True, alpha=0.3)
    plt.title("Stopping time for 1 ≤ n ≤ " + str(n))
    plt.savefig("figures/section2/stopping_time_N" + str(n) + ".png")
    plt.show()


def maxexcurge(n):
    return max(collatz(n))


def maxexcurgeplot(n):
    x = list(range(1, n + 1))
    y = []

    for i in range(1, n + 1):
        y.append(maxexcurge(i))

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.grid(True, alpha=0.3)
    plt.title("Maximum excursion for 1 ≤ n ≤ " + str(n))
    plt.savefig("figures/section2/max_excursion_N" + str(n) + ".png")
    plt.show()


def mestplot(n):
    x = list(range(1, n + 1))

    y = []
    for i in range(1, n + 1):
        y.append(stoptime(i))

    q = []
    for i in range(1, n + 1):
        q.append(maxexcurge(i))

    plt.figure()
    plt.plot(x, y, label="stopping time")
    plt.plot(x, q, label="Max excursion")
    plt.xlabel("n")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title("Stopping time and maximum excursion for 1 ≤ n ≤ " + str(n))
    plt.savefig("figures/section2/stopping_max_excursion_N" + str(n) + ".png")
    plt.show()


def correlationplot(n):
    x = []
    for i in range(1, n + 1):
        x.append(stoptime(i))

    y = []
    for i in range(1, n + 1):
        y.append(maxexcurge(i))

    m, c = np.polyfit(x, y, 1)
    p = np.linspace(min(x), max(x), 100)
    q = m * p + c

    plt.figure()
    plt.plot(p, q, color="red", label="Regression line")
    plt.xlabel("Stopping time")
    plt.ylabel("Max excursion")
    plt.scatter(x, y)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title("Stopping time vs maximum excursion")
    plt.savefig("figures/section2/correlation_N" + str(n) + ".png")
    plt.show()


def parity_sequence(n):
    seq = []

    while n != 1:
        seq.append(n % 2)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    seq.append(0)
    return seq


def parity_plot(N, maxlen):
    data = np.zeros((N, maxlen))

    for i in range(1, N + 1):
        p = parity_sequence(i)
        data[i - 1, :len(p)] = p[:maxlen]

    plt.figure()
    plt.imshow(data, cmap="binary", interpolation="none")
    plt.xlabel("Step")
    plt.ylabel("Starting number")
    plt.title("Parity sequence plot for 1 ≤ n ≤ " + str(N))
    plt.savefig("figures/section2/parity_plot_N" + str(N) + ".png")
    plt.show()


def parity_fraction(n):
    p = parity_sequence(n)
    return sum(p) / len(p)


def parity_fraction_graph(N):
    x = np.arange(1, N + 1)
    y = [parity_fraction(n) for n in x]

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Starting number")
    plt.ylabel("Fraction of odd numbers in parity sequence")
    plt.title("Parity fraction for starting numbers 1 to " + str(N))
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section2/parity_fraction_N" + str(N) + ".png")
    plt.show()


def max_excursion_record_sequence(N):
    record_sequence = []
    record_n = []
    current_record = 1

    for n in range(1, N + 1):
        max_excursion = maxexcurge(n)

        if max_excursion > current_record:
            record_n.append(n)
            current_record = max_excursion
            record_sequence.append((n, current_record))

    return record_sequence, record_n


def me_rs_graph(N):
    record_sequence, record_n = max_excursion_record_sequence(N)

    x = [n for n, excursion in record_sequence]
    y = [excursion for n, excursion in record_sequence]

    plt.figure()
    plt.plot(x, y, "o")
    plt.xlabel("Starting number")
    plt.ylabel("Maximum excursion")
    plt.title("Record maximum excursions for starting numbers 1 to " + str(N))
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section2/record_max_excursion_N" + str(N) + ".png")
    plt.show()


def stopping_time_record_sequence(N):
    record_sequence = []
    record_n = []
    current_record = 0

    for n in range(1, N + 1):
        st = stoptime(n)

        if st > current_record:
            record_n.append(n)
            current_record = st
            record_sequence.append((n, current_record))

    return record_sequence, record_n


def st_rs_graph(N):
    record_sequence, record_n = stopping_time_record_sequence(N)

    x = [n for n, st in record_sequence]
    y = [st for n, st in record_sequence]

    plt.figure()
    plt.plot(x, y, "o")
    plt.xlabel("Starting number")
    plt.ylabel("Stopping time")
    plt.title("Record stopping times for starting numbers 1 to " + str(N))
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section2/record_stopping_time_N" + str(N) + ".png")
    plt.show()


def odd_step_valuations(n):
    seq = collatz(n)
    vals = []

    for num in seq:
        if num % 2 == 1 and num != 1:
            x = 3 * num + 1
            i = 0

            while x % 2 == 0:
                i += 1
                x //= 2

            vals.append((num, i))

    return vals

# --- --- --- --- --- --- ---

# Plots and outputs:

mestplot(26)
correlationplot(26)

parity_plot(50, 50)
parity_fraction_graph(512)

me_rs_graph(10000)
st_rs_graph(10000)

print("2-adic valuations for starting value 27:")
print(odd_step_valuations(27))
