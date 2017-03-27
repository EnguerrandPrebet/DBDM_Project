from fd import *
from classe import *
from generate import generate

def naive(fds,attr):
	cl = attr.copy()
	done = False
	while(not done):
		done = True
		for fd in fds:
			# print("checking",fd)
			if(fd.prerequis.issubset(cl) and not fd.conclusion.issubset(cl)):
				# print(cl,"contains",fd.prerequis)
				cl.update(fd.conclusion)
				# print(cl,"updated from",fd.conclusion)
				done = False
	return cl
	


		
def improved(fds,attr):
	def choose(u):
		return u.pop()
	
	count = dict()
	list = dict()
	already_added = set()
	for fd in fds:
		count[fd] = len(fd.prerequis)
		for attribute in fd.prerequis:
			if attribute in already_added:
				list[attribute].append(fd)
			else:
				list[attribute] = [fd]
				already_added.add(attribute)
	#print("list",list)
	#print("count",count)
	closure = attr.copy()
	update = attr.copy()
	while update:
	#	print("update",update)
		a = choose(update)
	#	print("a chosen",a)
		if(a not in list):
			continue
		for fd in list[a]:
			count[fd] -= 1
			if(count[fd] == 0):
				update.update(fd.conclusion.difference(closure))
	#			print("update",update,"updated from",fd.conclusion.difference(closure))
				closure.update(fd.conclusion)
	#			print("closure",closure,"updated from",fd.conclusion)
	#	print(count)
	return closure
	
	
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

def test(fds,attr):
	print("naive",naive(fds,attr))
	print("improved",improved(fds,attr))
	
# test(fds,SetAttr("B"))

fds = generate(5)

# test(fds,SetAttr("13"))