import numpy as np
import matplotlib.pyplot as plt
def fourier_syn(sig, a0, an, m, N, xL, xR):
    X = np.linspace(xL,xR,N)
    plt.subplot(2,1,1)
    plt.plot(X,[sig()(x) for x in X],color='green')
    plt.title('Original signal')
    

    fourier = np.zeros(X.size,dtype=complex)
    fourier+= a0
    E = lambda n,t:np.exp(1j*n*t*np.pi)
    for n in range(-m,m+1):
        if n ==0:
            continue
        fourier+= eval(an)*E(n,X)
    plt.subplot(2,1,2)
    plt.title('Fourier')
    plt.plot(X,fourier)
        
    
    plt.show()
  
  
  
def sig():
    
    return lambda x: 0 if (x%2 >= 1 and x%2<=2) else np.exp(x%2)
    
def main():
    a0 = (np.exp(1) -1)/2
    an = '(pow(-1,n)*np.e-1)/(2*(-1j*n*np.pi+1))'
    fourier_syn(sig , a0,an,200,10000,-2,8)
main()
