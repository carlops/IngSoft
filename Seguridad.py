'''
Created on 1 Oct 2014

@authors: Carlo Polisano S
          Alejandro Guevara
'''
import re

class clsSeguridad(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def registrarUsuario(self,correo,clave1,clave2):
        correoValido=False
        claveValida=False
        if (re.match(r'\w(\w|_|\.|-)+@\w+\.\w+',correo)):
            correoValido=True
        if ((isinstance(clave1, str))and(isinstance(clave2, str))and(clave1.equal(clave2))):
            claveValida=True
        if not (claveValida):
            print ("Dirección de correo electrónico inválido")
        if not (correoValido):
            print("Clave inválida")
        if (claveValida and correoValido):
            claveCodificada=clave1.reverse()
            # meter en el diccionario
        