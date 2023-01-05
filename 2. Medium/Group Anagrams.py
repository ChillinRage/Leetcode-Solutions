def groupAnagrams(strs):
    track = {}
    
    for s in strs:
        main = ''.join(sorted(s))
        
        if main not in track:
            track[main] = []
        track[main].append(s)
        
    return list(track.values())
