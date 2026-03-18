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

#calculates the fraction of odd numbers in the parity sequence for a given starting number n
def parity_fraction(n):
    p=parity_sequence(n)
    return sum(p)/len(p)

def parity_fraction_graph(N):
    x=np.arange(1,N+1)
    y=[parity_fraction(n) for n in x]
    plt.plot(x,y)
    plt.xlabel("Starting number")
    plt.ylabel("Fraction of odd numbers in parity sequence")
    plt.title("Parity fraction for starting numbers 1 to "+str(N))
    plt.show()
    
parity_fraction_graph(512)

def max_excursion_record_sequence(N):
    record_sequence=[]
    record_n=[]
    current_record=1
    for n in range(1,N+1):
        max_excursion=maxexcurge(n)
        if max_excursion>current_record:
            record_n.append(n)
            current_record=max_excursion
            record_sequence.append((current_record))
    return record_sequence,record_n

def me_rs_graph(N):
    record_sequence,record_n=max_excursion_record_sequence(N)
    x=[n for n,excursion in record_sequence]
    y=[excursion for n,excursion in record_sequence]
    plt.plot(x,y,'o')
    plt.xlabel("Starting number")
    plt.ylabel("Maximum excursion")
    plt.title("Record maximum excursions for starting numbers 1 to "+str(N))
    plt.show()

def stopping_time_record_sequence(N):
    record_sequence=[]
    record_n=[]
    current_record=0
    for n in range(1,N+1):
        st=stoptime(n)
        if st>current_record:
            record_n.append(n)
            current_record=st
            record_sequence.append((current_record))
    return record_sequence,record_n

def st_rs_graph(N):
    record_sequence,record_n=stopping_time_record_sequence(N)
    x=[n for n,st in record_sequence]
    y=[st for n,st in record_sequence]
    plt.plot(x,y,'o')
    plt.xlabel("Starting number")
    plt.ylabel("Stopping time")
    plt.title("Record stopping times for starting numbers 1 to "+str(N))
    plt.show()