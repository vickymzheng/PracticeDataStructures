class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
    def print_list(self):
    	if (self.data == None):
    		print ""
    	while (self.data != None):
    		print self.data
    		if (self.next == None):
    			break
    		self = self.next
    def appendToTail(self, toAdd):
    	end = Node(toAdd)
    	while (self.next != None):
    		self = self.next
    	self.next = end
    def delete(self, toDelete):
    	if self.data = toDelete:
    		return self.next

    	while self.next != none:
    		if self.next.data == toDelete:
    			self.next = self.next.next
    			return self
    		self = self.next
    	return self


d = Node(1)
d.appendToTail(2)
d.print_list()

