import unittest

def chop(value, array_of_int) :
	index = -1;
	sup = len(array_of_int)-1
	inf = 0

	# si tiene elementos
	if len(array_of_int) > 0 :
		while inf <= sup:
			mid = ((sup - inf) // 2) + inf
			if array_of_int[mid] == value:
				return mid
			else:
				if value < array_of_int[mid]:
					sup = mid - 1
				else:
					inf = mid + 1
	return index

class TestChopKata(unittest.TestCase):
	
		def test_chop(self):
			self.assertEqual(-1, chop(3, []))
			self.assertEqual(-1, chop(3, [1]))
			self.assertEqual(0, chop(1, [1]))
			#
			self.assertEqual(0, chop(1, [1, 3, 5]))
			self.assertEqual(1, chop(3, [1, 3, 5]))
			self.assertEqual(2, chop(5, [1, 3, 5]))
			self.assertEqual(-1, chop(0, [1, 3, 5]))
			self.assertEqual(-1, chop(2, [1, 3, 5]))
			self.assertEqual(-1, chop(4, [1, 3, 5]))
			self.assertEqual(-1, chop(6, [1, 3, 5]))
			#
			self.assertEqual(0, chop(1, [1, 3, 5, 7]))
			self.assertEqual(1, chop(3, [1, 3, 5, 7]))
			self.assertEqual(2, chop(5, [1, 3, 5, 7]))
			self.assertEqual(3, chop(7, [1, 3, 5, 7]))
			self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
			self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
			self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
			self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
			self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
    unittest.main()

