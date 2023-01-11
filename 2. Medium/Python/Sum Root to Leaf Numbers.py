def sumNumbers(root, num = ''):
        if not root:  # empty root
            return 0
        elif not (root.left or root.right):  # current root is a leaf
            return int(num + str(root.val))
        else:
            num += str(root.val)
            return sumNumbers(root.left, num) + sumNumbers(root.right, num)
