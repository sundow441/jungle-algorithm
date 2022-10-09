from sys import stdin

stdin = open('inputfile.txt','r')
N = int(stdin.readline().strip())
tree = {}
for n in range(N):
    root, lc, rc = stdin.readline().strip().split()
    tree[root] = [lc, rc]

def preorder(root):
    if root != ".":
        print(root, end="") #root
        preorder(tree[root][0]) #l
        preorder(tree[root][1]) #r

def inorder(root):
    if root != ".":
        inorder(tree[root][0]) #l
        print(root, end="") #root
        inorder(tree[root][1]) #r

def postorder(root):
    if root != ".":
        postorder(tree[root][0]) #l
        postorder(tree[root][1]) #r
        print(root, end="") #root

preorder('A')
print()
inorder('A')
print()
postorder('A')
            