import sys
from tabuleiro import *

"""
Retorna a quantidade de iteracoes usadas para terminar
"""

def busca_gulosa( heuristica, tabuleiro ):
    estado_final = (heuristica(Tabuleiro()),Tabuleiro())

    candidatos = [ (heuristica(filho), filho) for filho in tabuleiro.filhos() ]
    encontrou = False
    passados = []
    iteracao = 0

    while encontrou == False:
        candidatos.sort(key= lambda x: x[0], reverse=True)
        iteracao += 1
        candidato = candidatos.pop()
        passados.append(candidato)

        if candidato == estado_final:
            encontrou = True
        else:
            novos_candidatos = [ (heuristica(filho), filho) for filho in candidato[1].filhos() ]
            for c in novos_candidatos:
                if c not in passados and c != candidato:
                    candidatos.append(c)


  
        #print( "candidato: {}\nlen(candidatos):{}\niteracao:{}\nlen(novos_candidatos):{}\nlen(passados){}".format(candidato,len(candidatos),iteracao,len(novos_candidatos), len(passados)) )
        #exec(input())

    return iteracao

