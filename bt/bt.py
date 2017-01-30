import math

def printLevel(level):
    levelAsNums = []
    for node in level:
        levelAsNums.append(node.data)
    print levelAsNums

class node:
    def __init__(self, data = None, left = None, right = None):
        # 
        self.left = left
        self.right = right
        self.data = data
    

    def insert(self, newNode):
        # base case: insert if direct child is None
        # otherwise, call this on left child and call this on right child
        
        if self.left is None:
            self.left = newNode
            return newNode
        if self.right is None:
            self.right = newNode
            return newNode
        
        if self.left is not None:
            return self.left.insert(newNode)
        if self.right is not None:
            #never get here
            return self.right.insert(newNode)

    def BFSPrint(self):
        thisLevel = [self]
        level = 0
        nodesAdded = 1
        while nodesAdded > 0:
            nodesAdded = 0
            print "Level: " + str(level) 
            printLevel(thisLevel)
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

    def balancedInsert(self, newNode):
        print "newNode: " + str(newNode.data)
        if self is None:
            self = newNode
            return self

        thisLevel = [self]
        it = 0
        while True:
            numNodesThisLevel = len(thisLevel) #should be a power of 2
            expectedNextLevel = 2*numNodesThisLevel
            nextLevel = []
            nodesNextLevel = 0
            for node in thisLevel:
                if node.left is not None:
                    nextLevel.append(node.left)
                    nodesNextLevel+=1
                if node.right is not None:
                    nextLevel.append(node.right)
                    nodesNextLevel+=1    
            
            #This means current level is full
            if nodesNextLevel == 0:
                parent = thisLevel[0]
                parent.left = newNode
                return newNode

            if nodesNextLevel != expectedNextLevel:
                nodeDiff = expectedNextLevel - nodesNextLevel
                numNodesToPop = 0
                if nodeDiff%2 == 0:
                    numNodesToPop = nodeDiff/2 -1
                else:
                    numNodesToPop = (nodeDiff)/2 # added 1 to round up
                for i in range(0, numNodesToPop):
                    thisLevel.pop()
                    
                parent = thisLevel[-1]
                if parent.left is None:
                    parent.left = newNode
                    return newNode
                if parent.right is None:
                    parent.right = newNode
                    return newNode

            thisLevel = nextLevel
            it+=1


    def printTree(self, depth=0):
        #do dfs print
        print 'data={data}, depth={depth}'.format(data=self.data, depth=depth)
        if self.left is None and self.right is None:
            return 
        if self.left is not None:
            self.left.printTree(depth=depth+1)
        if self.right is not None:
            self.right.printTree(depth=depth+1)
    #implement deletion 
root = node(0)
numbers_to_insert = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14]
for num in numbers_to_insert:
    root.balancedInsert(node(num))

root.BFSPrint()

# print "root: " + str(root.data)
# print "rootLeft: " + str(root.left.data)
# print "rootRight: " + str(root.right.data)
# print "rootLeftLeft: " + str(root.left.left.data)
# print "rootLeftRight: " + str(root.left.right.data)
# print "rootRightLeft: " + str(root.right.left.data)
# print "rootRightRight: " + str(root.right.right.data)
# print "rootLeftLeftLeft: " + str(root.left.left.left.data)
#    0
#   /  \ 
#  1    2
# / \  / \
# 3 4  5  6

