class FauxSet(object):
    def __init__(self,set):
        self.set = set
    
    def __repr__(self):
        return self.set.__repr__()
    def __str__(self):
        return str(self.set)
    
    #Simulate set behaviour    
    def __getattr__(self,name):
        #Get set equivalence
        attr = self.set.__getattribute__(name)
        #Distinguish method from attribute
        if hasattr(attr,'__call__'):
            #Create method for the fake class
            def newfunc(*args, **kwargs):
                return attr(*args, **kwargs)
            return newfunc
        else:
            #Return the attribute
            return attr

class FauxSet2(set):
    def __repr__(self):
        s = set.__repr__(self)
        return "".join(s[10:-2].split(", "))
