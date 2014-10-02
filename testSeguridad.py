'''
Created on 1 Oct 2014

@authors: Carlo Polisano S
          Alejandro Guevara
'''
import unittest
from Seguridad import clsSeguridad

seg=clsSeguridad()

class Test(unittest.TestCase):

#    def testRegistroIni(self):
#        seg.registrarUsuario()

    def testRegistroBien(self): 
        seg.registrarUsuario("jon@blahmail.com","a12345F6789fg","a12345F6789fg")

    def testAutBien(self):
        seg.registrarUsuario("jon1@blahmail.com","a12345F6789fg","a12345F6789fg")
        seg.AutenticarUsuario("jon1@blahmail.com","a12345F6789fg")
        
    def testAutMalaClave(self):
        seg.registrarUsuario("jon2@blahmail.com","a12345F6789fg","a12345F6789fg")
        seg.AutenticarUsuario("jon2@blahmail.com","a12345F6789f")
        
    def testAutMalCorreo(self):
        seg.registrarUsuario("jon3@blahmail.com","a12345F6789fg","a12345F6789fg")
        seg.AutenticarUsuario("jon3@mail.com","a12345F6789fg")
        
    # Frontera
    def testStringGrande(self):
        muchasA = 'a'*(2**20)
        seg.registrarUsuario("{}@b.ve".format(muchasA), "a12345F6789fg", "a12345F6789fg")
        
    def tesStringVacioEmail(self):
        seg.registrarUsuario("","a12345F6789fg","a12345F6789fg")
        
    def tesStringVacioClave(self):
        seg.registrarUsuario("jon3@blahmail.com","","")
        
    def testStringsVacios(self):
        seg.registrarUsuario("","","")
        
    # Malicia   
    def testStringPequeno(self):
        seg.registrarUsuario("@.com", "a12345F6789fg", "a12345F6789fg")
        
    def testDoblePuntoHost(self):
        seg.registrarUsuario("jon3@blahmail.com.ve", "a12345F6789fg", "a12345F6789fg")
        seg.AutenticarUsuario("jon3@blahmail.com.ve","a12345F6789fg")
        
    def testCaracterEspecialEmail(self):
        seg.registrarUsuario("hola+2@blahmail.com","a12345F6789fg","a12345F6789fg")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()