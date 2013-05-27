class node():
    def __init__(self,p=None,key=None):
        self.key=key
        self.p=p
        self.left=None
        self.right=None
    def __repr__(self):
        return str(self.key)
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print self.key, 
        if self.right is not None:
            self.right.inorder()
    def search(self,k):
        if k==self.key:
            return self
        elif k<self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(k)
    def minimum(self):
        x=self
        while x.left is not None:
            x=x.left
        return x
    def maximum(self):
        x=self
        while x.right is not None:
            x=x.right
        return x
    def successor(self):
        if self.right is not None:
            return self.right.minimum()
        x=self
        while x.p is not None and x.p.right is x:
            x=x.p
        return x.p

class BST():
    def __init__(self):
        self.root=None
    def inorder(self):
        if self.root is not None:
            self.root.inorder()
            print
        else:
            print 'empty BST'
    def search(self,k):
        if self.root is None:
            return None
        else:
            return self.root.search(k)
    def search_iterative(self,k):
        x=self.root
        while x is not None and x.key!=k:
            if k<x.key:
                x=x.left
            else:
                x=x.right
        return x
    def insert(self,k): #value k, not node
        y=None
        x=self.root
        while x is not None:
            y=x
            if k<x.key:
                x=x.left
            else:
                x=x.right
        new=node(p=y,key=k)
        if y is None:
            self.root=new
        else:
            if new.key<y.key:
                y.left=new
            else:
                y.right=new
        return new
    def delete(self,z):
        if z.left is None and z.right is None:
            if z is self.root:
                self.root=None
            else:
                if z.p.left is z:
                    z.p.left=None
                else:
                    z.p.right=None
        elif z.left is not None and z.right is None or\
             z.left is None and z.right is not None:
            if z is self.root:
                x=z.left or z.right
                self.root=x
                x.p=None
            else: #z is not self.root
                x=z.left or z.right
                x.p=z.p
                if z is z.p.left:
                    z.p.left=x
                else:
                    z.p.right=x
        else: #both child exist
            y=z.successor()
            x=y.left or y.right
            if x is not None:
                x.p=y.p
            if y is y.p.left:
                y.p.left=x
            else:
                y.p.right=x
            z.key=y.key

if __name__=='__main__':
    tree=BST();
    A=[15,5,16,3,12,20,10,13,18,23,6,7]
    #A=[2,1,3]
    for i in A:
        tree.insert(i)
    print 'tree inorder:'
    tree.inorder()
    z=tree.search(5)
    if z is not None:
        tree.delete(z)
    print 'deleted 5:'
    tree.inorder()


