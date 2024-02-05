class Node:
    def __init__(self, val):
        self.left, self.right, self.val= None,None, val


class binaryTree: 
    def __init__(self):
        self.head = Node(None)
        self.lst= []

    def  inOrder(self , node):
        if (node):
            self.lst.append(node.val)
            self.inOrder(node.left)
            self.inOrder(node.right)
        
    def search(self,val):
        self.inOrder(self.head) 
        return val in self.lst

    def ret_lst(self):
        self.inOrder(self.head) 
        return self.lst

    def push(self,value):
        n = Node(value)
        inserted = False
        pointer = self.head
        while (not(inserted)):
            if(not(pointer.val)):
                self.head = n
                inserted= True
            else: 
                if (pointer.val > value):
                    if(pointer.left):   
                        pointer = pointer.left
                    else: 
                        pointer.left= n
                        inserted= True

                elif (pointer.val < value):
                    if(pointer.right):   
                        pointer = pointer.right
                    else: 
                        pointer.right= n    
                        inserted= True

bt= binaryTree()
bt.push(8)
bt.push(3)
bt.push(10)
bt.push(1)
bt.push(6)
bt.push(14)
bt.push(4)
bt.push(7)
bt.push(13)

print(bt.ret_lst())
print(bt.search(13))
print(bt.search(11))