import random

random.seed()

def generate(n):
	tab = list(range(n))
	random.shuffle(tab)
	list_fds = [FD(i,i+1) for i in tab]
	for fd in list_fds:
		print(fd)
		