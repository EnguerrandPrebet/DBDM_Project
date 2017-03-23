from fd import *
from algo1 import *
from generate import *
from setatt import *

def check(fds,x,y):
    imp = improved(fds,x)
    print(y,imp)
    return y in imp
    
def normalize(fds):
    return reduce(minimize(fds))
    
def minimize(fds):
    G = set()
    for fd in fds:
        print("fd",fd,"fds",fds)
        print(improved(fds,fd.prerequis))
        G.add(FD(fd.prerequis,improved(fds,fd.prerequis)))
        print(G)
    iterable = G.copy()
    
    for fd in iterable:
        G.remove(fd)
        if(not check(G,fd.prerequis,fd.conclusion)):
            G.add(fd)
    print("G",G)
    return G

def reduce(mini):
    for fd in mini:
        iterable = fd.conclusion.copy()
        for a in iterable:
            fd.conclusion.remove(a)
            if(not check(mini,fd.prerequis,iterable)):
                fd.conclusion.add(a)
    return mini
    
    
print(normalize(generate(5)))