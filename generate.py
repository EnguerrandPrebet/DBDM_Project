import random

from fd import FD
from setatt import SetAttr
random.seed()

def generate(n):
	tab = list(range(n))
	random.shuffle(tab)
	list_fds = [FD(SetAttr(str(i)),SetAttr(str(i+1))) for i in tab]
	for fd in list_fds:
		print(fd)
	return list_fds
generate(5)