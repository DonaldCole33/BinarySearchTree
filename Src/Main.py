'''
Created on Feb 2, 2015

@author: Don Cole
'''
#!/usr/bin/env python

import sys

class Node:
    def __init__(self, key=None, lineNumber=None):
        self.l_child = None
        self.r_child = None
        self.key = key
        self.lineNumber = []
        self.lineNumber.append(lineNumber)
 

def main():
    delim = ",.!?"      #parsing delimeter for strings
    bool = True         #used for creating the root node
    i = 0               #for line numbers
    
    logFile = open("BinarySearchlogfile.txt", "w")                    #log file
    logFile.write("Log File for Binary Search Tree Program\n")
    
    with open("file.txt",'r') as f:     #read file.txt
        fileData = f.readlines()
        for lines in fileData:              #create lines
            wordsArray = lines.split()      #parse lines               
            for key in wordsArray:          #key = each word
                key = key.strip(delim)      #strips period at end of words
                if key.isdigit() and i > 0:             #skip numbers
                    break
                elif key is "#":            #for end of File   
                    break  
                #this is for creating the root and then adding
                #the rest of the nodes to the root from the first line
                #root needs to be created on its own before nodes are added
                if i is 0:
                    for j in range(len(wordsArray)):        #loop through first line
                        key = wordsArray[j].strip(delim)    #creating stripped key
                        if not key.isdigit():               #checking for numbers on first line
                            if bool is True:                ####bool is for if a number is found as the first word(s)  
                                root = Node(key, i+1)       ####root would not be created if using i = 0 and the first
                                bool = False                ####word is a number
                            else:
                                node = Node(key, i+1)       
                                binary_insert(root, node)   #add the nodes to the root
                    break                     #End of the first line
                else:
                    #now the addition of nodes is easier from lines 2 and on
                    #i+1 = number of lines in text file
                    node = Node(key, i+1)
                    binary_insert(root, node)               #add nodes to root
            i += 1      #increment Line number
            
    key_in_order_print(root, logFile)
    f.close()           #close read-in file
    logFile.close()
    
def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.key == node.key:
            root.lineNumber.append(node.lineNumber[0])      #will add node's line number to root's
            return
        elif root.key > node.key:           #checks left child of root
            if root.l_child == None:        
                root.l_child = node         #root left child = node
            else:
                binary_insert(root.l_child, node)       #walks to the left child
        else:
            if root.r_child == None:
                root.r_child = node         #root right child = node
            else:
                binary_insert(root.r_child, node)       #walks to the right child

def key_in_order_print(root, logFile):
    if not root:
        return
    key_in_order_print(root.l_child, logFile)        #walk to the bottom of left child
    #will only print out the first 10 letters of each word        
    print '{0:15s}'.format(root.key[0:10]),"%s" % '     '.join(map(str,root.lineNumber))        #screen output
    logFile.write('{0:15s}{1:5s}\n'.format(root.key[0:10], root.lineNumber[0:]))                #logfile output
    key_in_order_print(root.r_child, logFile)        #walk to right when left is printed
    
if __name__ == '__main__':main()
