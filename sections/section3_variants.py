# Section 3: Variants of the Collatz rule

import matplotlib.pyplot as plt

# --- --- --- --- --- --- --- --- ---

# Core Functions:

def variant_step(n, a=3, b=1):
    if n % 2 == 0:
        return n // 2
    else:
        return a * n + b


def variant_sequence(start, a=3, b=1, max_steps=200, cap=10**6):
    sequence = [start]
    seen = [start]
    n = start
    status = "max_steps"

    for _ in range(max_steps):
        if n == 1:
            status = "hit_1"
            break

        n = variant_step(n, a, b)
        sequence.append(n)

        if n > cap:
            status = "hit_cap"
            break

        if n in seen:
            status = "cycle"
            break

        seen.append(n)

    return sequence, status


def variant_simulations(N, a=3, b=1, max_steps=200, cap=10**6):
    starting_values = []
    lengths = []
    max_values = []
    statuses = []

    for n in range(1, N + 1):
        seq, status = variant_sequence(n, a=a, b=b, max_steps=max_steps, cap=cap)

        starting_values.append(n)
        lengths.append(len(seq) - 1)
        max_values.append(max(seq))
        statuses.append(status)

    return starting_values, lengths, max_values, statuses

# --- --- --- --- --- --- --- --- ---

# List the variants we will look at
variants = [
    ("Standard Collatz (3n+1)", "3n1", 3, 1),
    ("Variant 5n+1", "5n1", 5, 1),
    ("Variant 5n+3", "5n3", 5, 3)
]


# Set up starting parameters
start = 7
N = 50
max_steps = 100
cap = 10**6


results_summary = []


# Loop the investigation for all variants
for name, label, a, b in variants:

    print("\n---")
    print(name)

    seq, status = variant_sequence(start, a=a, b=b, max_steps=max_steps, cap=cap)

    print("Starting value =", start)
    print("Status:", status)
    print("Sequence:", seq)

    n_val, lengths, max_vals, statuses = variant_simulations(N, a=a, b=b, max_steps=max_steps, cap=cap)

    hit1 = 0
    hitcap = 0
    cycles = 0

    for s in statuses:
        if s == "hit_1":
            hit1 += 1
        elif s == "hit_cap":
            hitcap += 1
        elif s == "cycle":
            cycles += 1

    total = len(statuses)

    print("Proportion reaching 1:", round(hit1 / total, 3))

    results_summary.append((name, hit1, hitcap, cycles))


    plt.figure()
    plt.plot(n_val, lengths, marker='o', markersize=3, linewidth=0.8)
    plt.xlabel("Starting value")
    plt.ylabel("Sequence length")
    plt.title(name)
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section3/lengths_" + label + "_N" + str(N) + ".png")
    plt.show()

    plt.figure()
    plt.plot(n_val, max_vals, marker='o', markersize=3, linewidth=0.8)
    plt.xlabel("Starting value")
    plt.ylabel("Maximum value reached")
    plt.title(name + " : maximum value")
    plt.yscale("log")
    plt.grid(True, alpha=0.3)
    plt.savefig("figures/section3/max_values_" + label + "_N" + str(N) + ".png")
    plt.show()



print("\n---")
print("Summary of variant behaviour:")
print("---")


for name, hit1, hitcap, cycles in results_summary:
    print(name)
    print("Reached 1:", hit1)
    print("Hit cap:", hitcap)
    print("Cycles:", cycles)
    print()


#& "C:\Users\georg\anaconda3.0\python.exe" -m sections.section3_variants