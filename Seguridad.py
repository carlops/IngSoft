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
    ERcorreo = re.compile(r'\w(\w|_|\.|-)*@\w+\.\w+')
    ERclave = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-z]){3,15}.{8,16}$')
    Diccionario = {}
    def __init__(self):
        '''
        Constructor
        '''
    
    def registrarUsuario(self,correo,clave1,clave2):
        correoValido=False
        claveValida=False
        if (isinstance(correo,str)and(self.ERcorreo.match(correo))):
            #(re.match(r'\w(\w|_|\.|-)*@\w+\.\w+',correo)):
            correoValido=True
        else:
            print ("Direccion de correo electronico invalido")
        
        if ((isinstance(clave1, str))and(isinstance(clave2, str))and(clave1==clave2)):
            if self.ERclave.match(clave1):
                claveValida=True
        if not (claveValida):
            print("Clave invalida")
            
        if (claveValida and correoValido):
            claveCodificada=clave1[::-1]
            self.Diccionario[correo]=claveCodificada;
#            print(self.Diccionario)
            
    def AutenticarUsuario(self,correo,clave):
        correoValido=False
        claveValida=False
        print(self.Diccionario)
        print(correo)
        print(correo in self.Diccionario)
        if isinstance(correo,str) and self.ERcorreo.match(correo) and (correo in self.Diccionario):
            correoValido= True
            claveCodificada = self.Diccionario[correo]
            claveCodificada = claveCodificada[::-1]
            
            if isinstance(clave,str) and self.ERclave.match(clave) and claveCodificada==clave:
                claveValida = True

        if claveValida and correoValido:
            print("Usuario Aceptado")

        if correoValido and not claveValida:
            print("Clave invalida")

        if not correoValido:
            print("Correo invalido")
        print()