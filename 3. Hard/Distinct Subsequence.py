def numDistinct(s, t):
    def iter(mem, s_index, t_index):
        if t_index == t_length:
            return 1
        elif s_index == s_length:
            return 0
        
        #length of current t >= length of current s
        #no need to iterate, compare equal
        elif (s_length - s_index) <= (t_length - t_index):
            return int(s[s_index:] == t[t_index:])
        
        else:
            if mem[s_index][t_index] != -1:
                return mem[s_index][t_index]
            else:
                count = 0
                for i in range(s_index, s_length):
                    if s[i] == t[t_index]:
                        count += iter(mem, i + 1, t_index + 1)
                    
                mem[s_index][t_index] = count
                return count
            
    s_length = len(s)
    t_length = len(t)
    mem = [[-1 for i in range(t_length)] for j in range(s_length)]
    return iter(mem, 0, 0)
