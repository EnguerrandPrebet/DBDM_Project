import algo1,unittest

from classe import *

class MyTestCaseNaive(unittest.TestCase):
	def test_normal_case(self):
		fd = set([FD(SetAttr('A'),SetAttr('B')),FD(SetAttr('B'),SetAttr('C')),FD(SetAttr('C'),SetAttr('D')),FD(SetAttr('D'),SetAttr('E'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.naive(fd, attr), SetAttr(['A','B','C','D','E']))
	def test_empty_fds(self):
		fd = set()
		attr=SetAttr('A')
		self.assertEqual(algo1.naive(fd, attr), SetAttr('A'))
	def test_right_blank(self):
		fd = set([FD(SetAttr('A'),SetAttr()),FD(SetAttr('B'),SetAttr('C'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.naive(fd, attr), SetAttr('A'))
	def test_left_blank(self):
		fd = set([FD(SetAttr('A'),SetAttr('B')),FD(SetAttr('B'),SetAttr('C')),FD(SetAttr(),SetAttr('D'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.naive(fd, attr), SetAttr(['A','B','C','D']))
	def test_compliquer_case(self):
		fd = set([FD(SetAttr('A'),SetAttr(['B','C'])),FD(SetAttr('C'),SetAttr(['D','E'])),FD(SetAttr(['B','E']),SetAttr('F')),FD(SetAttr('A'),SetAttr('C'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.naive(fd, attr), SetAttr(['A','B','C','D','E','F']))


class MyTestCaseimproved(unittest.TestCase):
	def test_normal_case(self):
		fd = set([FD(SetAttr('A'),SetAttr('B')),FD(SetAttr('B'),SetAttr('C')),FD(SetAttr('C'),SetAttr('D')),FD(SetAttr('D'),SetAttr('E'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.improved(fd, attr), SetAttr(['A','B','C','D','E']))
	def test_empty_fds(self):
		fd = set()
		attr=SetAttr('A')
		self.assertEqual(algo1.improved(fd, attr), SetAttr('A'))
	def test_right_blank(self):
		fd = set([FD(SetAttr('A'),SetAttr()),FD(SetAttr('B'),SetAttr('C'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.improved(fd, attr), SetAttr('A'))
	def test_left_blank(self):
		fd = set([FD(SetAttr('A'),SetAttr('B')),FD(SetAttr('B'),SetAttr('C')),FD(SetAttr(),SetAttr('D'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.improved(fd, attr), SetAttr(['A','B','C','D']))
	def test_compliquer_case(self):
		fd = set([FD(SetAttr('A'),SetAttr(['B','C'])),FD(SetAttr('C'),SetAttr(['D','E'])),FD(SetAttr(['B','E']),SetAttr('F')),FD(SetAttr('A'),SetAttr('C'))])
		attr=SetAttr('A')
		self.assertEqual(algo1.improved(fd, attr), SetAttr(['A','B','C','D','E','F']))

if __name__ == '__main__':
	unittest.main()