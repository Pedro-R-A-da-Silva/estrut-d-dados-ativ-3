#busca em profundidade
def DFS_VISIT(G, u, tempo):
    tempo += 1
    G[u]['d'] = tempo
    G[u]['cor'] = 'CINZA'

    # Processa as adjacências
    for v in G[u]['adjacencias']:
        if(G[v]['cor'] == 'BRANCO'):
            G[v]['pai'] = u
            tempo = DFS_VISIT(G, v, tempo)

    G[u]['cor'] = 'PRETO'
    tempo += 1
    G[u]['f'] = tempo
    return tempo

def ordenaçãoTopologica(G):
    ordem = list([])
    tempo = 0
    for u in G:
        G[u]['cor'] = 'BRANCO'
        G[u]['pai'] = None
    
    for u in G:
        if(G[u]['cor'] == 'BRANCO'):
            tempo = DFS_VISIT(G, u, tempo)
    
    return ordem

#Cria o grafo
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
ordem=ordenaçãoTopologica(G)

#Imprime o grafo para ver o resultado
print(ordem)