## Assert and function
assert 1 == 1
print('Assert successful')


def dummy_func(num):
    """
    Input: Number
    Converts a number to boolean and returns that.
    Output: True or False
    """
    return bool(num)

# help (dummy_func)
assert(dummy_func(1))
assert(dummy_func(-1))
assert(dummy_func(0))

# Another function
def string_check(string):
    if '.' in string:
        return True
    return False

assert('1.23')
assert('2.')
assert('2')

## List sorting
A = [1, 5, 2, 4, 3]
A.sort() # increasing
A.sort(reverse = True) # decreasing

## Some string functions
# isdigit(), replace()
# -------------------------
A = '12'
print('Is 12 a digit: ', A.isdigit())

B = '1b232'
print('Before: ', B)
B = B.replace('b', 'p')
print('After: ', B)

# and, or
# -------------------------
# (1 == 1) and (1 == 2)
# (1 == 1) or (1 == 2)
num = 2
if (1 <= num <= 5):
    print(num, ' is >= 1 and <= 5')
    
if (num > 0 and num < 24):
    print(num, 'is > 0 and < 24')
    
## Dictionary
# ------------------------- 
tmp_dict = {}
tmp_key = 'A1BG'
tmp_val = 10

# Putting value (key-value pair) inside dictionary
tmp_dict[tmp_key] = tmp_val

# printing the value using key
print(tmp_key, ':', tmp_dict[tmp_key])

# Updating the value
tmp_dict['A1BG'] = 20

# Insert some other values
tmp_dict['BRCA'] = 15
tmp_dict['TP53'] = 25


# Printing key, value pairs
# tmp_dict.keys() doesn't return a list
# print(tmp_dict.keys()) 
# dict_keys(['A1BG', 'BRCA', 'TP53'])
keys = list(tmp_dict.keys())
for i in keys:
    print(i, ':', tmp_dict[i])
    
for key, value in tmp_dict.items():
    print(key, ':', value)