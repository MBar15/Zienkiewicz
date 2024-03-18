import numpy as np


L = 100e1
A = 2e2
E = 10**5
P = 2e3
b = -0.25e2

def Al(x,L,A):
    return A + A*x/L

exact = -0.03142513e1

N = 4

KG = np.zeros((N+1,N+1))
BG = np.zeros((N+1,1))
h = L/N

for i in range(N):
    #ke = E*A*(1/h + (2+2*i-1)/2/L) * np.array([[1,-1],[-1,1]]) #zienkiwicyovo
    ke = E*Al(h/2+i*h,L,A)/h * np.array([[1,-1],[-1,1]])   # moje
    be = b*h/2 * np.array([[1],[1]])

    KG[i:i+2,i:i+2] += ke
    BG[i:i+2] += be

KG = KG[0:N,0:N]
BG[0] += P
BG = BG[0:N]

sol = np.linalg.inv(KG)@BG
index = N//2
print(sol)
