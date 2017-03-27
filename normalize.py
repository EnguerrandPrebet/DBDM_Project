from fd import *
from algo1 import *
from generate import *
from classe import *

def check(fds,x,y):
    imp = improved(fds,x)
    # print("y",y,"imp",imp,y.issubset(imp))
    return y.issubset(imp)
    
def normalize(fds):
    x = minimize(fds)
    # print("mini",x)
    y = reduce(x)
    return y
    
def minimize(fds):
    G = set()
    # print("fds:",fds)
    for fd in fds:
        # print("fd",fd)
        # print(improved(fds,fd.prerequis))
        G.add(FD(fd.prerequis,improved(fds,fd.prerequis)))
        # print(G)
    iterable = G.copy()
    
    for fd in iterable:
        G.remove(fd)
        if(not check(G,fd.prerequis,fd.conclusion)):
            G.add(fd)
    # print("G",G,"fd :",fd)
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

s = SetAttr("ABC")
s1 = SetAttr("AB")
s2 = SetAttr("AC")
s3 = SetAttr("A")
s4 = SetAttr("B")
s5 = SetAttr("C")
s6 = SetAttr("D")
s7 = SetAttr("BDE")
s8 = SetAttr("BC")
s9 = SetAttr("BE")

fds = [FD(s4,s5),FD(s3,s1),FD(s5,s6),FD(s7,s3),FD(s8,s9)]

# print(normalize(fds))