def findAndReplacePattern(words, pattern):
        
    def match(word, pattern):
        if len(word) != len(pattern):
            return False
            
        diction1 = {s:'' for s in word}
        diction2 = {s:'' for s in pattern}
        for i in range(len(word)):
            if (diction1[word[i]] == '') or (diction2[pattern[i]] == ''):
                if (diction1[word[i]] == '') and (diction2[pattern[i]] == ''):
                    diction1[word[i]] = pattern[i]
                    diction2[pattern[i]] = word[i]
                else:
                    return False
            elif (diction1[word[i]] != pattern[i]):
                return False
            
        return True
        
    matches = []
    for word in words:
        if match(word, pattern):
            matches.append(word)
        
    return matches
