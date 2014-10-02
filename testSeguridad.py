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
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()