'''
Created on 28 ene. 2017

@author: luciod
'''
import unittest
from datetime import datetime
from src.Billetera import *

class PruebaBilletera(unittest.TestCase):
    
    def testRecargar(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
        self.assertEqual(b.saldo(),100)
    
    def testConsumir(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
        b.consumir(25, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1, 1234)
        self.assertEqual(b.saldo(), 75, )
    
    def testDebitoConPinIncorrecto(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
        with self.assertRaises(Exception):
            b.consumir(25, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1, 1235)        
    
    def testSaldoInsuficiente(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
        with self.assertRaises(Exception):
            b.consumir(125, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1, 1234)
    
    def testRecargasMultiples(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        for i in range (50):
            b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
        self.assertEqual(b.saldo(),5000)

    def testConsumosMultiples(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        for i in range (50):
            b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
        self.assertEqual(b.saldo(),5000)
        for i in range (50):
            b.consumir(25, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1, 1234)        
        self.assertEqual(b.saldo(),3750)
        
    def testConsumosYRecargas(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        for i in range (50):
            b.recargar(100, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)
            b.consumir(25, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1, 1234)
        self.assertEqual(b.saldo(),3750)
    
    def testRecargaNegativa(self):
        b = Billetera(1, "Pedro", "Perez", 7573920, 1234)
        with self.assertRaises(Exception):
            b.recargar(-23, datetime.strptime("07/27/2012", "%m/%d/%Y"), 1)        
               
if __name__ == '__main__':
    unittest.main()