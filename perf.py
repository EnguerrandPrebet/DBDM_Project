import os, time, sys

GEN_CMD="./closure -generate "
NLIN_CL_CMD="./closure -naive - 0 "
LIN_CL_CMD="./closure -improved - 0 "


fichier=open("sortie.csv","w")
sys.stdout=fichier

print("Taille,Algorithme naïf,Algorithme amélioré")

n=1
for i in range (100,10000,100):
	for j in range(n):
		t0=time.time()
		os.system(GEN_CMD+str(i)+" | "+NLIN_CL_CMD)
		t1=time.time()
		os.system(GEN_CMD+str(i)+" | "+LIN_CL_CMD)
		t2=time.time()
		print(str(i)+","+str(t1-t0)+","+str(t2-t1))