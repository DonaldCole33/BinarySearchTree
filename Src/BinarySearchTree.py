



class Node:
    def __init__(self, key=None, lineNumber=None):
        self.l_child = None
        self.r_child = None
        self.key = key
        self.lineNumber = []
        
    def _addLineNumberf(self, num):
        self.lineNumber.append(num)
        
    def _getLineNumber(self):
        return self.lineNumber  #this will be used for when there are multiples of the same word
                                #returning the line number will be added to the previous node
 
        
def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

