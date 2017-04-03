import os,sys

from classe import *




def parseFD(EntreStantard,filename=""):
	if EntreStantard:
		text=sys.stdin.read()
	else:
		with open(filename,"r") as monfichier:
			text=monfichier.read()
	text.replace('\r','\n')
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
		print(ligne)
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