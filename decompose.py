
from classe import *
from algo1 import *
from normalize import *

def schema(fds):
    setattr = SetAttr()
    for fd in fds:
        setattr.update(fd.prerequis,fd.conclusion)
    return setattr
    
def check_key(fds,attr):
    return improved(fds,attr).issuperset(schema(fds))
    

def check_condition(fds,r):
    for table in r:
        for fd in fds:
            if(fd.prerequis.issubset(table) and not fd.conclusion.isdisjoint(table)):
                if(not check(fds,fd.prerequis,table)):
                    return True,table,fd
    return False,None,None
    
def decompose(fds,u):
    new_fds = normalize(fds)
    r = set({u})
    
    continuer,table_faux,fd_faux = check_condition(fds,r)
    while(continuer):
        r.remove(table_faux)
        closure = improved(fds,fd_faux.prerequis)
        r.add(closure)
        r.add(SetAttr(table_faux.difference(closure).union(fd_faux.prerequis)))
        continuer,table_faux,fd_faux = check_condition(fds,r)
    
    return r
    
    
"""s = SetAttr("ABC")
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

print(schema(fds))

print(check_key(fds,SetAttr("B")))
print(check_key(fds,SetAttr("A")))
print(check_key(fds,SetAttr("E")))

print(decompose(fds,schema(fds)))"""
# print(decompose(generate(40),schema(generate(40))))
