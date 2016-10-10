def pecas_fora_lugar( tabuleiro ):
	tabuleiro_final = [1,2,3,4,5,6,7,8,0]
	tabuleiro_incial = sum(tabuleiro.estado,[])
	qtd_fora = 0

	for i in range( len(tabuleiro_incial) ):
		if( tabuleiro_final[i] != tabuleiro_incial[i] ):
			qtd_fora += 1

	return qtd_fora

def distancia_manhattan( tabuleiro ):
	tabuleiro_final = [1,2,3,4,5,6,7,8,0]
	tabuleiro_inicial = sum(tabuleiro.estado,[])
	distancia = 0
	for i in tabuleiro_inicial:
		if i != 0: 
			indice_inicial = tabuleiro_inicial.index(i)
			indice_final = tabuleiro_final.index(i)
			if( indice_inicial != indice_final ):
				vetor_inicial = ( int(indice_inicial/3), indice_inicial%3 )
				vetor_final = ( int(indice_final/3), indice_final%3 )
				distancia += abs(vetor_final[0] - vetor_inicial[0]) + abs(vetor_final[1] - vetor_inicial[1])
	return distancia
