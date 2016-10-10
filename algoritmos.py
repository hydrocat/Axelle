import sys
import collections
from tabuleiro import *
from fila import *


def busca_estrela( heuristica, tabuleiro ):
	candidatos = PriorityQueue()
	candidatos.put((heuristica(tabuleiro), tabuleiro), 0)
	pai = {}
	pai[(heuristica(tabuleiro), tabuleiro)] = [None, 0]
	passados = {}
	passados[(heuristica(tabuleiro), tabuleiro)] = 0

	no_final = None
	estado_final = (heuristica(Tabuleiro()),Tabuleiro())

	tick = 0
	while not candidatos.empty():
		candidato = candidatos.get()

		if candidato == estado_final:
			no_final = candidato
			break

		novos_candidatos = [(heuristica(filho), filho) for filho in candidato[1].filhos()]
		for novo_candidato in novos_candidatos:
			novo_custo = pai[candidato][1] + novo_candidato[0]
			if novo_candidato not in passados:
				passados[novo_candidato] = novo_custo
				prioridade = passados[novo_candidato]
				candidatos.put(novo_candidato, prioridade)
				pai[novo_candidato] = [candidato, pai[candidato][1] + 1]

		tick += 1

	return tick, pai, passados, no_final


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

