'''
Created on 31 ene. 2017

@author: luciod
'''

class Movimiento(object):
    '''
    Clase Movimiento, guarda informacion de cada movimiento
    '''
    def __init__(self, monto, fecha, idEstablecimiento):
        '''
        Constructor de la clase Movimiento
        '''
        self._monto = monto
        self.fecha = fecha
        self.idEstablecimiento = idEstablecimiento
    
    def monto(self):
        '''
        Get del atributo monto
        '''
        return self._monto

class Billetera(object):
    '''
    Clase Billetera, guarda toda la informacion de la billetera
    '''

    def __init__(self, ID, nombre, apellido, ci, pin):
        '''
        Constructor de la clase Billetera
        '''
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.pin = pin;
        self.creditos = []
        self.debitos = []
    
    def saldo(self):
        '''
        Metodo para obtener el saldo en una billetera
        '''
        saldo = 0
        for movimiento in self.creditos:
            saldo += movimiento.monto()
        for movimiento in self.debitos:
            saldo -= movimiento.monto()
        return saldo
        
    def recargar(self, monto, fecha, idEstablecimiento):
        '''
        Metodo para recargar saldo en una billetera
        '''
        assert (monto > 0), "Monto negativo"
        recarga = Movimiento(monto, fecha, idEstablecimiento)
        self.creditos.append(recarga)
    
    def consumir(self,monto, fecha, idEstablecimiento, pin):
        '''
        Metodo para consumir saldo en una billetera
        '''
        assert(self.pin == pin), "PIN incorrecto"
        assert(self.saldo() > monto), "Saldo insuficiente"
        consumo = Movimiento(monto, fecha, idEstablecimiento)
        self.debitos.append(consumo)