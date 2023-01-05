import re

def strStr(haystack, needle):
    if needle == '':
        return 0
    if needle not in haystack:
        return -1
        
    return re.search(needle,haystack).start()
