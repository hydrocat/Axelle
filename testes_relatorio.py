from algoritmos import *
from heuristicas import *
from tabuleiro import *

# t = Tabuleiro([[2,3,1],[0,5,6],[4,7,8]])


# ticks, passados, no_final = busca_largura(t)
# print(str.format("Gulosa Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", passados[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_gulosa(distancia_manhattan, t)
# print(str.format("Gulosa Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_gulosa(pecas_fora_lugar, t)
# print(str.format("Gulosa Fora do Lugar"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_estrela(distancia_manhattan, t)
# print(str.format("Estrela Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_estrela(pecas_fora_lugar, t)
# print(str.format("Estrela Fora do Lugar"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# print("----------------------------------------------")

t = Tabuleiro([[5,0,3],[4,8,2],[1,7,6]])
ticks, passados, no_final = busca_largura(t)
print(str.format("BFS"))
print(str.format("ticks: {0}", ticks))
print(str.format("nivel: {0}", passados[no_final][1]))
print(str.format("nos_totais: {0}", len(passados)))
print("")

# ticks, pai, passados, no_final = busca_gulosa(distancia_manhattan, t)
# print(str.format("Gulosa Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_gulosa(pecas_fora_lugar, t)
# print(str.format("Gulosa Fora do Lugar"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_estrela(distancia_manhattan, t)
# print(str.format("Estrela Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_estrela(pecas_fora_lugar, t)
# print(str.format("Estrela Fora do Lugar"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# print("----------------------------------------------")

# t = Tabuleiro([[1,5,6],[8,2,7],[3,0,4]])

# ticks, pai, passados, no_final = busca_gulosa(distancia_manhattan, t)
# print(str.format("Gulosa Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_gulosa(pecas_fora_lugar, t)
# print(str.format("Gulosa Fora do Lugar"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_estrela(distancia_manhattan, t)
# print(str.format("Estrela Manhatthan"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
# print("")

# ticks, pai, passados, no_final = busca_estrela(pecas_fora_lugar, t)
# print(str.format("Estrela Fora do Lugar"))
# print(str.format("ticks: {0}", ticks))
# print(str.format("nivel: {0}", pai[no_final][1]))
# print(str.format("nos_totais: {0}", len(passados)))
