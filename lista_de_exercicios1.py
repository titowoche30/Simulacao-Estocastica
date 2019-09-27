import numpy as np

#%%
def quest12(n):
    n = 100
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
    n = 1000
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
def somatory():
	cont = 0
	u = np.random.rand()
	while u< np.exp(-3) : 
		u*=np.random.rand()
		cont+=1
		if cont == max:
			print('Nao convergiu')
			return -1

	print('CONT DA FUNCAO=',cont)
	return cont

#%%
def quest14(n):
    #text's random number sequence
    n = 14
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

#%%
##------------------------------CAP4-----------------------------##

def quest1(n):
    n = 100
    x = []
    for i in range(n):
        u = np.random.rand()
        if u<1/3:
            x.append(1)
        elif u<2/3:
            x.append(2)
            
    prop=(x.count(1))/len(x)
    print('proporcao de 1:',prop)

#%%    
def quest2(Pj):
    Pj = [0.4,0.3,0.2,0.1]
    n = 5
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
    print(amostras)
    return amostras
