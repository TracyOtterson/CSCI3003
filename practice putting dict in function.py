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

    
GregMendel = read_SNP_file('GregMendel_SNPs.txt')
