import os

os.chdir("D:\\Users\\Yannis\\Documents")




def parseFD(filename):
	with open(filename,'r') as fichier:
		text=fichier.read()
	text=text.split('\n')
	print(len(text))
	list=[]	
	for i,ligne in enumerate(text):
		ligne=ligne.strip(' \t')
		text[i]=ligne
	if len(ligne)==0 or ligne[0]=='#':
	list.append(i)
	for i in reversed(list):
		del(text[i])
	for ligne in text:
		print(ligne.split('->'))
	[txtpre,txtconcl]=ligne.split('->')  
	return(parseSetattr(txtpre),parseSetattr(txtconcl))



def parseSetattr(ligne):
	ligne=ligne.split(' ')
	list=[]
	for i,attr in enumerate(ligne):
		if attr=='':  
	list.append(i)
	for i in reversed(list):
		del(ligne[i])  
