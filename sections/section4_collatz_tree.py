# --------------------------
# Section 4: Collatz Trees
# --------------------------

import matplotlib.pyplot as plt

from core_lib.collatz_tree import node_parents, tree_generator


# Print first few levels
depth = 8
levels = tree_generator(depth)

print("\nTree structure:")

for i, level in enumerate(levels):
    print(f"Level {i}: {level}")
    print(f"Nodes in level: {len(level)}")
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
print("All nodes (sorted):")
print(sorted(all_nodes))

#& "C:\Users\georg\anaconda3.0\python.exe" -m sections.section4_collatz_tree
#git add . ; git commit -m "collatz tree functions update" ; git push origin main