# ---------------------
# CORE FUNCTIONS USED
# ---------------------

# Functions related to the Collatz Tree

def node_parents(n):
    '''
    
    '''
    parents = []

    parents.append(2*n)

    if (n-1)%3 == 0:
        m = (n-1)//3
        if m%2 == 1:
            parents.append(m)

    return parents

    

def tree_generator(depth):
    '''

    '''
    levels = []
    levels.append([1])      # level 0 starts with 1

    seen = [1]

    for i in range(depth):

        current_level = levels[i]
        next_level = []

        for n in current_level:
            for parent in collatz_parents(n):
                if parent not in seen:
                    next_level.append(parent)
                    seen.add(parent)

        levels.append(next_level)

    return levels