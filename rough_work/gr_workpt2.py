# Reverse engineer the Collatz sequence using by defining a parent of a node

def node_parents(n):
    parents = [2 * n]

    if (n - 1) % 3 == 0:
        m = (n - 1) // 3
        if m % 2 == 1:
            parents.append(m)

    return sorted(parents)

def node_parents2(n):

    if (n - 1) % 3 == 0:
        m = (n - 1) // 3
        if m % 2 == 1:
            return (2*n, m)

    return (2*n,)

def node_parents(n):
    parents = []

    parents.append(2*n)

    if (n-1)%3 == 0:
        m = (n-1)//3
        if m%2 == 1:
            parents.append(m)

    return parents

# We need to build a Collatz Tree from 1 - it will have different levels. e.g. level 0 = 1, level 1 is for parents of 1, then level 2 parents of those, etc..
# The tree will grow upwards from 1

def generate_collatz_tree(depth):

    levels = []
    levels.append([1])      # level 0 starts with 1

    seen = set()
    seen.add(1)

    for i in range(depth):

        current_level = levels[i]
        next_level = []

        for number in current_level:

            parents = collatz_parents(number)

            for parent in parents:

                if parent not in seen:
                    next_level.append(parent)
                    seen.add(parent)

        levels.append(next_level)

    return levels

# Print levels:

levels = generate_collatz_tree(8)

for i in range(len(levels)):
    print("Level", i, ":", levels[i])
    print("Number of nodes:", len(levels[i]))



levels = generate_collatz_tree(12)

sizes = []
for level in levels:
    sizes.append(len(level))

import matplotlib.pyplot as plt

plt.plot(range(len(sizes)), sizes, marker='o')
plt.xlabel("Tree depth")
plt.ylabel("Number of nodes")
plt.title("Growth of the Collatz tree")
plt.show()


branching = []

for level in levels:
    count = 0
    for n in level:
        if len(collatz_parents(n)) == 2:
            count += 1
    branching.append(count)


plt.plot(range(len(branching)), branching)
plt.xlabel("Tree depth")
plt.ylabel("Nodes with two parents")
plt.title("Branching in the Collatz tree")
plt.show()



max_values = []

for level in levels:
    if len(level) > 0:
        max_values.append(max(level))
    else:
        max_values.append(0)

plt.plot(range(len(max_values)), max_values)
plt.xlabel("Tree depth")
plt.ylabel("Largest number")
plt.title("Largest number in Collatz tree by depth")
plt.show()


all_nodes = []

for level in levels:
    all_nodes.extend(level)

print(sorted(all_nodes))

example structure

levels = generate_collatz_tree(12)

sizes = []
max_values = []

for level in levels:
    sizes.append(len(level))
    if len(level) > 0:
        max_values.append(max(level))
    else:
        max_values.append(0)

# plot size
plt.plot(range(len(sizes)), sizes)

# plot largest number
plt.plot(range(len(max_values)), max_values)


import networkx as nx
import matplotlib.pyplot as plt


def draw_collatz_tree(levels):

    G = nx.DiGraph()

    for level in levels:
        for node in level:
            parents = collatz_parents(node)

            for p in parents:
                if p in sum(levels, []):   # check node exists in tree
                    G.add_edge(p, node)

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        node_color="lightblue",
        font_size=8
    )

    plt.title("Collatz Tree")
    plt.show()

    
levels = generate_collatz_tree(6)

draw_collatz_tree(levels)


depths = {}
levels = generate_collatz_tree(10)

for i, level in enumerate(levels):
    for n in level:
        depths[n] = i

for n in list(depths.keys())[:20]:
    print(n, depths[n], stopping_time(n))


branch_nodes = []

for level in levels:
    for n in level:
        if len(collatz_parents(n)) == 2:
            branch_nodes.append(n)

len(branch_nodes) / len(all_nodes)

even_count = 0
odd_count = 0

for level in levels:
    for n in level:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(even_count, odd_count)

max_values = []

for level in levels:
    if level:
        max_values.append(max(level))

all_nodes = []

for level in levels:
    all_nodes.extend(level)

print(len(all_nodes))
print(max(all_nodes))


generate_collatz_tree(root=5)