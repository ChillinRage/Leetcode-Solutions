def maxArea(height):
    maxm = 0
    left = 0 ; right = len(height)-1
    
    while left < right:
        area = min([height[left],height[right]])*(right-left)
        
        if area > maxm:
            maxm = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
            
    return maxm
