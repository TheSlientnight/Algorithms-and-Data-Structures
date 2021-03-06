def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


print(to_str(211, 2))
print(to_str(211, 8))
print(to_str(211, 16))
