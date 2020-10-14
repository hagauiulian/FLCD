#Represent a node of binary tree
class Node:
    def __init__(self,data,id):
        #Assign data to the new node, set left and right children to None
        self.id = id
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        #Represent the root of binary tree
        self.count = 0
        self.root = Node("", -1)

    #insert() will add new node to the binary search tree
    def insert(self, key, data):
        #Create a new node
        newNode = Node(key, data)

        #Check whether tree is empty
        if(self.root == None):
            self.root = newNode
            return
        else:
            #current node point to root of the tree
            current = self.root

            while(True):
                #parent keep track of the parent node of current node.
                parent = current

                #If data is less than current's data, node will be inserted to the left of tree
                if(data < current.data):
                    current = current.left
                    if(current == None):
                        parent.left = newNode
                        return

                #If data is greater than current's data, node will be inserted to the right of tree
                else:
                    current = current.right
                    if(current == None):
                        parent.right = newNode
                        return

    #minNode() will find out the minimum node
    def minNode(self, root):
        if(root.left != None):
            return self.minNode(root.left)
        else:
            return root

    #deleteNode() will delete the given node from the binary search tree
    def deleteNode(self, node, value):
        if(node == None):
            return None
        else:
            #value is less than node's data then, search the value in left subtree
            if(value < node.data):
                node.left = self.deleteNode(node.left, value)

            #value is greater than node's data then, search the value in right subtree
            elif(value > node.data):
                node.right = self.deleteNode(node.right, value)

            #If value is equal to node's data that is, we have found the node to be deleted
            else:
                #If node to be deleted has no child then, set the node to None
                if(node.left == None and node.right == None):
                    node = None

                #If node to be deleted has only one right child
                elif(node.left == None):
                    node = node.right

                #If node to be deleted has only one left child
                elif(node.right == None):
                    node = node.left

                #If node to be deleted has two children node
                else:
                    #then find the minimum node from right subtree
                    temp = self.minNode(node.right)
                    #Exchange the data between node and temp
                    node.data = temp.data
                    #Delete the node duplicate node from right subtree
                    node.right = self.deleteNode(node.right, temp.data)
        return node

    #inorder() will perform inorder traversal on binary search tree
    def inorderTraversal(self, node):
        #Check whether tree is empty
        if(self.root == None):
            print("Tree is empty")
            return
        else:
            if(node.left != None):
                self.inorderTraversal(node.left)
            print(node.data, end=" ")
            if(node.right != None):
                self.inorderTraversal(node.right)

bt = BinarySearchTree()
#Add nodes to the binary tree
bt.insert("a",50)
bt.insert("b",30)
bt.insert("c",70)
bt.insert("d",60)
bt.insert("e",10)
bt.insert("f",90)

print("Binary search tree after insertion:")
#Displays the binary tree
bt.inorderTraversal(bt.root)
