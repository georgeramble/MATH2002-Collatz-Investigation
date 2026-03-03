# ============================================================
# Collatz Investigation – Structured Plan
# ============================================================

# ------------------------------------------------------------
# I. Behaviour of the Standard Collatz Map
# ------------------------------------------------------------
# Core computational investigation.
#
# Main Aim:
# Explore how the Collatz map behaves for 1 ≤ n ≤ N,
# and how this behaviour changes as N increases.
#
# Focus:
# - Total stopping time
# - Maximum excursion
# - Comparison across different bounds (e.g. N = 1000, 2000, 5000)
# - Identification of extreme values
# - Correlation between stopping time and maximum excursion
#
# Key Questions:
# - Does stopping time grow steadily or irregularly?
# - Where do large spikes occur?
# - Is there a relationship between stopping time and max excursion?
# - How does behaviour change as N increases?


# ------------------------------------------------------------
# II. Structural Analysis of the Map
# ------------------------------------------------------------
# Theoretical understanding of observed behaviour.
#
# Aim:
# Explain why the standard Collatz map behaves as it does.
#
# Focus:
# - Even vs odd step dynamics
# - Why odd steps cause temporary growth
# - Parity sequence behaviour
# - Heuristic argument using logarithmic growth
# - Explanation of "average decrease" despite local increases
#
# Optional:
# - Light discussion of 2-adic interpretation (only if well understood)
#
# Goal:
# Connect empirical irregularity to structural properties of the map.


# ------------------------------------------------------------
# III. Variants of the Collatz Rule
# ------------------------------------------------------------
# Sensitivity and structural balance of the rule.
#
# Aim:
# Investigate how small changes to the rule alter long-term behaviour.
#
# Focus:
# - 5n + 1
# - 5n + 3
# - Speeded-up Collatz
# - Cycle detection
# - Divergence vs convergence
#
# Key Insight:
# The 3n + 1 rule appears delicately balanced —
# small modifications may drastically change behaviour.


# ------------------------------------------------------------
# IV. Inverse Collatz Tree Investigation (Main Extension)
# ------------------------------------------------------------
# Backward structural perspective.
#
# Aim:
# Investigate the backward structure of the Collatz map.
#
# Focus:
# - Determine inverse parents of a number
# - Construct a finite inverse tree rooted at 1
# - Study branching structure
# - Examine how quickly the tree expands
# - Investigate coverage of integers within a bound
#
# Key Questions:
# - Does the inverse tree appear to cover all integers up to a bound?
# - How does branching behave at different depths?
# - What structural patterns emerge?
#
# This provides a fundamentally different viewpoint
# from forward simulation.