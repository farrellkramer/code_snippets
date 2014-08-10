# Swaps keys, values in dictionary

test = {'a': 'apple', 'b': 'boy', 'c': 'cat'}
swapped = dict((v, k) for k, v in test.items())
print swapped # This just tests the swap