INF = 65536
def BFS(G, s):
    for u in G:
        G[u]["cor"] = 'BRANCO'
        G[u]["d"]   = INF
        G[u]["pai"] = None
    
    G[s]["cor"] = 'CINZA'
    G[s]['d']   =   0

    Q = list([])
    Q.append(s)
    while(len(Q)>0):
        u = Q.pop(0)
        for v in G[u]['adjacencias']:
            if (G[v]['cor'] == 'BRANCO'):
                G[v]['cor'] = 'CINZA'
                G[v]['d'] = G[u]['d']+1
                G[v]['pai'] = u
                Q.append(v)
        G[u]['cor']='PRETO'

    return G[u]["pai"]


G = {}

print("Implementação exemplo da DFS")

# Esta entrada de dados é para um grafo dirigido
# para um grafo não dirigido deve usar a entrada
# da busca em profundidade

# Leia até não ter mais nada para ler
linha = input("aqui:")
while(linha != ""):
        lista = linha.split(" ")
        v1    = lista[0]
        if(len(lista) == 1):
                if(v1 not in G):
                        G[v1] = {'adjacencias':[]}
        else:
                v2 = lista[1]
                if(v1 not in G):
                        G[v1] = {'adjacencias':[v2]}
                else:
                        G[v1]['adjacencias'].append(v2)
                if(v2 not in G):
                    G[v2] = {'adjacencias':[]}
        linha = input()
#Chegou aqui o grafo está montado. Agora é chamar o DFS
#Imprime o grafo para ver o resultado
s=input("seacher:")
ordem=BFS(G,s)
print(ordem)