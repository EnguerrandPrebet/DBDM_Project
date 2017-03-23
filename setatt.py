class SetAttr(set):
	def __init__(self, *args, **kwargs):
		super(SetAttr,self).__init__(*args,**kwargs)
		self.s_hash = hash(str(self))
		
	def __repr__(self):
		s = set.__repr__(self)
		return "".join(list(self))
	
	def __hash__(self):
		return self.s_hash
		
	def upd_hash(self):
		self.s_hash = hash(str(self))
		
	def copy(self):
		return SetAttr(super(SetAttr,self).copy())