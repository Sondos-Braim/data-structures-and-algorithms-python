def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        output = ''
        i = 0
        while  num > 0:
            print(num // val[i])
            for j in range(num // val[i]):
                output += roman[i]
                num -= val[i]
            i += 1
        return output

print(int_to_Roman(1995))