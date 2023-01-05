def lowestCommonAncestor(root, p, q):
    mapP = mapper(root,'',p)
    mapQ = mapper(root,'',q)
    node = root
    
    for i in range(len(mapP) if len(mapP)<len(mapQ) else len(mapQ)):
        if mapP[i] != mapQ[i]:
            return node
        
        node = (node.left if mapP[i]=="L" else node.right)
        
    return node
    
def mapper(cur,mapp,tar):
    if cur == tar:
        return mapp
    if not cur:
        return None
    
    return (mapper(cur.left,mapp+'L',tar) or mapper(cur.right,mapp+'R',tar))
