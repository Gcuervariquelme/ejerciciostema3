def roman_to_decimal(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    prev_value = 0
    
    for char in reversed(roman_numeral):
        value = roman_values[char]
        if value < prev_value:
            decimal_num -= value
        else:
            decimal_num += value
        prev_value = value
    
    return decimal_num

    def count_digits(number):
        count = 0
        while number != 0:
            number //= 10
            count += 1
        return count
    def reverse_number(number):
        reversed_num = 0
        while number != 0:
            remainder = number % 10
            reversed_num = reversed_num * 10 + remainder
            number //= 10
        return reversed_num