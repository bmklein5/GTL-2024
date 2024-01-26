def celsius_to_fahrenheit(temp_c):
    """"""
    return 9/5 * temp_c + 32

def fahrenheit_to_celsius(temp_f):
    """"""
    return (temp_f - 32) * 5/9

# write any custom tests/prints you want here

# TEST CASES
assert(abs(celsius_to_fahrenheit(0) - 32) < 0.001)
assert(abs(celsius_to_fahrenheit(-20) - -4) < 0.001)
assert(abs(celsius_to_fahrenheit(20) - 68) < 0.001)
assert(abs(fahrenheit_to_celsius(32)) < 0.001)
assert(abs(fahrenheit_to_celsius(100) - 37.7778) < 0.001)
assert(abs(fahrenheit_to_celsius(-30) - -34.4444) < 0.001)

