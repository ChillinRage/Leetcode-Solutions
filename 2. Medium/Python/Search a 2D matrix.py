def searchMatrix(matrix, target):
    def binarySearch():
        l,r = 0,len(row)
        
        while l <= r:
            mid = (l+r)//2
            if target == row[mid]:
                return 1
            
            if target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return 0
        

    for row in matrix:
        if target > row[-1]:
            continue
        if target < row[0]:
            return 0
        if binarySearch():
            return 1
        
    return 0
