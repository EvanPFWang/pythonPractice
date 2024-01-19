
class singlyLinkedList:
	
	class Node:
		def __init(self,data,	next_Node=None):
			self.element = data
			self.next = next_node

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def size(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def first(self):
		if self.is_empty():
			return None
		return self.head.element
	def last(self):
		if self.is_empty():
			return	None
		return	self.tail.element

	def add_first(self,	data):
		new_Node = self.Node(data,	self.head)
		self.head = new_Node
		if self.size	==	0:
			self.tail	=	new_Node
		self.size	+=	1

	def	add_last(self,data):
		new_Node = self.Node(data)
		if self.is_empty():
			self.head = new_Node
		else:
			self.tail.next = new_Node
		self.tail	=	new_Node
		self.size	+=	1

	def remove_first(self):
		if self.is_empty():
			return None
		removed_elem	=	self.head.element
		self.head	=	self.head.next
		self.size	-=	1
		if	self.size()	==	0:
			self.tail = None
		return removed_elem


		"""     def equals(self, other):
        if other is None:
            return False
        if self.__class__ != other.__class__:
            return False
        if self.size != other.size:
            return False

        walk_a = self.head
        walk_b = other.head
        while walk_a is not None:
            if walk_a.element != walk_b.element:
                return False
            walk_a = walk_a.next
            walk_b = walk_b.next
        return True

    def clone(self):
        try:
            other = SinglyLinkedList()
            if self.size > 0:
                other.head = self.Node(self.head.element)
                walk = self.head.next
                other_tail = other.head
                while walk is not None:
                    newest = self.Node(walk.element)
                    other_tail.next = newest
                    other_tail = newest
                    walk = walk.next
            other.size = self.size
            return other
        except CloneNotSupportedException:
            return None

    def hash_code(self):
        h = 0
        walk = self.head
        while walk is not None:
            h ^= hash(walk.element)
            h = (h << 5) | (h >> 27)
            walk = walk.next
        return h

    def __str__(self):
        result = "("
        walk = self.head
        while walk is not None:
            result += str(walk.element)
            if walk != self.tail:
                result += ", "
            walk = walk.next
        result += ")"
        return result"""