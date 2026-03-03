def one_step(n):
    # Does one step of the Collatz seq
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1
    
def collatz_sequence(n):
    # Start a Collatz sequence from n

    collatz = [n]
    while collatz[-1]!=1:
        collatz.append(one_step(collatz[-1]))
    return collatz

def total_stopping_time(n):
    # Number of steps needed to reach 1

    return len(collatz_sequence(n))-1

def max_excursion(n):
    # Maximum value reached in the sequence

    return max(collatz_sequence(n))


# ------

# Found a way to add error messages,
# easy to add to some functions to make better.

# if n <= 0:
    #raise ValueError("n must be positive")

# So now have:

def one_step(n):
    # Does one step of the Collatz seq
    if n <= 0:
        raise ValueError("n must be positive")

    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1
    
def collatz_sequence(n):
    # Start a Collatz sequence from n
    if n <= 0:
        raise ValueError("n must be positive")

    collatz = [n]

    while collatz[-1]!=1:
        collatz.append(one_step(collatz[-1]))
    return collatz

def total_stopping_time(n):
    # Number of steps needed to reach 1

    return len(collatz_sequence(n))-1

def max_excursion(n):
    # Maximum value reached in the sequence

    return max(collatz_sequence(n))

# Now going to move onto other stuff:

# ------

# Actually scratch that could make a helper function for it:

def validate_input(n):
    # Checks if input is valid
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n<=0:
        raise ValueError("n must be positive")
    
# Had to research how to check Type errors to add on.

# Now:

def one_step(n):
    # Does one step of the Collatz seq
    validate_input(n)

    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1
    
def collatz_sequence(n):
    # Start a Collatz sequence from n
    validate_input(n)

    collatz = [n]

    while collatz[-1]!=1:
        collatz.append(one_step(collatz[-1]))
    return collatz

def total_stopping_time(n):
    # Number of steps needed to reach 1

    return len(collatz_sequence(n))-1

def max_excursion(n):
    # Maximum value reached in the sequence

    return max(collatz_sequence(n))

# ------

# Now have tried to attempt all code Luke did
# These are the core functions to include now need to go down a seperate path for developement

# I am going to simulate 'N' values of the collatz sequence next:

def collatz_simulations(N):
    # Run Collatz simulations for 1 <= n <= N

    # Finds starting values and their total stopping times / max excursion
    # Returns three seperate lists to for them

    validate_input(N)

    starting_values = []
    stopping_times = []
    max_values = []

    for n in range(1, N+1):
        starting_values.append(n)
        stopping_times.append(total_stopping_time(n))
        max_values.append(max_excursion(n))

    return starting_values, stopping_times, max_values

# Slight correction to make more efficient (doens't involve calculating the sequence multiple times)

def collatz_simulations(N):
    # Run Collatz simulations for 1 <= n <= N

    # Finds starting values and their total stopping times / max excursion
    # Returns three seperate lists to for them

    validate_input(N)

    starting_values = []
    stopping_times = []
    max_values = []

    for n in range(1, N+1):
        col = collatz_sequence(n)
        
        starting_values.append(n)
        stopping_times.append(len(col) - 1)
        max_values.append(max(col))

    return starting_values, stopping_times, max_values

# This centralises the process for all stopping times and max excursion
# values and can be used for plots later on

# ------

# Stopping time variant: 
# Stopping time until it drops under its original value.

def stopping_time_under_n(n):
    # Steps until it first is <n

    validate_input(n)
    if n == 1:
        return 0
    
    col = collatz_sequence(n)

    for i, value in enumerate(col):
        if value < n:
            return i
        
    return 0


# That was out of interest.

# Now I need to review what we can discover to decide what else to look into:

# Just made a plan document - 4 main branches.

# Now going to keep trying to finish the 1st branch.


# ------ 

# Spending some time reproducing Lukes work from last week:

import matplotlib.pyplot as plt
import numpy as np

def collatz(n):
    seq=[n]
    while seq[-1]!=1:
        if seq[-1]%2==0:
            seq.append((seq[-1])//2)
        else:
            seq.append((3*seq[-1])+1)
    return seq
        
def colplot(n):
    plt.plot(collatz(n))
    
def stoptime(n):
    return len(collatz(n))-1

def stoptimeplot(n):
    x=list(range(1,n+1))
    y=[]
    for i in range(1,n+1):
        y.append(stoptime(i))
    plt.plot(x,y)
    plt.xlabel("n")
    plt.ylabel("stopping time σ(n)")
    plt.show

def maxexcurge(n):
    return max(collatz(n))

def maxexcurgeplot(n):
    x=list(range(1,n+1))
    y=[]
    for i in range(1,n+1):
        y.append(maxexcurge(i))
    plt.plot(x,y)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.show
    

def parity_sequence(n):
    seq=[]
    while n!=1:
        seq.append(n%2)
        if n%2==0:
            n//=2
        else:
            n=3*n+1
    seq.append(0)
    return seq

N=50  
maxlen=50
data=np.zeros((N,maxlen))
for i in range(1,N+1):
    p=parity_sequence(i)
    data[i-1,:len(p)]=p[:maxlen]

plt.imshow(data,cmap='binary',interpolation='none')
plt.xlabel("Step")
plt.ylabel("Starting number")
plt.show()


# ------ 

# Just pasted over for now will tweak later..

# Back to simulations of collatz sequence:

# For the plan for the project this will be used to
# complete part 1

N_values = [1000, 2000, 5000, 10000]

#from collatz_functions import collatz_simulations
# (idea for later)(will be incorporating it from one file to another)

def summary_values(N):
    n_val, stop_t, max_x = collatz_simulations(N)

    max_stopping = max(stop_t)
    n_at_max_stopping = n_val[stop_t.index(max_stopping)]

    max_exc = max(max_x)
    n_at_max_exc = n_val[max_x.index(max_exc)]

    avg_stopping = sum(stop_t) / len(stop_t)

    print("Maximum stopping time:", max_stopping, "at n =", n_at_max_stopping)
    print("Maximum excursion:", max_exc, "at n =", n_at_max_exc)
    print("Average stopping time:", avg_stopping)



import matplotlib.pyplot as plt

#from collatz_utils import collatz_simulations


def plot_stopping_time(N):
    ns, ts, _ = collatz_simulations(N)
    plt.figure()
    plt.plot(ns, ts)
    plt.xlabel("n")
    plt.ylabel("Total stopping time")
    plt.title(f"Total stopping time for 1 ≤ n ≤ {N}")
    plt.show()


def plot_max_excursion(N):
    ns, _, mx = collatz_simulations(N)
    plt.figure()
    plt.plot(ns, mx)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.yscale("log")
    plt.title(f"Maximum excursion for 1 ≤ n ≤ {N} (log scale)")
    plt.show()


if __name__ == "__main__":
    plot_stopping_time(2000)
    plot_max_excursion(2000)


# Can write about what find etc...

# suggestion:

running_max = []
current_max = 0

for t in stop_t:
    if t > current_max:
        current_max = t
    running_max.append(current_max)

for i, t in enumerate(stop_t):
    if t == max(stop_t[:i+1]):
        print("New record at n =", n_val[i], "with stopping time =", t)

