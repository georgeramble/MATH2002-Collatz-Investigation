# ---------------------
# CORE FUNCTIONS USED
# ---------------------

# Functions related to the Collatz Tree

def node_parents(n):
    '''
    Creates parent nodes for one value n, similar to doing one_step()
    '''
    parents = []

    parents.append(2*n)

    if (n-1)%3 == 0:
        m = (n-1)//3
        if m%2 == 1 and m>0:
            parents.append(m)

    return parents

    

def tree_generator(depth):
    '''
    Generates a set amount of layers of the Collatz Tree
    '''
    levels = []
    levels.append([1])      # level 0 starts with 1

    seen = [1]

    for i in range(depth):

        current_level = levels[i]
        next_level = []

        for n in current_level:
            for parent in node_parents(n):
                if parent not in seen:
                    next_level.append(parent)
                    seen.append(parent)

        levels.append(next_level)

    return levels