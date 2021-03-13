# string -> List of strings
# Returns list of permutations for input string
def perm_gen_lex(a):
    if a == '':
        return []
    if len(a) == 1: #returns a singular character 
         return [a]
    perm_lst = []

    
    for i in range(len(a)):
        #char is specific character that is going to be moved to the front
        char = a[i]
        #perm is the rest of string a that is going to be recursivly called 
        perm = perm_gen_lex(a[:i] + a[i+1:])
        for p in range(len(a)-1):
            if p == 0:
                #char is always first
                put = char + perm[p]
                perm.insert(p, put)
                perm_lst.append(perm[p])
            else:
                put = char + perm[p+1]
                perm.insert(p, put)
                perm_lst.append(perm[p])
    return perm_lst
    