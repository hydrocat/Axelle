import sys
import collections
from tabuleiro import *
try:
	from Queue import PriorityQueue
except ImportError:
	from queue import PriorityQueue


def busca_estrela( heuristica, tabuleiro ):
	estado_final = (heuristica(Tabuleiro()),Tabuleiro())
	encontrou = False

	chaves = [ 'custo', 'tabuleiro' ]
	candidatos = PriorityQueue()
	candidatos.put((heuristica(tabuleiro), tabuleiro), 0)
	pai = {}
	custo_ate = {}
	custo_ate[(heuristica(tabuleiro), tabuleiro)] = heuristica(tabuleiro)
	pai[(heuristica(tabuleiro), tabuleiro)] = [None, 0]


	candidatos_passados = PriorityQueue()

	iteracao = 0

	while not candidatos.empty():
		candidato = candidatos.get()

		print(candidato)

		if candidato == estado_final:
			break

		print(candidato)
		novos_candidatos = [(heuristica(filho), filho) for filho in candidato[1].filhos()]
		for novo_candidato in novos_candidatos:
			novo_custo = custo_ate[candidato] + novo_candidato[0] + iteracao
			if (novo_candidato not in custo_ate or novo_custo < custo_ate[novo_candidato]) and candidato != novo_candidato:
				if novo_candidato in custo_ate:
					print(str.format("novo: {0} - velho: {1}", novo_custo, custo_ate[novo_candidato]))
				custo_ate[novo_candidato] = novo_custo
				# prioridade = novo_custo + heuristica(novo_candidato[1])
				prioridade = novo_custo + pai[candidato][1] 
				candidatos.put(novo_candidato, prioridade)
				pai[novo_candidato] = [candidato, pai[candidato][1] + 1]

		iteracao+=1
	
	return iteracao
	# return iteracao, pai, custo_ate


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

