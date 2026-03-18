from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, List


def v2(x: int) -> int:
    """Return the largest k such that 2^k divides x (for x > 0)."""
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k


def step_custom(
    n: int,
    a: int = 3,
    b: int = 1,
    accelerated: bool = False,
    mod_m: Optional[int] = None,
) -> int:
    """
    One step of a Collatz-type rule.

    If n is even: n -> n/2
    If n is odd:  n -> a*n + b

    If accelerated=True, divide out all factors of 2 after the odd step.
    If mod_m is given, return the result modulo mod_m.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if a <= 0:
        raise ValueError("a must be positive")

    if n % 2 == 0:
        nxt = n // 2
    else:
        nxt = a * n + b
        if nxt <= 0:
            raise ValueError(f"odd-step produced non-positive value: {nxt}")

        if accelerated:
            while nxt % 2 == 0:
                nxt //= 2

    if mod_m is not None:
        if mod_m <= 0:
            raise ValueError("mod_m must be a positive integer")
        nxt %= mod_m

    return nxt


@dataclass
class TrajectoryResult:
    start: int
    a: int
    b: int
    accelerated: bool
    mod_m: Optional[int]
    path: List[int]
    status: str
    cycle: List[int]
    steps: int
    peak: int


def run_trajectory(
    start: int,
    a: int = 3,
    b: int = 1,
    accelerated: bool = False,
    mod_m: Optional[int] = None,
    target: Optional[int] = 1,
    max_iter: int = 10_000,
    cap: Optional[int] = None,
    detect_cycle: bool = True,
) -> TrajectoryResult:
    """Generate a trajectory under the custom Collatz-type rule."""
    if start <= 0:
        raise ValueError("start must be positive")

    path: List[int] = [start]
    peak = start
    seen: Dict[int, int] = {}
    if detect_cycle:
        seen[start] = 0

    n = start
    status = "max_iter"
    cycle: List[int] = []

    for _ in range(max_iter):
        if target is not None and n == target:
            status = "hit_target"
            break

        if cap is not None and mod_m is None and n > cap:
            status = "hit_cap"
            break

        n = step_custom(n, a=a, b=b, accelerated=accelerated, mod_m=mod_m)
        path.append(n)
        peak = max(peak, n)

        if detect_cycle:
            if n in seen:
                idx = seen[n]
                cycle = path[idx:]
                status = "cycle"
                break
            seen[n] = len(path) - 1

    return TrajectoryResult(
        start=start,
        a=a,
        b=b,
        accelerated=accelerated,
        mod_m=mod_m,
        path=path,
        status=status,
        cycle=cycle,
        steps=len(path) - 1,
        peak=peak,
    )


@dataclass
class SummaryRow:
    n: int
    steps: int
    peak: int
    status: str
    cycle_len: int


def summarize_one(
    n: int,
    a: int = 3,
    b: int = 1,
    accelerated: bool = False,
    mod_m: Optional[int] = None,
    target: Optional[int] = 1,
    max_iter: int = 10_000,
    cap: Optional[int] = None,
) -> SummaryRow:
    r = run_trajectory(
        start=n,
        a=a,
        b=b,
        accelerated=accelerated,
        mod_m=mod_m,
        target=target,
        max_iter=max_iter,
        cap=cap,
        detect_cycle=True,
    )
    return SummaryRow(
        n=n,
        steps=r.steps,
        peak=r.peak,
        status=r.status,
        cycle_len=len(r.cycle) if r.status == "cycle" else 0,
    )


def scan_range(
    N: int,
    a: int = 3,
    b: int = 1,
    accelerated: bool = False,
    mod_m: Optional[int] = None,
    target: Optional[int] = 1,
    max_iter: int = 10_000,
    cap: Optional[int] = None,
) -> List[SummaryRow]:
    """Return summary rows for n = 1, 2, ..., N."""
    if N <= 0:
        raise ValueError("N must be positive")

    rows = []
    for n in range(1, N + 1):
        rows.append(
            summarize_one(
                n,
                a=a,
                b=b,
                accelerated=accelerated,
                mod_m=mod_m,
                target=target,
                max_iter=max_iter,
                cap=cap,
            )
        )
    return rows