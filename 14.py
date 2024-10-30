def longestCommonPrefix(strs):
    prefix = ''
    possible_prefixes = []
    shortest_str = min(len(string) for string in strs)
    for j in range(len(strs)):
        for i in range(shortest_str):
            if shortest_str == i:
                return prefix
            prefix+=strs[j][i]
        possible_prefixes.append(prefix)
        prefix = ''
    if '' in possible_prefixes:
        return prefix
    print(possible_prefixes)
    for k in range(len(possible_prefixes)):
        for l in range(shortest_str):
            print(l)
            if shortest_str-1 == l:
                return prefix
            if possible_prefixes[k][l] in list(possible_prefixes[k+1:][k][l]):
                prefix+=possible_prefixes[k][l]
            elif possible_prefixes[k][l] in prefix and possible_prefixes[k][l] not in list(possible_prefixes[k+1:][k][l]):
                prefix-=possible_prefixes[k][l]
            print(list(possible_prefixes[k+1:]))
            print(prefix) 
    return prefix

prefix = longestCommonPrefix(["flower","flow","flight"])
print(prefix)

["flower","flow","flight"]
["dog","racecar","car"]