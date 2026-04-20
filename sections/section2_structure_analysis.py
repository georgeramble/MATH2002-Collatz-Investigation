### Section 2: Related sequences and further sequence analysis

## Import Python libraries:
import matplotlib.pyplot as plt
import numpy as np

# --- --- --- --- --- --- --- --- ---

## Core functions:

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


# ...

# --- --- --- --- --- --- --- --- ---

## Plots and outputs:

# ...