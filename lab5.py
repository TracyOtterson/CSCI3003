#Lab5 Part 1 Practice with Functions
#Write a function to check if a string is valid.  A Homo sapiens locus needs to 
#have the following format:  A number between 1 to 23 or a X or Y, a 'p' or 'q',
#a band number, a period, and a sub_band number
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

#(1)Checking to see if function returns true for valid loci.
assert is_valid_humanlocus('6p21.3'), 'This is not a valid locus.'

assert is_valid_humanlocus('11q1.4'), 'This is not a valid locus.'

assert is_valid_humanlocus('22p11.2'), 'This is not a valid locus.'
#None of the assertion statements triggered, so code is valid for purpose.

#(2)Checking to see if function returns false for invalid loci.
assert is_valid_humanlocus('chr1:1000'), 'This is not a valid locus.'

assert is_valid_humanlocus('nonsense'), 'This is a not valid locus.'

assert is_valid_humanlocus('2a11p'), 'This is a not valid locus.'
#None of the assertion statements triggered, so code is valid for purpose.


#(3)This is checking to see if chromosome number is out of range.  Inputing 24 
#instead of between 1 to 23.
assert is_valid_humanlocus('24p21.3'), 'This is not a valid locus.'

#This is checking to see if a letter besides p or q are used as chromosome arm info:
assert is_valid_humanlocus('20r2.10'), 'This is not a valid locus.'

    
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
    
    

#Part II Analyzing SNP Data and addin them into separate lists (no dictionary)
GregMendel = open('GregMendel_SNPs.txt', 'rt')
Gregid = []
GregChr = []
GregPosition = []
GregSNP1 = []
GregSNP2 = []
Buffer = ''
offset = 0
for line in GregMendel:
    Gregid.append(line[:line.find('c')])
    offset = line.find('chr') + 3
    Buffer = line[offset:offset+2]  
    if not Buffer[1].isnumeric():
        Buffer = Buffer[0:1]
    GregChr.append(int(Buffer))
    GregPosition.append(int(line[offset + len(Buffer) + 1:line.find('(')]))
    GregSNP1.append(line[-5])
    GregSNP2.append(line[-3])
GregMendel.close()


#Create a function read_SNP_file to read in SNPfiles and parse the data for input
#files
def read_SNP_file(filename):
    infile = open(filename, 'rt')
    temp_dict = {'id':[], 'Chr':[], 'Position':[], 'Bases':[]}
    SNP1 = ''
    SNP2 = ''
    Buffer = ''
    offset = 0
    for line in infile:
        temp_dict['id'].append(line[:line.find('c')])
        offset = line.find('chr') + 3
        Buffer = line[offset:offset+2]  
        if not Buffer[1].isnumeric():
            Buffer = Buffer[0:1]
        assert Buffer.isdigit() and (1 <= int(Buffer) <= 22), "This chromosome number is invalid!" +Buffer
        temp_dict['Chr'].append(int(Buffer))
        temp_dict['Position'].append(int(line[offset + len(Buffer) + 1:line.find('(')]))
        SNP1 = (line[-5])
        SNP2 = (line[-3])
        temp_dict['Bases'].append(SNP1 + SNP2)
    infile.close()
    return temp_dict
   
    
#Testing the assertion using an invalid chromosome number
#InvalidSNP = read_SNP_file('testSNPfile.txt')

#Reading in Greg Mendel's data and stroing as Greg dictionary
Greg_dict = read_SNP_file('GregMendel_SNPs.txt')


#Reading in Lilly Mendel's data and storing as Lilly dictionary
Lilly_dict = read_SNP_file('LillyMendel_SNPs.txt')




#Part C Iterate through the list to find identical SNP's in Chromosome 10 and compare SNPs to each other from Lilly and Greg
#Determine longest region of similarity of SNP's in Chromosome 10
#Print maxstart and maxend and print maxlength
maxstart = -10
maxend = -10
maxlength = -5
startindex = -5
endindex = 5
count = 0
length = 0
Greglist = Greg_dict['Position']
Lillylist = Lilly_dict['Position']
for i in range(len(Greglist)):
    if Greg_dict['Chr'][i] == 10: 
        if Greg_dict['Bases'][i] == Lilly_dict['Bases'][i]:
            if (count == 0):
                startindex = 0
                count += 1
            else:
                count += 1
        else:
            endindex = (i - 1)
            length = (Greglist[endindex] - Greglist[startindex]) +1
    else:
        continue
    if maxlength < length:
        maxstart = startindex
        maxend = endindex
        maxlength = length
    else:
        count = 0
        
        


print('(',maxstart,',',maxend,')')
print(maxlength)      
    
    
    
            
            
        

    
        







        
   
    
        

          
    

    
    
