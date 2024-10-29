def romanToInt(s: str):
        value = 0
        actual_combination = []
        previous_value = ''
        x = 1
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        } 
        for index, item in enumerate(s):
            if index+x == len(s):
                x = 0
            if [previous_value, s[index]] == actual_combination: 
                value+=0
            elif romans.get(s[index]) >= romans.get(s[index+x]):
                value+=romans[item]
            else:
                value+=romans.get(s[index+x]) - romans.get(s[index]) 
                actual_combination.clear()
                previous_value = s[index]
                actual_combination.append(s[index])
                actual_combination.append(s[index+x])
            print(f"Iteração {index}")
            print([previous_value, s[index]])
            print(value)
            print(actual_combination)

romanToInt("MCMXCIV")