def naive(fds,attr):
	cl = SetAttr(attr)
	done = False
	while(not done):
		done = True
		for fd in fds:
			if(fds.prerequis.issubset(cl) and not fds.conclusion.issubset(cl)):
				cl = cl.union(fds.prerequis)
				done = False
	return cl
	

	
def choose(u):
	return u.pop()
		
def improved(fds,attr):
	count = dict()
	list = dict()
	already_added = set()
	for fd in fds:
		count[fd] = len(fd.prerequis)
		for attribute in fd.prerequis:
			if attribute in already_added:
				list[attribute].append(fd)
			else:
				list[attribute] = []
				
	closure = SetAttr(attr)
	update = SetAttr(attr)
	while update:
		a = choose(update)
		update.remove(a)
		for fd in list[a]:
			count[fd] -= 1
			if(count[fd] == 0):
				update.union(fd.conclusion.difference(closure))
				closure.union(fd.conclusion)
	return closure
	