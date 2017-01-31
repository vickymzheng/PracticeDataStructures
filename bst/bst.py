class node: 
	def __init__(self, data = None, left = None, right = None, parent = None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

	def height(self):
		if self is None:
			return 0 
		leftHeight = 0
		if self.left is not None:
			leftHeight = self.left.height() 
		rightHeight = 0
		if self.right is not None:
			rightHeight = self.right.height() 
		return max(leftHeight, rightHeight) + 1

	def printLevel(self, level):
	    levelAsNums = []
	    for node in level:
	    	if node is None:
	    		levelAsNums.append(None)
	        else:
	        	levelAsNums.append(node.data)
	    print levelAsNums

	#Helps Identify left and right children
	def BFSPrintFullTree(self):
		thisLevel = [self]
		level = 0
		nodesAdded = 1
		while nodesAdded > 0:
		    nodesAdded = 0
		    print "Level: " + str(level) 
		    self.printLevel(thisLevel)
		    nextLevel = []
		    for node in thisLevel:
		    	if node is None:
		    		nextLevel.append(None)
		    		nextLevel.append(None)
		    	else:
			        if node.left is not None:
			            nodesAdded+=1
			        nextLevel.append(node.left)
			        if node.right is not None:
			            nodesAdded+=1
			        nextLevel.append(node.right)
		        thisLevel = nextLevel
		    level+=1

	#Gives contents at each level (non-None)
	def BFSPrint(self):
		thisLevel = [self]
		level = 0
		nodesAdded = 1
		while nodesAdded > 0:
		    nodesAdded = 0
		    print "Level: " + str(level) 
		    self.printLevel(thisLevel)
		    nextLevel = []
		    for node in thisLevel:
		        if node.left is not None:
		            nextLevel.append(node.left)
		            nodesAdded+=1
		        if node.right is not None:
		            nextLevel.append(node.right)
		            nodesAdded+=1
		        thisLevel = nextLevel
		    level+=1

	def size(self):
		return self.size 

	def insert(self, newNode):
		if self is None:
			self = newNode
			self.parent = self
			return newNode
		if newNode.data < self.data:
			if (self.left is None):
				self.left = newNode
				self.left.parent = self 
				return newNode
			return self.left.insert(newNode)
		else: 
			if (self.right is None):
				self.right = newNode
				self.right.parent = self 
				return newNode
			return self.right.insert(newNode)
	
	def find(self,value):
		root = self
		while root is not None:
			if root.data == value:
				return root
			if value < root.data:
				root = root.left
			else:
				root = root.right
		return None

	def contains(self, value):
		if self.find(value) is  None:
			return False
		return True 
	
	def isLeftChild(self):
		return self == self.parent.left 

	def isRightChild(self):
		return self == self.parent.right 

	def delete(self, value):
		toDelete = self.find(value)
		if toDelete is None:
			return 
		numChildren = 0
		if toDelete.left is not None:
			numChildren+=1
		if toDelete.right is not None:
			numChildren+=1
		
		#leaf 
		if numChildren == 0:
			toDelete = None
		elif numChildren == 1:
			if toDelete.left is not None:
				#toDelete has a left child
				if toDelete.isLeftChild():
					#to delete is a left child and has a left child

					#set left child's parent to to delete's parent
					toDelete.left.parent = toDelete.parent
					# set parent's left child to 
					toDelete.parent.left = toDelete.left
					toDelete = None
					return 
				#to delete has a left child and is a right child
				toDelete.left.parent = toDelete.parent
				# set parent's left child to toDelete's left
				toDelete.parent.right = toDelete.left
				toDelete = None
				return 
			
			#toDelete has a right child
			if toDelete.isLeftChild():
				#to delete has a right child and is a left child 

				#set right child's parent to to delete's parent
				toDelete.right.parent = toDelete.parent
				# set parent's left child to 
				toDelete.parent.left = toDelete.right
				toDelete = None
				return 

				#to delete has a right child and is a right child 

			#set right child's parent to to delete's parent
			toDelete.right.parent = toDelete.parent
			# set parent's right child to toDelete's right child
			toDelete.parent.right = toDelete.right
			toDelete = None
			return 
		else: 
			#toDelete has two children. 
			#The right child will replace to delete
			#The left child will be added the right child's subtree
			toDelete.right.parent = toDelete.parent 
			if toDelete.isLeftChild():
				toDelete.parent.left = toDelete.right
			else: 
				toDelete.parent.right = toDelete.right
			toDelete.right.insert(toDelete.left)
			toDelete = None 
			return 


tree = node(50)
nums = [1,2, 51]
for num in nums:
	tree.insert(node(num))
tree.BFSPrint()
print tree.height()
