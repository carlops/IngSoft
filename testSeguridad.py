'''
Created on 1 Oct 2014

@authors: Carlo Polisano S
          Alejandro Guevara
'''
import unittest
from Seguridad import clsSeguridad

seg=clsSeguridad()

class Test(unittest.TestCase):

    def testRegistroIni(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario(None,None,None))
        
    def testRegistroClaveLong7(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","a123Abc","a123Abc"))
        
    def testRegistroClaveLong8(self):
        # Corrio a la primera
        self.assertEqual(True,seg.registrarUsuario("jonblah@mail.com","a123Abcd","a123Abcd"))

    def testRegistroClaveLong16(self):
        # Corrio a la primera
        self.assertEqual(True,seg.registrarUsuario("jonblah@mail.com","a123Abcda123Abcd","a123Abcda123Abcd"))
        
    def testRegistroClaveLong17(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","ba123Abcdba123Abc","ba123Abcdba123Abc"))
        
    def testRegistroClaveSinNumeros(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","aBCDEabcd","aBCDEabcd"))
        
    def testRegistroClaveSinMayus(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","a123abcd","a123abcd"))
        
    def testRegistroClaveSinMinus(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","A123ABCD","A123ABCD"))
        
    def testRegistroClaveCaracterEspecial(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","a123ab+cd","a123ab+cd"))
        
    def testRegistroClaveSinLetras(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","012345678","012345678"))
        
    def testRegistroClaveUnaLetra(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","a12345678","a12345678"))
        
    def testRegistroClaveUnaMayusUnaMinus(self):
        # No funciono a la primera y hubo que realizar una modificacion a la expresion regular
        # que verifica las contrasena. Y al segundo intento si funciono
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","a123B4567","a123B4567"))
        
    def testRegistroClaveDosMayusUnaMinus(self):
        # Corrio a la primera
        self.assertEqual(True,seg.registrarUsuario("jonblah@mail.com","AB1234567c","AB1234567c"))
        
    def testRegistroClaveDosMinusUnaMayus(self):
        # Corrio a la primera
        self.assertEqual(True,seg.registrarUsuario("jonblah@mail.com","ab1234567C","ab1234567C"))
        
    def testRegistroClaveTresMinus(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","ab1234567c","ab1234567c"))

    def testRegistroClaveTresMayus(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jonblah@mail.com","AB1234567C","AB1234567C"))
        
    def testRegistroClavesBienDif(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jon@blahmail.com","a12345F6789fg","a12345F6789ff"))
        
    def testRegistroBien(self):
        # Corrio a la primera
        self.assertEqual(True,seg.registrarUsuario("jon@blahmail.com","a12345F6789fg","a12345F6789fg"))

    def testAutVacio(self):
        # Corrio a la primera
        self.assertEqual(False,seg.AutenticarUsuario(None,None))
        
    def testDicVacio(self):
        # Corrio a la primera
        # Se intenta buscar algo en un diccionario vacio
        seg.Diccionario={}
        self.assertEqual(False,seg.AutenticarUsuario("jon1@blahmail.com","a12345F6789fg"))
        
    def testAutBien(self):
        # Corrio a la primera
        seg.registrarUsuario("jon1@blahmail.com","a12345F6789fg","a12345F6789fg")
        self.assertEqual(True,seg.AutenticarUsuario("jon1@blahmail.com","a12345F6789fg"))
        
    def testAutMalaClave(self):
        # Corrio a la primera
        seg.registrarUsuario("jon2@blahmail.com","a12345F6789fg","a12345F6789fg")
        self.assertEqual(False,seg.AutenticarUsuario("jon2@blahmail.com","a12345F6789f"))
        
    def testAutMalCorreo(self):
        # Corrio a la primera
        seg.registrarUsuario("jon3@blahmail.com","a12345F6789fg","a12345F6789fg")
        self.assertEqual(False,seg.AutenticarUsuario("jon3@mail.com","a12345F6789fg"))

    # Frontera
    def testStringGrande(self):
        # Primero se trato con un string demasiado grande y se quedo colgada la computadora
        # luego intentamos con este string bastante grande y funciono
        muchasA = 'a'*(2**20)
        self.assertEqual(True,seg.registrarUsuario("{}@b.ve".format(muchasA), "a12345F6789fg", "a12345F6789fg"))

    def testStringVacioEmail(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("","a12345F6789fg","a12345F6789fg"))

    def testStringVacioClave(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jon3@blahmail.com","",""))

    def testStringsVacios(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("","",""))

    # Malicia   
    def testCorreoInicioVacio(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("@.com", "a12345F6789fg", "a12345F6789fg"))
        
    def testDoblePuntoHost(self):
        # Corrio a la primera
        self.assertEqual(True,seg.registrarUsuario("jon3@blahmail.com.ve", "a12345F6789fg", "a12345F6789fg"))
        self.assertEqual(True,seg.AutenticarUsuario("jon3@blahmail.com.ve","a12345F6789fg"))
       
    def testDosArrobasSeguidos(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jon3@@blahmail.com.ve", "a12345F6789fg", "a12345F6789fg"))

    def testDosArrobasSeparados(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("jon3@blah@mail.com.ve", "a12345F6789fg", "a12345F6789fg"))

    def testCaracterEspecialEmailValido(self):
        # Dependiendo de que caracter especial se coloque en la direccion email este lo puede aceptar
        # o no, por ahora solo acepta .,_,- y +, cualquier otro fallara
        self.assertEqual(True,seg.registrarUsuario("hola+2@blahmail.com","a12345F6789fg","a12345F6789fg"))

    def testCaracterEspecialEmailInvalido(self):
        # Corrio a la primera
        self.assertEqual(False,seg.registrarUsuario("hola~2@blahmail.com","a12345F6789fg","a12345F6789fg"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
