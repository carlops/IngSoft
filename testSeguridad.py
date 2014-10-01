'''
Created on 1 Oct 2014

@authors: Carlo Polisano S
          Alejandro Guevara
'''
import unittest
from Seguridad import clsSeguridad


class Test(unittest.TestCase):


    def testRegistro(self): #se agrega siguiendo el enfoque TDD
        seg=clsSeguridad()
        seg.registrarUsuario()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()