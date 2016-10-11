import sys
import collections
from tabuleiro import *
from fila import *
try:
	from queue import Queue
except ImportError:
	from Queue import Queue

"""
Retorna a quantidade de ticks, o parentesco, os locais por onde passou
e o ultimo no
"""

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

	pai = {}
	pai[(heuristica(tabuleiro), tabuleiro)] = [None, 0]
	candidatos = [ (heuristica(tabuleiro), tabuleiro) ]
	encontrou = False
	passados = []
	tick = 0

	no_final = None

	while encontrou == False:
		candidatos.sort(key= lambda x: x[0], reverse=True)
		tick += 1
		candidato = candidatos.pop()
		passados.append(candidato)

		if candidato == estado_final:
			encontrou = True
			no_final = candidato
		else:
			novos_candidatos = [ (heuristica(filho), filho) for filho in candidato[1].filhos() ]
			for c in novos_candidatos:
				if c not in passados and c != candidato:
					candidatos.append(c)
					pai[c] = [candidato, pai[candidato][1] + 1]

	return tick, pai, passados, no_final

def busca_largura( tabuleiro ):
	candidatos = Queue()
	candidatos.put(tabuleiro)
	passados = {}
	passados[tabuleiro] = [None, 0]

	no_final = None
	estado_final = Tabuleiro()

	tick = 0
	while not candidatos.empty():
		candidato = candidatos.get()

		if candidato == estado_final:
			no_final = candidato
			break

		novos_candidatos = [ filho for filho in candidato.filhos()]
		for novo_candidato in novos_candidatos:
			if novo_candidato not in passados:
				candidatos.put(novo_candidato)
				passados[novo_candidato] = [candidato, passados[candidato][1] + 1]

		tick += 1

	return tick, passados, no_final

def busca_profundidade( tabuleiro ):
	candidatos = []
	candidatos.append(tabuleiro)
	passados = {}
	passados[tabuleiro] = [None, 0]

	encontrou = False

	no_final = None
	estado_final = Tabuleiro()

	tick = 0
	while not encontrou:
		candidato = candidatos.pop()

		if candidato == estado_final:
			encontrou = True
			no_final = candidato
			break
		
		novos_candidatos = [ filho for filho in candidato.filhos()]
		for novo_candidato in novos_candidatos:
			if novo_candidato not in passados:
				candidatos.append(novo_candidato)
				passados[novo_candidato] = [candidato, passados[candidato][1] + 1]

		tick += 1

	return tick, passados, no_final
