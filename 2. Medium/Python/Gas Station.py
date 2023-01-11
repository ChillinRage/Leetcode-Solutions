def canCompleteCircuit(gas, cost):
    def test_run(start):
        tank = 0
            
        for i in range(start, length):
            tank += gas[i] - cost[i]
                
            if tank < 0:
                return [False,i]
            
        for i in range(0, start):
            tank += gas[i] - cost[i]
                
            if tank < 0:
                return [False,i]
            
        return [True,i]
    
    length = len(gas)
    start  = 0
    far    = 0
        
    for i in range(length):
        if far > start:
            return -1
        
        run = test_run(start)
        
        if run[0]:
            return start
        else:
            if run[1] == length - 1:
                return -1
            else:
                start = run[1] + 1
                far = max(start, far)
                    
        
    return -1
