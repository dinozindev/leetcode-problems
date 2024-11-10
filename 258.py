def addDigits(num: int) -> int:
        print(f'numero atual: {num}')
        actual_num = str(num)
        sum = 0
        if num < 10:
            return num
        for digit in actual_num:
            sum+=int(digit)
        print(f'soma: {sum}')
        if sum > 9:
             print(f'entrou: {sum}')
             return addDigits(sum)
        return sum

print(addDigits(32))