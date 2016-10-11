#!/usr/bin/env python2
import sys
import getopt
from algoritmos import *
from heuristicas import *
from tabuleiro import *

def usage():
	print("\nUso:")
	print("\tpython main.py -a estrela|guloso|largura|profundidade -h manhattan|pecas --tabuleiro=[[2,3,1], [0,5,6], [4,7,8]]")
	print("")

def main():
	funcoes_heuristicas = { 'manhattan': distancia_manhattan, 'pecas': pecas_fora_lugar  }
	funcoes_busca = { 'estrela': busca_estrela, 'guloso': busca_gulosa, 'largura': busca_largura, 'profundidade': busca_profundidade  }

	algoritmo = None
	heuristica = None
	tbl = []

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'a:h:t', ['algoritmo=', 'heuristica=', 'tabuleiro='])
	except getopt.GetoptError:
		usage()
	
	if len(opts) == 0:
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-a', '--algoritmo'):
			try:
				algoritmo = funcoes_busca[arg]	
			except KeyError:
				usage()
				sys.exit(2)
		elif opt in ('-h', '--heuristica'):
			try:
				heuristica = funcoes_heuristicas[arg]
			except KeyError:
				usage()
				sys.exit(2)
		elif opt in ('-t', '--tabuleiro'):
			try:
				lista = [int(y) for y in [x.replace('[','').replace(']','') for x in arg] if y != '' and y != ',']
			except ValueError:
				usage()
				sys.exit(2)

			if len(lista) != 9:
				usage()
				sys.exit(2)

			tbl.append(lista[0:3])
			tbl.append(lista[3:6])
			tbl.append(lista[6:9])

	t = Tabuleiro(tbl)
	if heuristica != None:
		ticks, pai, passados, no_final = algoritmo(heuristica, t)
	else:
		ticks, passados, no_final = algoritmo(t)
	
	print(str.format("ticks: {0}", ticks))
	if heuristica != None:	
		print(str.format("nivel: {0}", pai[no_final][1]))
	else:
		print(str.format("nivel: {0}", passados[no_final][1]))
	print(str.format("nos_totais: {0}", len(passados)))
	print("")

if __name__ == '__main__':
	main()
