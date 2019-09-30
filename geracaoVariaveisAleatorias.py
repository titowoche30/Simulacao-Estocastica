import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##------------------GERACAO BERNOULLI(0,1)--------------------##
def bernoulli(m,n,p,printar=None,prob=None,plotar=None,ret=None):
    #Gera m sequencias de tamanho n de variaveis aleatorias de Bernoulli
    amostras = []
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
        amostras.append(X)
        
    if ret: return amostras
    
    if printar: print('{} amostras de {} variaveis bernoulli com p={}: {}'.format(n_amostras,n,p,amostras))        
    
    if prob:
        cont = 1
        for i in amostras:
            print('Amostra:',cont)
            print('Media da Bernoulli=',np.mean(i))
            print('Desvio Padrao da Bernoulli=',np.std(i),'\n')
            cont+=1


        amostrasFlat = [var for amostra in amostras for var in amostra]            
        print('Media de todas amostras=',np.mean(amostrasFlat))
        print('Desvio Padrao de todas amostras=',np.std(amostrasFlat))
            
    if plotar:
        bern = np.random.binomial(n=1,p=p,size=tam_amostras)
        plt.figure(figsize=(8,8))
        sns.distplot(bern,kde=False,bins=15,hist_kws={'alpha':1.0,
                                                      'weights': np.ones(len(bern)) / len(bern),
                                                      'edgecolor': 'white',
                                                      'linewidth': 1})
        plt.title('Bernoulli do numpy de tamanho {};p={}'.format(tam_amostras,p),fontdict={'fontsize': 15})
        plt.xlabel('x')
        plt.ylabel('P(X=x)')
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Bernoulli simulada com {} Amostras de tamanho {};p={}'.format(n_amostras,tam_amostras,p),y=1.05,fontsize=15)
        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('x')
               ax[i,j].set_ylabel('P(X=x)')
               ax[i,j].set_xticks([0,1])
               sns.distplot(amostras[i*n_plot+j],kde=False,bins=10,ax=ax[i,j],hist_kws={'alpha':1.0,
                                                                                      'weights': np.ones(len(amostras[i*n_plot+j])) / len(amostras[i*n_plot+j]),
                                                                                      'edgecolor': 'white',
                                                                                      'linewidth': 1})
               tam_amostras+=tam_amostras
    
        plt.show()

###--------------------------GERACAO POISSON-----------------------------##
def poisson(m,n,lamba,printar=None,prob=None,plotar=None,ret=None):        
    #Gera m sequencias de tamanho n de variaveis aleatorias de Poisson
    
    n_amostras = m
    tam_amostras = n
    n_plot = int(np.sqrt(n_amostras))
    amostras = []
    
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
        amostras.append(vet)
    
    if ret: return amostras
    
    if printar: print(n_amostras,'amostras de tamanho',tam_amostras,'de variaveis aleatorias da Poisson=',amostras)
    
    if prob:
        cont = 1
        for i in amostras:
            print('Amostra:',cont)
            print('Media da Poisson=',np.mean(i))
            print('Desvio Padrao da Poisson=',np.std(i),'\n')
            cont+=1


        amostrasFlat = [var for amostra in amostras for var in amostra]            
        print('Media de todas amostras=',np.mean(amostrasFlat))
        print('Desvio Padrao de todas amostras=',np.std(amostrasFlat))
            
            
    if plotar:
        pois = np.random.poisson(lam=lamba,size=tam_amostras)
        plt.figure(figsize=(8,8))
        sns.distplot(pois,kde=False,bins=15,hist_kws={'alpha':1.0,
                                                      'weights': np.ones(len(pois)) / len(pois),
                                                      'edgecolor': 'white',
                                                      'linewidth': 1})
    
        plt.title('Poisson do numpy de tamanho {};lambda={}'.format(tam_amostras,lamba),fontdict={'fontsize': 15})
        plt.xlabel('x')
        plt.ylabel('P(X=x)')
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Poisson simulada com {} Amostras de tamanho {};lamba={}'.format(n_amostras,tam_amostras,lamba),y=1.05,fontsize=15)
        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('x')
               ax[i,j].set_ylabel('P(X=x)')
               ax[i,j].set_xticks(np.unique(amostras[i*n_plot+j]))
               sns.distplot(amostras[i*n_plot+j],kde=False,bins=10,ax=ax[i,j],hist_kws={'alpha':1.0,
                                                                                      'weights': np.ones(len(amostras[i*n_plot+j])) / len(amostras[i*n_plot+j]),
                                                                                      'edgecolor': 'white',
                                                                                      'linewidth': 1})
               tam_amostras+=tam_amostras
        plt.show()
    
###-------------------GERACAO BINOMIAL------------------##
def binomial(m,n,p,printar=None,prob=None,plotar=None,ret=None):
    n_amostras = m
    tam_amostras = n              
    amostras = []
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
        amostras.append(vet)
    if ret: return amostras
    
    if printar: print(n_amostras,'amostras de tamanho',tam_amostras,'de variaveis aleatorias da binomial=',amostras)
    
    if prob:
        cont = 1
        for i in amostras:
            print('Amostra:',cont)
            print('Media da Binomial=',np.mean(i))
            print('Desvio Padrao da Binomial=',np.std(i),'\n')
            cont+=1


        amostrasFlat = [var for amostra in amostras for var in amostra]            
        print('Media de todas amostras=',np.mean(amostrasFlat))
        print('Desvio Padrao de todas amostras=',np.std(amostrasFlat))
    
    
    if plotar:
        bino = np.random.binomial(n,p,size=tam_amostras)
        plt.figure(figsize=(8,8))
        sns.distplot(bino,kde=False,bins=15,hist_kws={'alpha':1.0,
                                                      'weights': np.ones(len(bino)) / len(bino),
                                                      'edgecolor': 'white',
                                                      'linewidth': 1})
    
        plt.title('Binomial do numpy de tamanho {}; n={} e p={}'.format(tam_amostras,n,p),fontdict={'fontsize': 15})
        plt.xlabel('x')
        plt.ylabel('P(X=x)')
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Binomial simulada com {} Amostras de tamanho {}; n={} e p={}'.format(n_amostras,tam_amostras,n,p),y=1.05,fontsize=15)
        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('x')
               ax[i,j].set_ylabel('P(X=x)')
               #ax[i,j].set_xticks(np.unique(vetAux[i*n_plot+j]))
               sns.distplot(amostras[i*n_plot+j],kde=False,bins=10,ax=ax[i,j],hist_kws={'alpha':1.0,
                                                                                      'weights': np.ones(len(amostras[i*n_plot+j])) / len(amostras[i*n_plot+j]),
                                                                                      'edgecolor': 'white',
                                                                                      'linewidth': 1})
               tam_amostras+=tam_amostras
        
        plt.show()
def exponencial(m,n,lamba,printar=None,prob=None,plotar=None,ret=None):
    #m amostras de tamanho n
    amostras = []

    for i in range(m):
        Y = []
        for i in range(n):
            u = np.random.rand()
            Y.append(-(1/lamba)*np.log(u))
        
        amostras.append(Y)
        
    if ret: return amostras
     
    if printar: print(m,'amostras de tamanho',n,'de variaveis aleatorias da exponencial=',amostras)
    
    if prob:
        cont = 1
        for i in amostras:
            print('Amostra:',cont)
            print('Media da Exponencial =',np.mean(i))
            print('Desvio Padrao da Exponencial=',np.std(i),'\n')
            cont+=1


        amostrasFlat = [var for amostra in amostras for var in amostra]            
        print('Media de todas amostras=',np.mean(amostrasFlat))
        print('Desvio Padrao de todas amostras=',np.std(amostrasFlat))
        
    if plotar:
        n_plot = int(np.sqrt(m))
        expo = np.random.exponential(lamba,n)
        plt.figure(figsize=(8,8))
        sns.distplot(expo,kde=False,hist_kws={'alpha':1.0,
                                              'weights': np.ones(len(expo)) / len(expo),
                                              'edgecolor': 'white',
                                              'linewidth': 1})
    
        plt.title('Exponencial do numpy de tamanho {}; lambda={}'.format(n,lamba),fontdict={'fontsize': 15})
        plt.xlabel('x')
        plt.ylabel('P(X=x)')
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Exponencial simulada com {} Amostras de tamanho {}; lambda={}'.format(m,n,lamba),y=1.05,fontsize=15)
        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('x')
               ax[i,j].set_ylabel('P(X=x)')
               #ax[i,j].set_xticks(np.unique(vetAux[i*n_plot+j]))
               sns.distplot(amostras[i*n_plot+j],kde=False,ax=ax[i,j],hist_kws={'alpha':1.0,
                                                                                'weights': np.ones(len(amostras[i*n_plot+j])) / len(amostras[i*n_plot+j]),
                                                                                'edgecolor': 'white',
                                                                                'linewidth': 1})
               n+=n
     
        plt.show()
        
        
def normal(m,n,media,desvio_padrao,printar=None,prob=None,plotar=None,ret=None):
    #m amostras de tamanho n
    amostras = []
    
    for j in range(m):
        amostraZ = []
        amostraY = []    
        for i in range(n):
            u = np.random.rand(2)
            y1 = -(np.log(u[0]))
            y2 = -(np.log(u[1]))    
            if y2 - ((y1-1)**2)/2 >0:
                amostraY.append(y2 - ((y1-1)**2)/2)
                u0 = np.random.rand()
                if u0 <= 1/2:
                    amostraZ.append(media + desvio_padrao*y1)
                elif u0>1/2:
                    amostraZ.append(media + desvio_padrao*-y1)
    
        amostras.append(amostraZ)
    
    if ret: return amostras
    
    if printar: print(m,'amostras de tamanho',n,'de variaveis aleatorias da normal=',amostras)
    
    if prob:
        cont = 1
        for i in amostras:
            print('Amostra:',cont)
            print('Media da Normal =',np.mean(i))
            print('Desvio Padrao da Normal=',np.std(i),'\n')
            cont+=1


        amostrasFlat = [var for amostra in amostras for var in amostra]            
        print('Media de todas amostras=',np.mean(amostrasFlat))
        print('Desvio Padrao de todas amostras=',np.std(amostrasFlat))
        
    if plotar:
        n_plot = int(np.sqrt(m))
        norm = np.random.normal(0,1,size=n)
        plt.figure(figsize=(8,8))
        sns.distplot(norm,kde=False,hist_kws={'alpha':1.0,
                                              'weights': np.ones(len(norm)) / len(norm),
                                              'edgecolor': 'white',
                                              'linewidth': 1})
    
        plt.title('Normal do numpy de tamanho {}; media={} e desvio padrao={}'.format(n,media,desvio_padrao),fontdict={'fontsize': 15})
        plt.xlabel('x')
        plt.ylabel('P(X=x)')
        
        fig, ax = plt.subplots(nrows = n_plot, ncols = n_plot,constrained_layout=True,figsize=(10,8))
        fig.suptitle('Normal simulada com {} Amostras de tamanho {}; media={} e desvio padrao={}'.format(m,n,media,desvio_padrao),y=1.05,fontsize=15)
        for i in range(n_plot):
            for j in range(n_plot):
               ax[i,j].set_xlabel('x')
               ax[i,j].set_ylabel('P(X=x)')
               #ax[i,j].set_xticks(np.unique(vetAux[i*n_plot+j]))
               sns.distplot(amostras[i*n_plot+j],kde=False,ax=ax[i,j],hist_kws={'alpha':1.0,
                                                                                'weights': np.ones(len(amostras[i*n_plot+j])) / len(amostras[i*n_plot+j]),
                                                                                'edgecolor': 'white',
                                                                                'linewidth': 1})
               n+=n
        plt.show()
        
        
        
#np.random.seed(30)
#bernoulli(9,100,p=0.65,printar=False,prob=True,plotar=True,ret=False)
#poisson(9,100,lamba=0.5,printar=False,prob=True,plotar=True,ret=False)
#binominal(9,100,p=0.6,printar=False,prob=True,plotar=True,ret=False)
#normal(9,1000,media=4,desvio_padrao=0.37,printar=False,prob=True,plotar=True,ret=False)
#exponencial(9,100,lamba=0.5,printar=False,prob=True,plotar=True,ret=False)