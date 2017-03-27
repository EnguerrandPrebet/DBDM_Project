Attribute=str #Un attribut est simplement une chaine de caractre

class SetAttr(set):
	def __init__(self, *args, **kwargs):
		super(SetAttr,self).__init__(*args,**kwargs)
		self.s_hash = hash(str(self))
		
	def __repr__(self):
		s = set.__repr__(self)
		return "'" + " ".join(list(self)) + "'"	
		
	def __str__(self):
		s = self.__repr__()
		return s[1:-1]
	
	def copy(self):
		return SetAttr(super(SetAttr,self).copy())

	def __hash__(self):
		return self.s_hash
		
	def upd_hash(self):
		self.s_hash = hash(str(self))
SetOfSetAttr=set #Un set de set d'attribut est simplement un set


class FD:

	def __init__(self,prerequis=SetAttr(),conclusion=SetAttr()):
		self.prerequis=prerequis
		self.conclusion=conclusion
		self.s_hash = hash(str(self))
	def __repr__(self):
		return( "'" + str(self.prerequis)+' -> '+ str(self.conclusion) + "'")
	
	def __str__(self):
		s = self.__repr__()
		return s[1:-1]
		
	def __hash__(self):
		return self.s_hash
		
	def upd_hash(self):
		self.s_hash = hash(str(self))
SetFD=set #Un set de FD est simplement un set
