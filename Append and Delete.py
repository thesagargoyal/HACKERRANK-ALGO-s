def appendAndDelete(s, t, k):
    l1 = len(s)
    l2 = len(t)

    if l1 + l2 < k:
        return 'Yes'

    chk = 0
    for sl, tl in zip(s, t):
        if sl == tl: 
            chk += 1
        else: 
            break
   
    es = l1 - chk
    et = l2 - chk
    dif = es + et

    if dif <= k and dif % 2 == k % 2:
         return 'Yes'
    return 'No'