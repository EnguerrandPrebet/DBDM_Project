import os

NLIN_CL_CMD="./closure -naive - 0 "
LIN_CL_CMD="./closure -improved - 0 "

for i in range(10):
	os.system("./closure -naive -./TestUnitAlgo1Entre"+str(i)+" > Sortie"+str(i))