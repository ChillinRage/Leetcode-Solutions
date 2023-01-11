def combine(n, k):
    def iter(combi, m):
        if m == k:
            return combi
            
        output = []
        for each in combi:
            if each[-1] == n:
                continue
            else:
                for i in range(each[-1] + 1, n + 1):
                    output.append(each + [i])
                        
        return iter(output, m + 1)
        
    return iter([[i] for i in range(1, n + 1)], 1)
