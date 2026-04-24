# Section 4: Collatz Trees

# Import Python libraries:
import matplotlib.pyplot as plt
import os

# Create plot folder
os.makedirs("figures/section4", exist_ok=True)

# --- --- --- --- --- --- --- --- ---

# Core functions:

def node_parents(n):
    '''
    Returns all valid parent nodes of n in the Collatz Tree
    '''
    parents = []
    parents.append(2*n)

    if (n - 1) % 3 == 0:
        m = (n - 1) // 3

        if m % 2 == 1 and m > 0:
            parents.append(m)

    return parents


def validate_depth(depth):
    '''
    Similar function to validate_input(), allows for only positive integers
    '''
    if type(depth) != int:
        raise TypeError("n must be an integer")
    if depth<0:
        raise ValueError("n must be positive")


def tree_generator(depth):
    '''
    Generates the Collatz Tree levels up to the given depth
    '''
    validate_depth(depth)

    levels = []
    levels.append([1])      # level 0 starts with 1

    seen = {1}

    for i in range(depth):
        current_level = levels[i]
        next_level = []

        for n in current_level:

            for parent in node_parents(n):

                if parent not in seen:
                    next_level.append(parent)
                    seen.add(parent)
                    
        levels.append(next_level)
    return levels

# --- --- --- --- --- --- ---

# Plots and outputs:

# Print first few levels
depth = 8
levels = tree_generator(depth)

print("\nTree structure:")

for i in range(len(levels)):
    print("Level", i, ":", levels[i])
    print("Nodes in level:", len(levels[i]))
    print()


# Plot number of nodes in each level
sizes = []
for level in levels:
    sizes.append(len(level))

plt.figure()
plt.plot(range(len(sizes)), sizes, marker='o')
plt.xlabel("Tree depth")
plt.ylabel("Number of nodes")
plt.grid(True, alpha=0.3)

plt.title("Growth of the Collatz tree (depth = " + str(depth) + ")")
plt.savefig("figures/section4/tree_growth_depth_" + str(depth) + ".png")

plt.show()


# Plot largest value in each level
max_values = []
for level in levels:
    if len(level) > 0:
        max_values.append(max(level))
    else:
        max_values.append(0)

plt.figure()
plt.plot(range(len(max_values)), max_values, marker='o')
plt.xlabel("Tree depth")
plt.ylabel("Largest value")
plt.grid(True, alpha=0.3)

plt.title("Largest value in Collatz tree levels (depth = " + str(depth) + ")")
plt.savefig("figures/section4/tree_max_values_depth_" + str(depth) + ".png")

plt.show()


# Scatter plot of nodes by depth
x_vals = []
y_vals = []

for level_num, level in enumerate(levels):
    for node in level:
        x_vals.append(level_num)
        y_vals.append(node)

plt.figure()
plt.scatter(x_vals, y_vals, s=10)
plt.xlabel("Tree depth")
plt.ylabel("Node value")
plt.yscale("log")
plt.grid(True, alpha=0.3)

plt.title("Nodes in the Collatz tree by depth")
plt.savefig("figures/section4/tree_nodes_scatter_depth_" + str(depth) + ".png")

plt.show()


# List all nodes discovered
all_nodes = []

for level in levels:
    all_nodes.extend(level)

print("Total nodes discovered:", len(all_nodes))
print("Largest value discovered:", max(all_nodes))

#git add . ; git commit -m "collatz tree functions update" ; git push origin main