afd = {}
estados = input()
for i in estados.split(' '):
    afd[i] = {}
sigma = input()
indice = int(input())
for i in range(indice):
    x = input()
    x = x.split(' ')
    if(x[1]not in afd[x[0]]): 
        afd[x[0]][x[1]] = x[2]       
estadoI = input() 
estadoF = input()
F = {}
for i in estadoF.split(' '):
    F[i] = 'finalstate'
palavras = input()
for palavra in palavras.split(' '):
    e = estadoI
    errostate = 0
    for char in palavra: # no pior caso o custo é O(W) onde W é o tamanho da palavra
        if(afd[e].get(char)): #nessa verificação o custo é O(1)
            e = afd[e][char]
        else:
            errostate = 1
            break
    if(F.get(e) and errostate == 0):#nessa verificação o custo do F.get(e) é O(1) pois é uma verificação direta no indice desejado
        print('S')
    else:
        print('N')
#para que o custo se conservasse O(W) uma tabela a estrutura escolhida foi tabela hash.