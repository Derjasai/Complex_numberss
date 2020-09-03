import unittest
import Funciones
import math


class unit_calculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(Funciones.suma_compleja((-6, 10), (15, -5)), (9, 5))

    def test_mult(self):
        self.assertEqual(Funciones.multiplicacion_compleja((-6, 10), (15, -5)), (-40, 180))

    def test_resta(self):
        self.assertEqual(Funciones.sustracion_compleja((-6, 10), (15, -5)), (-21, 15))

    def test_division(self):
        self.assertEqual(Funciones.division_compleja((-6, 10), (15, -5)), (-0.56, 0.48))

    def test_modulo(self):
        self.assertEqual(Funciones.modulo((-3, 4)), 5)
        self.assertEqual(Funciones.modulo((-3, -4)), 5)
        self.assertEqual(Funciones.modulo((3, 4)), 5)
        self.assertEqual(Funciones.modulo((3, -4)), 5)

    def test_conjugado(self):
        self.assertEqual(Funciones.conjugado((-45, -10)), (-45, 10))

    def test_polarcart(self):
        self.assertEqual(Funciones.polar_a_carte((math.sqrt(2), (math.pi*3)/4)), (-1.0, 1.0))

    def test_cartepoalr(self):
        self.assertEqual(Funciones.carte_a_polar((-1.0, 1.0)), (math.sqrt(2), 135.0))
        self.assertEqual(Funciones.carte_a_polar((2.0, 1.0)), (math.sqrt(5), 26.56505117707799))
        self.assertEqual(Funciones.carte_a_polar((-3.0, -4.0)), (5, 233.13010235415598))

    def test_fase(self):
        self.assertEqual(Funciones.fase_compleja((-5/math.sqrt(2), 1/math.sqrt(2))), 111.80140948635182)
        self.assertEqual(Funciones.fase_compleja((6, -15)), 291.8014094863518)
        self.assertEqual(Funciones.fase_compleja((6, 15)), 68.19859051364818)
        self.assertEqual(Funciones.fase_compleja((-6, -15)), 248.19859051364818)

    def test_suma_vectores(self):
        self.assertEqual(Funciones.suma_vectores_complejos([9+7j, 11+0j, 14-18j], [6+3j, 3+1j, 10-8j]),
                         [(15+10j), (14+1j), (24-26j)])

    def test_vector_inverso(self):
        self.assertEqual(Funciones.inverso_vector([9+7j, -4j, 14-18j]), [(-9-7j), 4j, (-14+18j)])

    def test_vectorxescalar(self):
        self.assertEqual(Funciones.vectorxescalar([(-9-7j), (-11+0j), (-14+18j)], 4), [(-36-28j), (-44+0j), (-56+72j)])

    def test_suma_matriz(self):
        self.assertEqual(Funciones.suma_matrices_complex([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]],
                                                         [[6+3j, 3+1j, 10-8j], [-8j, 4+10j, 2-1j]]),
                         [[(10+11j), (10+2j), (18-4j)], [-4j, (4+16j), (9-9j)]])

    def test_matriz_inversa(self):
        self.assertEqual(Funciones.inverso_matriz([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(-4-8j), (-7-1j), (-8-4j)], [(-0-4j), (-0-6j), (-7+8j)]])

    def test_matrizxescalar(self):
        self.assertEqual(Funciones.matrizxescalar([[6+3j, 3+1j, 10-8j], [-8j, 4+10j, 2-1j]], 4),
                         [[(24+12j), (12+4j), (40-32j)], [-32j, (16+40j), (8-4j)]])

    def test_transpuesta(self):
        self.assertEqual(Funciones.transponer([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(4+8j), 4j], [(7+1j), 6j], [(8+4j), (7-8j)]])

    def test_conjugar(self):
        self.assertEqual(Funciones.conjugar([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(4-8j), (7-1j), (8-4j)], [-4j, -6j, (7+8j)]])

    def test_adjunta(self):
        self.assertEqual(Funciones.matriz_adjunta([[4+8j, 7+1j, 8+4j], [4j, 6j, 7-8j]]),
                         [[(4-8j), -4j], [(7-1j), -6j], [(8-4j), (7+8j)]])

    def test_multiplicacion(self):
        self.assertEqual(Funciones.matrizxmatriz([[4+8j, 4j, 8-3j], [7+1j, 6j, 4+5j], [8+4j, 7-8j, 10]],
                                                 [[6+3j, -8j, 5], [3+1j, 4+10j, 9j], [10-8j, 2-1j, 10+4.5j]]),
                         [[(52-22j), (37-30j), (77.5+46j)], [(113+63j), (-39-26j), (-1.5+73j)], [(165-49j), (160-36j),
                                                                                                 (212+128j)]])

    def test_productointerno(self):
        self.assertEqual(Funciones.producto_interno_vector([4+8j, 4j, 8-3j], [8+4j, 7-8j, 10]), (112-46j))

    def test_norma_vector(self):
        self.assertEqual(Funciones.norma([(4, 5), (3, 1), (0, -7)]), 10.0)

    def test_distancia(self):
        self.assertEqual(Funciones.distancia_vecotres([(3, 8), (5, -2), (8, -10)], [(8, 9), (3, -7), (6, 14)]),
                         25.199206336708304)

    def test_hermitania(self):
        self.assertEqual(Funciones.ishermitiana([[(3+0j),(2-1j),(-3j)],[(2+1j),(0+0j),(1-1j)],[(0+3j),(1+1j),(0+0j)]]),True)


unittest.main()
