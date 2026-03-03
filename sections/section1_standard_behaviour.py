import matplotlib.pyplot as plt
import numpy as np

from core_lib.collatz_functions import collatz_simulations



N_values = [1000, 2000, 5000, 10000]



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



def plot_stopping_time(N):
    n_val, stop_t, max_x = collatz_simulations(N)
    plt.figure()
    plt.plot(n_val, stop_t)
    plt.xlabel("n")
    plt.ylabel("Total stopping time")
    plt.title(f"Total stopping time for 1 ≤ n ≤ {N}")
    plt.show()



def plot_max_excursion(N):
    n_val, stop_t, max_x = collatz_simulations(N)
    plt.figure()
    plt.plot(n_val, max_x)
    plt.xlabel("n")
    plt.ylabel("Maximum excursion")
    plt.yscale("log")
    plt.title(f"Maximum excursion for 1 ≤ n ≤ {N} (log scale)")
    plt.show()


if __name__ == "__main__":
    plot_stopping_time(2000)
    plot_max_excursion(2000)

def collatz(n):
    seq=[n]
    while seq[-1]!=1:
        if seq[-1]%2==0:
            seq.append((seq[-1])//2)
        else:
            seq.append((3*seq[-1])+1)
    return seq

def stoptime(n):
    return len(collatz(n))-1

def maxexcurge(n):
    return max(collatz(n))


    """Maximum excursion and Stopping time on the same plot"""
def mestplot(n):
    x=list(range(1,n+1))
    y=[]  
    for i in range(1,n+1):
        y.append(stoptime(i))
    q=[]
    for i in range(1,n+1):
        q.append(maxexcurge(i))
    plt.plot(x,y,label="stopping time")
    plt.plot(x,q,label="Max excursion")
    plt.xlabel("n")
    plt.legend()
    plt.show

def correlationplot(n):
    x=[]
    for i in range(1,n+1):
        x.append(stoptime(i))
    y=[]
    for i in range(1,n+1):
        y.append(maxexcurge(i))
    m,c=np.polyfit(x,y,1)
    p=np.linspace(min(x),max(x),100)
    q=m*p+c
    plt.plot(p,q,color="red",label="Regression line")
    plt.xlabel("Stopping time")
    plt.ylabel("Max excursion")
    plt.scatter(x,y)
    plt.show()