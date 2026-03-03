def validate_input(n):
    # Checks if input is valid
    
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n<=0:
        raise ValueError("n must be positive")


    
def one_step(n):
    # Does one step of the Collatz seq
    
    validate_input(n)

    if n%2==0:
        return n//2
    else:
        return 3*n+1
    

    
def collatz_sequence(n):
    # Start a Collatz sequence from n

    validate_input(n)

    seq = [n]

    while seq[-1]!=1:
        seq.append(one_step(seq[-1]))
    return seq



def total_stopping_time(n):
    # Number of steps needed to reach 1

    return len(collatz_sequence(n))-1



def max_excursion(n):
    # Maximum value reached in the sequence

    return max(collatz_sequence(n))



def collatz_simulations(N):
    # Run Collatz simulations for 1<=n<=N
    # Returns three seperate lists

    validate_input(N)

    starting_values = []
    stopping_times = []
    max_values = []

    for n in range(1, N+1):
        seq = collatz_sequence(n)
        
        starting_values.append(n)
        stopping_times.append(len(seq) - 1)
        max_values.append(max(seq))

    return starting_values, stopping_times, max_values