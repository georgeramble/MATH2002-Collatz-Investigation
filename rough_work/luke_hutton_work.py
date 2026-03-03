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

"""
git add .
git commit -m "add plotting functions / fix matplotlib import"
git pull --rebase
git push
"""