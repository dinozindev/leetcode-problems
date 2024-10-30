def plusOne(digits):
        integer = ''
        list_digits = []
        for digit in digits:
            digit = str(digit)
            integer+=digit
        integer = int(integer)
        integer+=1
        for number in str(integer):
            list_digits.append(int(number))
        return list_digits

print(plusOne([1,2,3]))