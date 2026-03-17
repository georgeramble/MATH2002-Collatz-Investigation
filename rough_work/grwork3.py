def collatz_step_variant(n, a=3, b=1):
    if n % 2 == 0:
        return n // 2
    else:
        return a * n + b


def variant_sequence(start, a=3, b=1, max_steps=200):
    sequence = [start]
    n = start

    for _ in range(max_steps):
        if n == 1:
            break

        n = collatz_step_variant(n, a, b)
        sequence.append(n)

    return sequence


def run_variant_simulation(N, a=3, b=1, max_steps=200):
    start_vals = []
    lengths = []
    max_vals = []

    for n in range(1, N + 1):
        seq = variant_sequence(n, a, b, max_steps)
        start_vals.append(n)
        lengths.append(len(seq) - 1)
        max_vals.append(max(seq))

    return start_vals, lengths, max_vals


def run_variant_simulation(N, a=3, b=1, max_steps=200):
    start_vals = []
    lengths = []
    max_vals = []

    for n in range(1, N + 1):
        seq = variant_sequence(n, a, b, max_steps)
        start_vals.append(n)
        lengths.append(len(seq) - 1)
        max_vals.append(max(seq))

    return start_vals, lengths, max_vals


def variant_sequence(start, a=3, b=1, max_steps=200):
    sequence = [start]
    n = start

    for _ in range(max_steps):
        if n == 1:
            break

        n = collatz_step_variant(n, a, b)
        sequence.append(n)

    return sequence


def collatz_step_variant(n, a=3, b=1):
    if n % 2 == 0:
        return n // 2
    else:
        return a * n + b