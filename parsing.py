#coding:utf32
import os
os.chdir("D:\\Users\\Yannis\\Documents")

Attribute=str #Un attribut est simplement une chaine de caractére

Setattr=set #Un set d'attribut est simplement un set

Setofsetattr=set#Un set de set d'attribut est simplement un set
    
def affichSetattr(setattr):
    ret=""
    for i in setattr:
        ret+=' '+i
    return(ret[1:])

class FD:
    def __init__(self,prerequis=set(),conclusion=set()):
        self.prerequis=prerequis
        self.conclusion=conclusion
    
    def __repr__(self):
        return(affichSetattr(self.prerequis)+' -> '+ affichSetattr(self.conclusion))
        
SetFD=set #Un set de FD est simplement un set



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
    return(Setattr(ligne))
        
    
    
    

