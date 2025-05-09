import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Tests para la clase calculator.
    """
    def test_add(self):
        """Prueba funcion de suma
        """
        self.assertEqual(Calculator.add(5,3), 5, msg="Funcion suma incorrecta")
    
    def test_multiply(self):
        """_summary_
        """
        self.assertEqual(Calculator.multiply(2,2), 4, msg="Funcion multiplicacion incorrecta.")

if __name__ == "__main__":
    unittest.main()