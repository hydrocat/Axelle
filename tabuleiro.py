import copy

class Tabuleiro:
    def __init__ ( self, estado_inicial=[[1,2,3],[4,5,6],[7,8,0]] ):
        self.estado = estado_inicial

    def gerarEstados(self):
        lista = sum(self.estado, [] )
        """Metodo do Tabareu"""
        p = lista.index(0)
        TBRL = {}
        TBRL['t'] = p - 3
        TBRL['b'] = p + 3
        TBRL['r'] = p + 1 if (p+1)%3 > (p%3) else -1
        TBRL['l'] = p - 1 if (p-1)%3 < (p%3) else -1

        """
        Aplica restricao de intervalo
        0 <= T,B,R,L < 9
        """
        for tupla in TBRL.items():
            TBRL[tupla[0]] = tupla[1] if ( tupla[1] >= 0 and tupla[1] < 9 ) else -1

        """Cria lista de tabuleiros"""
        resultado = []
        for posicao in TBRL.values():
            if posicao > -1 :
                """Troca"""
                lista[p] = lista[posicao]
                lista[posicao] = 0
                """Monta a matriz"""
                matriz = [lista[:3],lista[3:6],lista[-3:]]
                resultado.append( Tabuleiro(estado_inicial=matriz) )
                """Destroca"""
                lista[posicao] = lista[p]
                lista[p] = 0

        return resultado

    def __str__(self):
        string = ''
        for linha in estado:
            string = string + str(linha) + '\n'
        return string
