
def romanToInt(s: str) -> int:
    count = 0
    roman_list = [x for x in s]
    print(roman_list)
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    N = len(roman_list)

    for i in range(N+1):
        test = roman_numerals[roman_list[i]]
        if i >= N-1:
            count += roman_numerals[roman_list[i]]
            return count
        if roman_numerals[roman_list[i]] >= roman_numerals[roman_list[i+1]]:
            count += roman_numerals[roman_list[i]]
        else:
            count -= roman_numerals[roman_list[i]]

    return count


numeral = "MCMXCIV"
print(romanToInt(numeral))
