# ---------------------
# CORE FUNCTIONS USED
# ---------------------

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


