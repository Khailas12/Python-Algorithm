from data_structures.binary_tree import BinaryTree


def pre_order_search(target, root):  # checks in the beginning
    if root:
        
        if root.data == target:
            return True
        
        if pre_order_search(target, root.left):
            return True
    
        if pre_order_search(target, root.right):
            return True
        
    return False

def post_order_search(target, root): # checks in the end
    if root:
        
        if post_order_search(target, root.left):
            return True
        
        if post_order_search(target, root.right):
            return True
        
        if root.data == target:
            return True
        
    return False

def in_order_search(target, root):  # checks in the middle
    if root:
        
        if in_order_search(target, root.left):
            return True
        
        if root.data == target:
            return True
        
        if in_order_search(target, root.right):
            return True
        
    return False
            
            
def search(args):
    bt = BinaryTree()
    
    print("\nBuilding Tree...")
    bt.create_from_file(args.file)
    print("Tree built!\n")
    
    if args.order == "pre-order":
        print("\nSearching tree...\n")
        
        target = args.word
        if pre_order_search(target, bt.root):
            print("Word found")
            return
        else:
            print("Word not found")
            return
            
    if args.order == "post-order":
        print("Searching tree...")
        target = args.word
        
        if post_order_search(target, bt.root):
            print("Word found :)")
            return
        else:
            print("Word not found :(")
            return 
            
    if args.order == "in-order":
        print("Searching tree...")
        target = args.word
        
        if in_order_search(target, bt.root):
            print("word found!")
            return
        else:
            print("word not found!")
            return      
            
    print("depth-first-search can only be used with --order 'pre-order', 'post-order', or 'in-order'")
    

# https://www.youtube.com/watch?v=gPMU_Kob_ac&list=PL7g1jYj15RUMeIY778b8lvgUzdRFnEniI&index=9
