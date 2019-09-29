import numpy as np
from geracaoVariaveisAleatorias import binominal,bernoulli


#%%
def permutacao(vetor):
    print('vetor inicial',vetor)
    k=len(vetor)
    
    while k!=1:
        u = np.random.rand()
        i = int(k*u)
        aux = vetor[i]
        vetor[i] = vetor[k-1]
        vetor[k-1] = aux
        #print('trocou {} com {}'.format(i,k-1))
        #print(vetor)
        k-=1
    print('vetor final',vetor)
    return vetor
#%%
##------------------------------CAP3-----------------------------##
def quest12(n):
    aux = []
    aux2 = []
    cont = 0
    
	##----LACO DA ESPERANCA-------##
    for k in range(int(n/2)):
		##-----GERA OS Ns DAQUI-----##
        for i in range(n):
            cont = 0
            u = 0
			##---FAZ O SOMATÓRIO DAQUI---##
            for j in range(int(n/2)):
                u+=np.random.rand()
                cont+=1
                if(u>1): break
            aux.append(cont)
			##----ATÉ AQUI---------------##
		##------ATÉ AQUI------------##	
        N = np.min(aux)
        aux2.append(N)
   
    print('valores de N=',aux2)
    return np.mean(aux2)
#%%
def quest13(n):
    #Ou vai de primeira, ou não vai	
    aux = []
    aux2 = []
    cont = 0
	
	##----LACO DA ESPERANCA-------##
    for k in range(int(n/2)):
		##-----GERA OS Ns DAQUI-----##
        for i in range(n):
            cont = 0
            cont = somatory(n)
            aux.append(cont)
		##------ATÉ AQUI---------##	
		#print('valores de aux=',aux)
        N = np.max(aux)
        aux2.append(N)

	#print('valores de N=',aux2)
    return np.mean(aux2)

#%%
def somatory(n):
	cont = 0
	u = np.random.rand()
	while u< np.exp(-3) : 
		u*=np.random.rand()
		cont+=1
		if cont == n:
			print('Nao convergiu')
			return -1

	print('Convergiu no =',cont)
	return cont

#%%
def quest14(n):
    #text's random number sequence
    u = []
    x = []
    x.append(23)
    x.append(66)
    for i in range(2,n+2):
        xn1 = x[i-1]
        xn2 = x[i-2]
        xn = (3*xn1 + 5*xn2)% 100
        x.append(xn)
        u.append(x[i-2] / 100)
        
    print('u=',u)
    return u

#%%
##------------------------------CAP4-----------------------------##

def quest1(n):
    x = []
    for i in range(n):
        u = np.random.rand()
        if u<1/3:
            x.append(1)
        elif u<2/3:
            x.append(2)
        else:
            x.append(3)
            
    prop=(x.count(1))/n
    print('proporcao de 1:',prop)
    return prop

#%%    
def quest2(Pj,n):
    m = len(Pj)
    np.random.seed(4)
    amostras = []
    for j in range(n):
        u = np.random.rand(n)
        x = []
        for i in range(n):
            if u[i]<= Pj[0]:
                #print('u = {} no x = {}'.format(u[i],1))
                x.append(1)
            else:
                for k in range(1,m+1):    
                    if u[i] <= sum(Pj[:k]):   
                        #print('u = {} no x = {}'.format(u[i],k))
                        x.append(k)
                        break
            
        amostras.append(x)
        print('Proporcoes=',props(x))
    print('amostras=',amostras)
    return amostras
#%%
def quest3(n):
    P = [0.3,0.2,0.35,0.15]
    u = np.random.rand(n)
    x = []
    for i in range(n):
        if u[i] <= P[2]:
            x.append(3)
        elif u[i] <= P[2] + P[0]:
            x.append(1)
        elif u[i] <= P[2] + P[0] + P[1]:
            x.append(2)
        else:
            x.append(4)
            
    print('Amostra=',x)
    print('Proporcoes=',props(x))
    return x
#%%
def props(amostra):
    one = np.unique(amostra)
    n = len(amostra)
    props = [(amostra.count(i)/n) for i in one]
    return props
#%%
def quest4(n,m):
    #X acertos em n=100 tentativas com p=1/100 de cada tentativa = binomial(n=100,p=1/100)
    amostras=binominal(n,1/n,m,False,False,False)
    p_bino = []
    var_bino = []
    for i in amostras:
        p_bino.append(np.mean(i))
        var_bino.append(np.std(i))
        
    print('esperanca de acertos com binomial simulada de {} amostras={}'.format(m,np.mean(p_bino)))
    print('variancia de acertos com binomial simulada de {} amostras={}'.format(m,np.mean(var_bino)))
    acertos = []
    
    #---Laco das amostras---##
    for j in range(m):
        baralho = list(range(1,101))
        np.random.shuffle(baralho)
        u = np.random.randint(1,101,n)
        
        n_acertos = len([i for i in range(n) if u[i] == baralho[i]])
        acertos.append(n_acertos)
        
    
    #print('acertos nas {} amostras = {}'.format(m,acertos))
    print('esperanca de acertos com {} amostras={}'.format(m,np.mean(acertos)))
    print('variancia de acertos com {} amostras={}'.format(m,np.std(acertos)))
    
#%%
def quest5(vetor):
    n = len(vetor)
    for i in range(n):
       vet = permutacao(vetor[:i+1])
       
    ind = np.random.randint(0,n-2)
    aux = vet[ind]
    vet[ind] = vet[n-1]
    vet[n-1] = aux
    
    return vet
#%%
def quest6(n,p):
    return bernoulli(n,p,1,False,False,False)
#%%
def quest7(n):
    n_lancamentos = []
    
    for i in range(n):
        k = 2
        cont = 0
        flag = True
        while flag:
            x = np.random.randint(1,7,2)
            if k==13:
                flag = False
            if sum(x) == k:
                k+=1
            cont+=1
        n_lancamentos.append(cont)
        
    print('n esperado de lancamentos necessarios',np.mean(n_lancamentos))
    

#%%
permutacao(list(range(15)))
#%%
#a
quest12(100)
#b
quest12(1000)
#c
quest12(1000)

#%%
quest13(100)
#%%
quest14(14)
#%%
#a
quest1(100)
#b
quest1(1000)
#c
quest1(1000)
#%%
quest2([0.4,0.3,0.2,0.1],100)
#%%
quest3(100)
#%%
quest4(100,10000)
#%%
quest5(list(range(15)))
#%%
quest6(25,0.8)
#%%
quest7(100)