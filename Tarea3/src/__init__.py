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
    
        
               
if __name__ == '__main__':
    unittest.main()