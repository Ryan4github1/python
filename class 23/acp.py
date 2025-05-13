test_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20, 'f': 40}

value_freq = {}
for value in test_dict.values():
    value_freq[value] = value_freq.get(value, 0) + 1

print(value_freq)