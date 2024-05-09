import unittest

def Calcular_mcd_dos_numeros(nro1, nro2):
    while(nro2):
            nro1, nro2 = nro2, nro1 % nro2
    return nro1

def Calcular_mcd_cuatro_numeros(nro1, nro2, nro3, nro4):
    mcd_nro1_nro2 = Calcular_mcd_dos_numeros(nro1, nro2)  
    mcd_nro3_nro4 = Calcular_mcd_dos_numeros(nro3, nro4) 
    return Calcular_mcd_dos_numeros(mcd_nro1_nro2, mcd_nro3_nro4)


class TestCalcular_mcd_cuatro_numeros(unittest.TestCase):
    def test_Calcular_mcd_cuatro_numeros(self):
        self.assertEqual(Calcular_mcd_cuatro_numeros(12, 24, 36, 48), 12)
        self.assertEqual(Calcular_mcd_cuatro_numeros(15, 30, 45, 60), 15)
        self.assertEqual(Calcular_mcd_cuatro_numeros(18, 36, 54, 72), 18)
        self.assertEqual(Calcular_mcd_cuatro_numeros(7, 14, 21, 28), 7)

if __name__ == '__main__':
    unittest.main()
