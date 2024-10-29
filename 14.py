def longestCommonPrefix(strs):
    prefix = ''
    shortest_strs = 0
    for i in range(len(strs[0])):
        if len(strs[0]) == i:
            return prefix
        for j in range(len(strs[1])):
            if len(strs[1]) == j:
            return prefix
            for k in range(len(strs[2])):
                if len(strs[2]) == k:
                    return prefix
                if strs[0][i] == strs[1][j] == strs[2][k]:
                    prefix+=strs[0][i]
    return prefix 

prefix = longestCommonPrefix(["flower","flow","flight"])
print(prefix)
