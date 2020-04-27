import json;

class Node(object):
    """Model for each node in the AVL tree"""

    def __init__(self,key,value):
        self.key = key;
        self.value = value;
        self.bf = 0;
        self.left = None;
        self.right = None;

    def printValues(self):
        return {
            'key' : self.key,
            'value' : self.value,
            'balanceFactor' : self.bf,
            'left' : '' if self.left is None else self.left.key,
            'right' : '' if self.right is None else self.right.key
                };

class AVLTree(object):
    """Model for the AVL tree"""

    ########## Tree Creation/Initialization ############
    def __init__(self):
        self.root = None;

    ########### Insertion ###########

    def add(self, word, meaning):
        self.root = self.__recurse_add(self.root, word, meaning);
        print('root:' + self.root.key);
        outp = [];
        return self.bfs_traversal(outp);
        #return self.preorder_traversal(self.root, outp);

    def __recurse_add(self, node, word, meaning):
        if node is None:
            node = Node(word,meaning);         
        elif word == node.key:
            return node;
        elif word < node.key:
            left = self.__recurse_add(node.left, word, meaning);
            node.left = left;
        else:
            right = self.__recurse_add(node.right, word, meaning);
            node.right = right;
        self.__update_bf(node);
        if node.bf > 1:
            if self.__heightDiff(node) < 0:
                if word > node.right.key:
                    print('left rotation');
                    node = self.__leftRotate(node);
                    self.print(node);
                else:
                    print('right-left rotation');
                    print('1.right child rotation');
                    node.right = self.__rightRotate(node.right);
                    self.print(node);
                    print('2.left rotation');
                    node = self.__leftRotate(node);
                    self.print(node);
            else:
                if word < node.left.key:
                    print('right rotation');
                    node = self.__rightRotate(node);
                    self.print(node);
                else:
                    print('left-right rotation');
                    print('1.left child rotation');
                    node.left = self.__leftRotate(node.left);
                    self.print(node);
                    print('2.right rotation');
                    node = self.__rightRotate(node);
                    self.print(node);
        return node;

    ########## Rotation ##############

    #rotate subtree to left
    def __leftRotate(self, node):
        newParent = node.right;
        child = newParent.left;

        newParent.left = node;
        node.right = child;

        self.__update_bf(newParent);
        return newParent;

    #rotate subtree to right
    def __rightRotate(self, node):
        newParent = node.left;
        child = newParent.right;

        newParent.right = node;
        node.left = child;

        self.__update_bf(newParent);
        return newParent;

    #update balance factor for each node |height(left) - height(right)|
    #return height of the node
    def __update_bf(self,node):
        if node is None:
            return;
        if node.left is None and node.right is None:
            node.bf = 0;
        else:
            leftHeight = self.__getHeight(node.left);
            rightHeight = self.__getHeight(node.right);
            node.bf = abs(leftHeight - rightHeight);
            self.__update_bf(node.left);
            self.__update_bf(node.right);

    #if 0 = subtree is balanced
    #if >0, leftSubtree is not balanced
    #id <0, rightSubtree is not balanced
    def __heightDiff(self, node):
        leftHeight = self.__getHeight(node.left);
        rightHeight = self.__getHeight(node.right);
        return leftHeight - rightHeight;

    #get height of subtree
    def __getHeight(self, node):
        leftHeight = 1;
        rightHeight = 1;
        if node is None:
            return 0;
        if node.left is None and node.right is None:
            return 1;
        leftHeight += 0 if node.left is None else self.__getHeight(node.left);
        rightHeight += 0 if node.right is None else self.__getHeight(node.right);
        return max(leftHeight,rightHeight);

    ########## Searching ##############

    def search(self, word):
        node = self.__recurse_search(self.root, word);
        if node is None:
            return '';
        else:
            return node.value;

    def __recurse_search(self, node, word):
        if node is None:
            return None;      
        elif word == node.key:
            return node;
        elif word < node.key:
            return self.__recurse_search(node.left, word);
        else:
            return self.__recurse_search(node.right, word);

    ########## Deletion ############

    def delete(self, word):
        self.root = self.__recurse_delete(self.root, word);
        if self.root is not None:
            print('root = ' + self.root.key);
        outp = [];
        return self.bfs_traversal(outp);

    def __recurse_delete(self, node, word):
        #find the node to delete
        if node is None:
            return None;      
        elif word == node.key:
            #always return new root after deletion
            if node.left is None:
                return node.right;
            elif node.right is None:
                return node.left;
            else:
                newRoot = self.__getSmallestNode(node.right);
                node.key = newRoot.key;
                node.value = newRoot.value;
                node.right = self.__recurse_delete(node.right, node.key);
        elif word < node.key:
            node.left = self.__recurse_delete(node.left, word);
        else:
            node.right = self.__recurse_delete(node.right, word);
        self.__update_bf(node);
        if node.bf > 1:
            #right subtree is inbalanced
            if self.__heightDiff(node) < 0:
                if self.__heightDiff(node.right) <= 0:
                    print('left rotation');
                    node = self.__leftRotate(node);
                    self.print(node);
                else:
                    print('right-left rotation');
                    print('1.right child rotation');
                    node.right = self.__rightRotate(node.right);
                    self.print(node);
                    print('2.left rotation');
                    node = self.__leftRotate(node);
                    self.print(node);
            #left subtree is inbalanced
            else:
                if self.__heightDiff(node.left) >= 0:
                    print('right rotation');
                    node = self.__rightRotate(node);
                    self.print(node);
                else:
                    print('left-right rotation');
                    print('1.left child rotation');
                    node.left = self.__leftRotate(node.left);
                    self.print(node);
                    print('2.right rotation');
                    node = self.__rightRotate(node);
                    self.print(node);
        return node;

    #smallest node should always be on the far left
    def __getSmallestNode(self,node):
        if node is None or node.left is None:
            return node;
        else:
            return self.__getSmallestNode(node.left);

    ########## Traversal ###########

    #LNR
    def inorder_traverse(self, node, output):
        if node.left is not None:
            self.inorder_traverse(node.left,output);
        output.append(node.printValues());
        if node.right is not None:
            self.inorder_traverse(node.right,output);
        return output;

    #NLR
    def preorder_traversal(self, node, output):
        if node is not None:
            output.append(node.printValues());
            self.preorder_traversal(node.left,output);
            self.preorder_traversal(node.right,output);  
        return output;

    #LRN
    def postorder_traversal(self, node, output):
        if node is not None:
            self.postorder_traversal(node.left, output);
            self.postorder_traversal(node.right, output);
            output.append(node.printValues());
        return output;

    def bfs_traversal(self, output):
        treeHeight = self.__getHeight(self.root);
        for i in range(1, treeHeight+1):
            self.__print_level(self.root, output, i);
        return output;

    def __print_level(self, node, output, level):
        if node is not None:
            if level == 1:
                output.append(node.printValues());    
            else:
                self.__print_level(node.left, output, level-1);
                self.__print_level(node.right, output, level-1);   
        return output;
            
    def print(self, node):
        if node is not None:
            print('{}-bf{}'.format(node.key, node.bf));
            self.print(node.left);
            self.print(node.right);    