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
    datos={}
    def __init__(self):
        '''
        Constructor
        '''
    
    def registrarUsuario(self,correo,clave1,clave2):
        correoValido=False
        claveValida=False
        if (re.match(r'\w(\w|_|\.|-)*@\w+\.\w+',correo)):
            correoValido=True
        else:
            print ("Dirección de correo electrónico inválido")
        
        if ((isinstance(clave1, str))and(isinstance(clave2, str))and(clave1==clave2)):
            if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-z]){3,15}.{8,16}$', clave1):
                claveValida=True
        if not (claveValida):
            print("Clave inválida")
            
        if (claveValida and correoValido):
            claveCodificada=clave1[::-1]
            self.datos[correo]=claveCodificada;
            print(self.datos)
            # meter en el diccionario
