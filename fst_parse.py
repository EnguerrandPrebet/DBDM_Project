import sys

from normalize import *
from decompose import *
from algo1 import *
from parsing import *
from classe import *
from generate import *


log = open("plop.log","w")
#Input parsing
if(len(sys.argv) < 3):
	print("Not enough arguments",file = sys.stderr)
algo = sys.argv[1]

if(algo == "-generate"):
	print("generate", file = log)
	if(len(sys.argv) != 3):
		print("Too much arguments for generate",file = sys.stderr)
	generate(int(sys.argv[2]))

else:
	if(sys.argv[2][0] != '-'):
		fds=parseFD(False,sys.argv[2])
	else:
		fds=parseFD(True)
	
	if(algo == "-normalize"):
		print("normalize", file = log)
		print("Normalize:",normalize(fds))
		
	elif(algo == "-decompose"):
		print("decompose", file = log)
		print("Decompose:",decompose(fds,schema(fds)))
		
	else:
		if(len(sys.argv) != 4):
			print("Wrong number of arguments, 4 expected",file = sys.stderr)
		
		setAttr = SetAttr("".join(sys.argv[3:]))
		
		if(algo == "-improved"):
			print("improved", file = log)
			print("Improved:",improved(fds,setAttr))
		
		elif(algo == "-naive"):
			print("naive", file = log)
			print("Naive:",naive(fds,setAttr))
			
		else:
			print("First argument should be: \n-naive\n-improved\n-generate\n-normalize\n-decompose", file = sys.stderr)