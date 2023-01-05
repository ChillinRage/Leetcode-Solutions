def permuteUnique(nums):
        return list(set(i for i in itertools.permutations(nums)))
