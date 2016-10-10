import sys
import collections
from tabuleiro import *


def busca_estrela( heuristica, tabuleiro ):
	estado_final = (heuristica(Tabuleiro()),Tabuleiro())
	encontrou = False

	candidatos = [ (heuristica(tabuleiro), tabuleiro, 0) ]
	passados = []

	iteracao = 0


	while encontrou == False:
		candidatos.sort(key= lambda x: x[0], reverse=True)
		if( len(candidatos) > 0 ):
			candidato = candidatos.pop()
		passados.append(candidato)

		if candidato == estado_final:
			encontrou = True
		else:
			novos_candidatos = [( heuristica(filho) + candidato[2] + 1, filho, candidato[2] + 1) for filho in candidato[1].filhos()]
			for novo_candidato in novos_candidatos:
				ja_foi_passado = filter( lambda x: x[1] == novo_candidato[1], passados )
				candidato_passado = [ x for x in passados if x[1] == novo_candidato[1] ]
				if ( len(ja_foi_passado) == 0 or (len(candidato_passado) > 0 and novo_candidato[0] < candidato_passado[0])) and novo_candidato != candidato:
					novo_candidato[0] += heuristica(novo_candidato[1])
					candidatos.append(novo_candidato)

		iteracao += 1

	return iteracao


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

