def closure(fds,attr):
    cl = SetAttr(attr)
    done = False
    while(not done):
        done = True
        for fd in fds:
            if(fds.prerequis.issubset(cl) and not fds.conclusion.issubset(cl)):
                cl = cl.union(fds.prerequis)
                done = False
    return cl