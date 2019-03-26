def factorial(n):
    if n < 0:
        raise Exception("Invalid input")
    return_value = 1
    for i in range(1, n+ 1):
        return_value *= i
    return return_value


from functools import reduce

def factorial2(n):
   # return_value =
   if n < 0:
       raise Exception("Invalid input")

   return reduce(lambda x, y: x * y, range(1, n+1) )

import unittest
#import pdb
class TestFactorial(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(factorial(22), factorial2(22))
        self.assertEqual(factorial(1), 1)

    def test_negative(self):
        #pdb.set_trace()
        self.assertRaises(Exception, factorial2, -1)
        self.assertRaises(Exception, factorial, -2)

if __name__ == "__main__":
    print(factorial(22))
    unittest.main()

