import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
plt.style.use('seaborn')
plt.rcParams.update({'font.size': 12})


##------------------GERACAO BERNOULLI(0,1)--------------------##
def bernoulli(n,p,m,printar,prob,plotar):
    #Gera n_amostras sequencias de tamanho n de variaveis aleatorias de Bernoulli
    vetAux = []
    n_amostras = m
    tam_amostras = n
    n_plot = int(np.sqrt(n_amostras))
    
    for j in range(n_amostras):
        X = []
        i = 0
        u = np.random.rand()
        
        #-----A sequência de variaveis aleatorias é gerada daqui------#
        while i<n:
            if u <= p:
                X.append(1)
            else:
                X.append(0)
           
            if i == n:
                break
        
            if u<=p:
                u = u/p
            else:
                u = (u-p)/(1-p)           
            i+=1    
        #---------------------------Até aqui-------------------------#
        vetAux.append(X)
    #return vetAux
    
    if printar: print('{} amostras de {} variaveis bernoulli com p={}: {}'.format(n_amostras,n,p,vetAux))        
    
    if prob:
        for i in range(n_amostras):
            print('Amostra',i+1,'\n')
            prob1=vetAux[i].count(1)
            print('P(X=1)=',prob1 / n)
            print('P(X=0)=',abs(1-(prob1/n)))
            print('---------------------------')
            
    if plotar:
        bern = np.random.binomial(n=1,p=p,size=tam_amostras)
    
        plt.figure(figsize=(10,8))
        plt.title('Bernoulli do numpy de tamanho {};p={}'.format(tam_amostras,p),fontdict={'fontsize': 15})
        plt.xlabel('X')
        plt.ylabel('P(X=x)')
        
        plt.hist(bern,weights=np.ones(len(bern)) / len(bern),edgecolor='white',linewidth=1)
        plt.gca().yaxis.set_major_formatter(ScalarFormatter())
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Bernoulli simulada com {} Amostras de tamanho {};p={}'.format(n_amostras,tam_amostras,p),y=1.05,fontsize=15)

        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('X')
               ax[i,j].set_ylabel('P(X=x)')
               ax[i,j].set_xticks([0,1])
               ax[i,j].hist(vetAux[i*n_plot+j], weights=np.ones(len(vetAux[i*n_plot+j])) / len(vetAux[i*n_plot+j]),edgecolor='white',linewidth=1)
               plt.gca().yaxis.set_major_formatter(ScalarFormatter())
               
               tam_amostras+=tam_amostras
    

###--------------------------GERACAO POISSON-----------------------------##
def poisson(lamba,n,m,printar,prob,plotar):        
    #Gera n_amostras sequencias de tamanho n de variaveis aleatorias de Poisson
    #1 numero aleatorio pra cada numero de poisson
    
    n_amostras = m
    tam_amostras = n
    n_plot = int(np.sqrt(n_amostras))
    vetAux = []
    
    for k in range(n_amostras):
        vet = []
        for i in range(tam_amostras):
            ##----A variavel aleatoria de Poisson é gerada daqui-----#
            I = 0
            u = np.random.rand()
            p = np.exp(-lamba)
            F = p
            while u>=F:
                p = (lamba*p) / (I+1)
                F = F + p
                I+=1
            ##--------------------Até aqui---------------------------#    
            vet.append(I)    
        vetAux.append(vet)
    
    if printar: print('vetAux=',vetAux)
    
    if prob:
        n = max([max(i) for i in vetAux])
        
        for i in range(n_amostras):
            print('Amostra',i+1,'\n')
            for j in range(n):
                proba=vetAux[i].count(j)
                print('P(X={})={}'.format(j, proba / tam_amostras ))
            print('---------------------------')
            
            
    if plotar:
        pois = np.random.poisson(lam=lamba,size=tam_amostras)
        
        plt.figure(figsize=(10,8))
        plt.title('Poisson do numpy de tamanho {};lambda={}'.format(tam_amostras,lamba),fontdict={'fontsize': 15})
        plt.xlabel('X')
        plt.ylabel('P(X=x)')
        
        plt.hist(pois,weights=np.ones(len(pois)) / len(pois),edgecolor='white',linewidth=1)
        plt.gca().yaxis.set_major_formatter(ScalarFormatter())
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Poisson simulada com {} amostras de tamanho {};lambda={}'.format(n_amostras,tam_amostras,lamba),y=1.05,fontsize=15)

        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('X')
               ax[i,j].set_ylabel('P(X=x)')
               ax[i,j].set_xticks( np.unique(vetAux[i*n_plot+j]))
               
               ax[i,j].hist(vetAux[i*n_plot+j], weights=np.ones(len(vetAux[i*n_plot+j])) / len(vetAux[i*n_plot+j]),edgecolor='white',linewidth=1 )
               plt.gca().yaxis.set_major_formatter(ScalarFormatter())
               
               tam_amostras+=tam_amostras        
    
    
###-------------------GERACAO BINOMIAL------------------##
def binominal(n,p,m,printar,prob,plotar):
    n_amostras = m
    tam_amostras = n              
    vetAux = []
    n_plot = int(np.sqrt(n_amostras))
    
    for k in range(n_amostras):
        vet = []        
        for i in range(tam_amostras):
            ##----A variavel aleatoria Binomial é gerada daqui-----#
            u = np.random.rand()
            c = p / (1-p)
            pr = (1-p)**n
            F = pr
            i = 0
            while u>=F:
                pr = (( c*(n-i) )/ (i+1)) * pr
                F = F + pr
                i+=1
            ##--------------------Até aqui---------------------------#    
            vet.append(i)    
        vetAux.append(vet)
    #return vetAux
    
    if printar: print(n_amostras,'amostras de tamanho',tam_amostras,'de variaveis aleatorias da binomial=',vetAux)
    
    if prob:
        for i in range(n_amostras):
            print('Amostra',i+1,'\n')
            for j in range(n):
                proba=vetAux[i].count(j)
                print('P(X={})={}'.format(j, proba / tam_amostras ))
            print('---------------------------')
    
    
    if plotar:
        bino = np.random.binomial(n,p,size=tam_amostras)
        
        plt.figure(figsize=(10,8))
        plt.title('Binomial do numpy de tamanho {}; n={} e p={}'.format(tam_amostras,n,p),fontdict={'fontsize': 15})
        plt.xlabel('X')
        plt.ylabel('P(X=x)')
        
        plt.hist(bino,weights=np.ones(len(bino)) / len(bino),edgecolor='white',linewidth=1)
        plt.gca().yaxis.set_major_formatter(ScalarFormatter())
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Binomial simulada com {} Amostras de tamanho {}; n={} e p={}'.format(n_amostras,tam_amostras,n,p),y=1.05,fontsize=15)

        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('X')
               ax[i,j].set_ylabel('P(X=x)')
               ax[i,j].set_xticks( np.unique(vetAux[i*n_plot+j]))
               ax[i,j].hist(vetAux[i*n_plot+j], weights=np.ones(len(vetAux[i*n_plot+j])) / len(vetAux[i*n_plot+j]),edgecolor='white',linewidth=1)
               plt.gca().yaxis.set_major_formatter(ScalarFormatter())
               
               tam_amostras+=tam_amostras
            
            
 
    
#np.random.seed(30)
#bernoulli(100,0.65,25,False,False,True)
#poisson(2.75,5,10,False,False,True)
#binominal(5,0.6,100,False,False,True)
