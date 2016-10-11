import unittest
from tabuleiro import *
from heuristicas import *
from algoritmos import *

class test_tabuleiro(unittest.TestCase):
    def setUp(self):
        "Tabuleiro Resolvido"
        self.tb_final = Tabuleiro()
        "Tabuleiro de Teste"
        self.tb_test = Tabuleiro([[0,8,3],[5,1,6],[4,7,2]])
        self.tb_test2 = Tabuleiro([[1,3,4],[2,0,5],[7,8,6]])

    def test_filhos_canto_superior(self):
        filhos = self.tb_test.filhos()
        self.assertIn([[8,0,3],[5,1,6],[4,7,2]], filhos)
        self.assertIn([[5,8,3],[0,1,6],[4,7,2]], filhos)

    def test_filhos_centro(self):
        filhos = self.tb_test2.filhos()
        self.assertIn([[1,3,4],[0,2,5],[7,8,6]], filhos)
        self.assertIn([[1,0,4],[2,3,5],[7,8,6]], filhos)
        self.assertIn([[1,3,4],[2,5,0],[7,8,6]], filhos)
        self.assertIn([[1,3,4],[2,8,5],[7,0,6]], filhos)

    def test_quantidade_filhos(self):
        filhos = self.tb_test2.filhos()
        self.assertEqual(4,len(filhos))

class test_heuristicas(unittest.TestCase):
    def setUp(self):
        "Tabuleiro Resolvido"
        self.tb_final = Tabuleiro()
        "Tabuleiro de Teste"
        self.tb_test = Tabuleiro([[0,8,3],[5,1,6],[4,7,2]])
        self.tb_test2 = Tabuleiro([[1,2,3],[4,5,6],[7,0,8]])

    def test_peca_fora_do_lugar(self):
        self.assertEqual( 7, pecas_fora_lugar(self.tb_test)  )

    def test_peca_fora_do_lugar2(self):
        self.assertEqual( 2, pecas_fora_lugar(self.tb_test2)  )

    def test_distancia_manhattan(self):
        self.assertEqual(10, distancia_manhattan(self.tb_test))

    def test_distancia_manhattan2(self):
        self.assertEqual(1, distancia_manhattan(self.tb_test2))

class test_algoritmo( unittest.TestCase ):
    def setUp(self):
        "Tabuleiro Resolvido"
        self.tb_final = Tabuleiro()
        "Tabuleiro de Teste"
        self.tb_test = Tabuleiro([[0,8,3],[5,1,6],[4,7,2]])

    def test_gulosa(self):
       iteracoes, pai, passado, final =  busca_gulosa(pecas_fora_lugar, self.tb_test) 
       self.assertEqual(iteracoes,641)


if __name__ == '__main__':
    unittest.main()


