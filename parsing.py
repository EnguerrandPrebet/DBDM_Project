import os

os.chdir("D:\\Users\\Yannis\\Documents\\DBDM_Project")

from classe import *




def parseFD(filename):
	with open(filename,'r') as fichier:
		text=fichier.read()
	text=text.split('\n')
	list=[]	
	for i,ligne in enumerate(text):
		ligne=ligne.strip(' \t')
		text[i]=ligne
		if len(ligne)==0 or ligne[0]=='#':
			list.append(i)
	for i in reversed(list):
		del(text[i])
	res=SetOfSetAttr()
	for ligne in text:
		[txtpre,txtconcl]=ligne.split('->')
		print(FD(parseSetattr(txtpre),parseSetattr(txtconcl)))
		res.add(FD(parseSetattr(txtpre),parseSetattr(txtconcl)))
	return(res)


def parseSetattr(ligne):
	ligne=ligne.split(' ')
	list=[]
	for i,attr in enumerate(ligne):
		ligne[i]=attr.strip(' \t')
		if len(ligne[i])==0:  
			list.append(i)
	for i in reversed(list):
		del(ligne[i])
	seta=SetAttr(ligne)
	return(seta)