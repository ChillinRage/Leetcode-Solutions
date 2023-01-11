def canJump(self, nums):
        i, end = 0, len(nums)
        nums[-1] = 0
        while nums[i] != 0:
            if i + nums[i] >= (end-1):
                return 1
            print(i)
            next = nums[i+1: i+nums[i]+1]
            i += self.max_index(next)
        return i >= end-1
    
    @staticmethod
    def max_index(x):
        maxm = maxi = 0
        for i in range(len(x)):
            if x[i]+i >= maxm:
                maxm = x[i] + i
                maxi = i
        return maxi + 1
