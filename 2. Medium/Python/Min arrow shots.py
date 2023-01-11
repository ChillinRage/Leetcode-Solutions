def findMinArrowShots(points):
        points.sort(key = lambda x: x[1])  # sort by ascending end points
        end   = points[0][1] # the end point of current overlap
        count = 0
        
        for i in range(1, len(points)):
            if end >= points[i][0]: # overlap
                continue
            
            else: # no overlap, find next balloon's end point.
                count += 1
                end    = points[i][1]
        
        return count + 1 # + 1 for final balloon.
