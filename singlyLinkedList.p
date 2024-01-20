
class singlyLinkedList:
	
	class	Node:
		def	__init__(self,	data,	next_Node=None):
			self.elem	=	data
			self.succ	=	next_Node

	def	__init__(self):
		self.head	=	None
		self.tail	=	None
		self.sz		=	0

	def sz(self):
		return self.sz 

	def is_empt(self):
		return self.sz==0

	def first(self):
		if self.sz==0:
			return None
		return self.head.elem

	def last(self):
		if self.sz==0:
			return None
		return self.tail.elem

	def addF(self,	data):
		new_Node	=	Node(data)
		self.head	=	new_Node
		if	self.is_empt():
			self.tail	=	new_Node
		self.sz		+=	1
	def addL(self,	data):
		new_Node	=	Node(data)
		if	self.is_empt():
			self.head	=	new_Node
		else:
			self.tail.succ	=	new_Node
		self.tail	=	new_Node
		self.sz	+=	1
	def remF(self):
		if self.is_empt:
			return None
		removed	=	self.head.elem
		self.head	=	self.head.succ
		self.sz	-=	1
		if	self.size	==	0:
			self.tail	=	None
		return	removed
	def	eq(self,other):
		if	other	is	None:
			return	False
		if	self.__class__	!=	other.__class__:
			return	False
		if	self.sz	!=	other.sz:
			return False

		walk1	=	self.head
		walk2	=	other.head

		while	walk1	is not	None:
			if	walk1.elem	!=	walk2.elem:
				return	False
			walk1	=	walk1.succ
			walk2	=	walk2.succ
		return True

	def	clone(self):
		try:
			other	=	singlyLinkedList
			if	self.sz	>	0:
				other.head	=	self.Node(self.head.elem)//instead of points to creates a new Node for this new instance
				walk	=	self.head.succ
				other_tail	=	self.Node(self.tail.elem)
				while	walk	is	not	None:
					baby	=	self.Node(walk.elem)
					other_tail.succ	=	baby
					other_tail	=	baby
					walk	=	walk.succ
			other.sz	=	self.sz
			return	other
		except	CloneNotSupportedException:
			return	None
	def hashF(self):
		h	=	0
		walk	=	self.head
		while	walk	is	not	None:
			h	^=	hash(walk.elem)
			h	=	(h	<<	5)	|	(h	>>	27) //	since 5 = 0101 and 27 = 1 1011 
			walk	=	walk.succ				//	stays 0 if elem <= 0100 or elem >= 1 1100
												//	(does it NEEDS  last 2 bits)
		return h

	def	__str__(self):
		res	=	"("
		walk	=	self.head
		while	walk	is	not	None:
			res	+=	str(walk.elem)
			if	walk	!=	self.tail:
				res	+=	", "
			walk	=	walk.succ
		res	+=	")"
		return	res
