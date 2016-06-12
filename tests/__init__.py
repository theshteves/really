import unittest

#def try_build(x):
def square(x):
    return x*x

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(square(2), 4)

if __name__ == '__main__':
    unittest.main()

