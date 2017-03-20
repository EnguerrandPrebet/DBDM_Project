import sys

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
	if(sys.argv[2] != '-'):
		sys.stdin = open(sys.argv[2],'r')
	
	fds = parseFD()#TODO argument
	
	if(algo == "-normalize"):
		print("normalize", file = log)
		normalize(fds)
		
	elif(algo == "-decompose"):
		print("decompose", file = log)
		decompose(fds)
		
	else:
		if(len(sys.argv) != 4):
			print("Wrong number of arguments, 4 expected",file = sys.stderr)
		
		setAttr = SetAttr(sys.argv[3:])
		
		if(algo == "-improved"):
			print("improved", file = log)
			improved(fds,setAttr)
		
		elif(algo == "-naive"):
			print("naive", file = log)
			naive(fds,setAttr)
			
		else:
			print("First argument should be: \n-naive\n-improved\n-generate\n-normalize\n-decompose", file = sys.stderr)