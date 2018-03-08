def is_valid_humanlocus(string):
    '''This is designed to validate the input of a human locus gene.'''
    chromosome = 0
    fields = []
    fields2 = []
    bandnumber = 0
    subbandnumber = 0
    name = ''
    if 'p' in string:
        fields = string.split('p')
        if not fields[0].isdigit():
            return False
        chromosome = int(fields[0])
        name = fields[1]
    elif 'q' in string:
        fields = string.split('q')
        chromosome = int(fields[0])
        name = fields[1]
    else:
        return False
    if not(1 <= chromosome <= 23):
        return False
    if '.' in name:
        fields2 = name.split('.')
        if not fields2[0].isdigit():
            return False
        if not fields2[1].isdigit():
            return False
        bandnumber = int(fields2[0])
        if bandnumber >= 0:
            return True
        subbandnumber = int(fields2[1])
        if subbandnumber >= 0:
            return True
    return False
  
    
#Checking to see if function returns true for valid loci.
assert is_valid_humanlocus('6p21.3'), 'This is not a valid locus.'

assert is_valid_humanlocus('11q1.4'), 'This is not a valid locus.'

assert is_valid_humanlocus('22p11.2'), 'This is not a valid locus.'
#None of the assertion statements triggered, so code is valid for purpose.

#Checking to see if function returns false for invalid loci.
assert is_valid_humanlocus('chr1:1000'), 'This is not a valid locus.'

assert is_valid_humanlocus('nonsense'), 'This is a not valid locus.'

assert is_valid_humanlocus('2a11p'), 'This is a not valid locus.'
#None of the assertion statements triggered, so code is valid for purpose.

#2 addtional assertion statements that should check invalid examples and why 
#they were chosen (printed as an assertian statement)

#This is checking to see if chromosome number is out of range.  Inputing 24 
#instead of between 1 to 23.
assert is_valid_humanlocus('24p21.3'), 'This is not a valid locus.'

#This is checking to see if a letter besides p or q are used as chromosome arm info:
assert is_valid_humanlocus('20r2.10'), 'This is not a valid locus.'    

#If statements designed to print if input is valid or not:
if is_valid_humanlocus('6p21.3'):
    print('This is a valid input.')
else:
    print('Not a valid input.')
                
if is_valid_humanlocus('11q1.4'):
    print('This is a valid input.')    
else:
    print('Not a valid input.')           
    
if is_valid_humanlocus('22p11.2'):
    print('This is a valid input.')
else:
    print('Not a valid input.')
    
if is_valid_humanlocus('chr1:1000'):
    print('This is a valid input.')
else:
    print('Not a valid input.')
    
if is_valid_humanlocus('nonsense'):
    print('This is a valid input.')
else:
    print('Not a valid input.')
    
if is_valid_humanlocus('2a11p'):
    print('This is a valid input.')
else:
    print('Not a valid input.')
    
#Part b Write a function to check if a human locus is on short arm (p)
def is_locus_onshortarm(string):
    if is_valid_humanlocus(string) and 'p' in string:
        return True
    return False

#Checking to see if this works with if statements.
if is_locus_onshortarm('6p21.3'):
    print('This is on the short arm.')
else:
    print('This is not on the short arm.')
    
if is_locus_onshortarm('11q1.4'):
    print('This is on the short arm.')
else:
    print('This is not on the short arm.')
    
    
#Alternate function written with Darnell
def is_valid_humanlocus(string):
    '''This is designed to validate the input of a human locus gene.'''
    offset = 0
    if string[0].isdigit():
        if string[1].isdigit():
            if int(string[:2]) <= 23:
                offset += 2
        elif int(string[0]) >= 1:
            offset += 1
    elif string[0] in 'XY':
        offset += 1
    else:
        return False
    if string[offset] in 'pq':
        offset += 1
        if string[offset].isdigit():
            if string[offset+1].isdigit():
                offset += 2
            else:
                offset += 1
    else:
        return False
    if string[offset] == '.':
        offset += 1
    else:
        return False
    if string[offset].isdigit():
        return True
    return False
