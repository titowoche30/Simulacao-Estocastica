import time
import numpy as np
import matplotlib.pyplot as plt

#AULA 5

#Primos entre si, mdc == 1
def mdc(a,b):
    while  a !=  0:
        a , b = b%a , a
    return b

#congruencial multiplicativo
def alea(x0,n):
    #m should be chosen to be a large prime number that can 
    #be fitted to the computer word size
    
    m = len(str(x0))                 #A semente tem m dígitos
    
    x = []
    x.append(x0)
    u = []
    u.append(x[0] / (10**m))
    
    i = 0
    while i<n:
        xi = (5*x[i] +7) % 200
        #xi = (3 * x[i]) % 150
        #xi = int( (x[i]**2) / (10**(m/2))) % (10**m)
        ui = xi / m
        #ui = xi / (10**m)
        x.append(xi)
        u.append(ui)
        i+=1
        
    print(x)
    print(u)                #Num aleatórios


#congruencial misto
def alea2(x0,a,b,m,n):
    #Comeca a repetir do m+1 pra frente
    x = []
    x.append(x0)
    u = []
    u.append(x[0]/m)
    
    i=0
    while i<n:
        xi = (a * x[i] + b) % m
        x.append(xi)
        ui = xi / m
        u.append(ui)
        
        i+=1

    print(x,'\n')
    print(u)

def alea2_teorema(x0,c,b,n):
    #m = 2**n , a = 4*c +1 , b = impar
    #ciclos de comprimento m
    
    a = 4*c +1
    #m = 2**n
    
    alea2(x0,a,b,32,n)
    


def simulated_pi(n,carlo):
    #x = np.random.rand(n)
    #y = np.random.rand(n)
    cont_carlo = 0
    pi = []
    
    while cont_carlo < carlo:
        np.random.seed(cont_carlo)
        x = np.random.rand(n)
        y = np.random.rand(n)
        cont = 0
        cont_iter = 0
        
        while cont<n:
            if x[cont]**2 + y[cont]**2 <= 1: 
                cont_iter+=1
            cont+=1
    
        cont_carlo+=1
        print('pi = ', 4 * (cont_iter/cont))
        pi.append(4 * (cont_iter/cont))
    
    print('Menor =',np.min(pi))
    print('Médio =',np.mean(pi))
    print('Maior =',np.max(pi))
    print('Desvio Padrao =',np.std(pi))    
    #return pi

#We can approximate an itegral by generating a large number of
#random numbers (ui) and taking as our approximation the average 
#value of g(ui )
def simulated_integral(f,n):
    #goal = 6.316563839
    #goal = 0.5890486225
    #goal = 93.162753292441
    #goal = 1/2
    goal = np.sqrt(np.pi)
    y = []
    #Ey = []
    
    for j in range(n):
        np.random.seed(j)
        u = np.random.rand(n)
        for i in range(n):
            #y.append(f(u[i]))
            #y.append(h(f,u[i]))
            #y.append(h1(f,u[i]))
             y.append(h2(f,u[i]))
        #Ey.append(np.mean(y))
        #print('valor da integral =',Ey[j])
     
    media = np.mean(y)
    #plotar(f,0,1)
    #print('\nMenor das Medias =',np.min(Ey))
    print('Goal = ',goal)
    print('Media das medias =',media)
    #print('Maior das Medias =',np.max(Ey))
    #print('Desvio Padrao das Medias =',np.std(Ey))
    print('\nGoal - Media =',goal - media)
    
    
    
def plotar(f,a,b):
    x = np.linspace(a,1.5,20)
    plt.figure(figsize=(8,8))
    plt.plot(x,f(x),color='purple')
    plt.axvline(x=b,color='red')
    plt.xlim(0,2)
    plt.ylim(a,20)
   
def f(x):
    #a,b = 0,1 
     return np.exp(-x**2)
    #return x*(1 + x**2)**(-2)
    #return np.exp(x+x**2)
    #return (1-x**2)**(3/2)
    #return np.exp(np.exp(x))

def h(f,y,a,b):
    #a,b= a,b
    
    return (b-a)*f(a+(b-a)*y)

def h1(f,y,a):
    #a,b = a,inf
    
    return f((1/y) -1 + a) / (y**2)

def h2(f,y,b):
    #a,b = -inf,b
    return f(1+b-(1/y)) / y**2 

def h3(f,y):
    #a,b = -inf,inf
    return h2(f,y,b = 0) + h1(f,y,a = 0)



alea(3,30)                  #Semente e qts numeros
#alea2(1,5,5,32,40)
#alea2(1,6,1,25,40)
#alea2_teorema(1,2,3,40)   
#simulated_pi(int(1e5),10000)
#t0 = time.time()
#simulated_integral(f,1000)    
#tf = time.time()
#print('Tempo = ',tf-t0,' segundos')
    