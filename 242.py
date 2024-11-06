def isAnagram(s: str, t: str) -> bool:
        queueS = []
        queueN = []
        if len(s) > len(t) or len(t) > len(s): 
            return False
        for i in range(len(t)):
            queueS.append(t[i])
            print(f"queue da iteração {i} : {queueS}")
            print(f"first: {s[i]}, second: {t[i]}")
            if s[i] in queueS:
                queueS.remove(s[i])
            else:
                queueN.append(s[i])
            print(f"queueS após remoção: {queueS}")
        for i in range(len(queueN)):
            if queueN[i] in queueS:
                queueS.remove(queueN[i])
        print(s)
        print(queueS)
        if queueS == []:
            return True
        return False

print(isAnagram("anagram", "nagaram"))