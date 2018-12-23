'''
Created on Dec 23, 2018

@author: Haming Wu 
'''
class Node:
    def __init__(self,data):
        self.data = data # We need to have a data in our node, so we can assign our node
        self.adjacentList = []  #adjacentList also means that the kid in binary search tree 
        self.prodeccesor = None # In this example, we don't need this, but when we use BFS (breadth frist search), it can be usefeul 
        self.visited = False # We initialize it as False in the begining
        
        
class DepthFirstSearch:
    def dfs(self, node):
        node.visited = True # we set the node as visited, so we can keep chekcing others 
        print('{}'.format(node.data), end=' ') 
        for v in node.adjacentList:
            if not v.visited:
                self.dfs(v) # call dfs recursively
                
                
                
                
''' lets test it out '''
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacentList.append(node2) # I put node2 as kid of node1 
node2.adjacentList.append(node4) # I put node4 as kid of node2
node1.adjacentList.append(node3) # I put node3 as kid of node1
node1.adjacentList.append(node5) # I put node5 sa kid of node1 
dfs = DepthFirstSearch()
dfs.dfs(node1)        # I should get an order of A,B,D,C,E. 
#                       DFS means that it will traverse thoroughlly one kid before moves to the next kid




        