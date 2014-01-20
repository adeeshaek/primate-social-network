import unittest
import common

class TestCommon(unittest.TestCase):

	def test_read_CSV(self):
		#input of '' should return []
		self.assertEqual(common.read_CSV(''), [])

		#input of 1.0 should return [1]
		self.assertEqual(common.read_CSV(1.0), [1])

		#input of 1.0, 2 should return [1,2]
		self.assertEqual(common.read_CSV('1.0, 2'),[1,2])
