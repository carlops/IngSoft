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
        seg.registrarUsuario()

    def testRegistroBien(self): 
        seg.registrarUsuario("jon@blahmail.com","a12345F6789fg","a12345F6789fg")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()