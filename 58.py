def lengthOfLastWord(s: str) -> int:
    word = ''
    words = []
    last_word = ''
    s = s.strip()
    for i in range(len(s)):
        if s[i] != ' ' and i+1 == len(s): 
            word+=s[i]
            words.append(word)
        elif s[i] != ' ':
            word+=s[i]   
        elif word != '' and last_word != ' ':
            words.append(word)
            word=''
        last_word = s[i]
        print(s[i])
        print(words)
    

lengthOfLastWord("   fly me   to   the moon  ")