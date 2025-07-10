import unittest
import pyserial




class mathtest(unittest.TestCase):
    def  test_aadd(self):
        
        self.assertEqual(2,2)
    def  test_sub(self):
        self.assertEqual(7,8)

if __name__ == '__main__':
    unittest.main()
