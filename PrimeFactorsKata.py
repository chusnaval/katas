import unittest


def generate(value) :
	array_of_int = []
	candidate = 2;
	while value > 1:
		while value % candidate == 0:
			array_of_int = array_of_int+[candidate]
			value /= candidate
		candidate = candidate+1
	if value > 1:
		array_of_int = array_of_int+[value]
	return array_of_int;

class TestPrimeFactorsKata(unittest.TestCase):
	
		def test_generate(self):
			self.assertEqual([], generate(1))
			self.assertEqual([2], generate(2))
			self.assertEqual([3], generate(3))
			self.assertEqual([2,2], generate(4))
			self.assertEqual([2,3], generate(6))
			self.assertEqual([2,2,2], generate(8))
			self.assertEqual([3,3], generate(9))
			

if __name__ == '__main__':
    unittest.main()
