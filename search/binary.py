from data_structures.binary_tree import BinaryTree


def binary_search(target, root):
    if root:
        
        if int(root.data) == int(target):
            return True

        if int(root.data) < int(target):
            if binary_search(target, root.right):
                return True

        if int(root.data) > int(target):
            if binary_search(target, root.left):
                return True
        
    
    
def search(args):
    bst = BinaryTree()

    print("\nBuilding tree...")
    bst.create_bst_from_file(args.file)
    print("Tree built!\n")
    print("Searching tree...")
    
    target = args.word
    if binary_search(target, bst.root):
        print("Word Found :D")    
        return
    else:
        print("Word not found D:")
        



# https://www.youtube.com/watch?v=Vnk2RiLsBEM&list=PL7g1jYj15RUMeIY778b8lvgUzdRFnEniI&index=6
