#!/ifs9/BC_B2C_01A/B2C_SGD/SOFTWARES/anaconda3/bin/python
## -*- coding = utf-8 -*-
import os
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

f = open('/ifs7/B2C_SGD/PROJECT/PP12_Project/analysis_pipeline/HPC_chip/db/aln_db/hg19/hg19_chM_male_mask.fa')
seq={}
a = f.readlines()
b = ''.join(a)
c = b.split('>')
dic ={}
for i in range(len(c)):
    x = c[i].split('\n')
    seq = ''
    chrom = x[0]
    seq = ''.join(x[1:])
    dic[chrom] = seq 
f.close()
for key in dic:
    print(key)
f = open(input_file)
fw = open(output_file, 'w')
def countgc(seq):
    sum = 0
    for i in range(len(seq)):
        if seq[i] == 'c' or seq[i] == 'C':
            sum = sum +1
        if seq[i] == 'g' or seq[i] =='G':
            sum = sum +1
    ratio = sum/len(seq) 
    result = "{:.2f}".format(ratio)
    return result
for line in f:
    line = line.strip()
    line = line.split('\t')
    chrom = line[0]
    start = int(line[1])
    end = int(line[2])
    seq = dic[chrom][start:end+1]
    num_gc = countgc(seq)
    order = "%s\t%s\t%s\t%s\n" %(chrom, start, end, num_gc)
    fw.write(order)
f.close()
fw.close()
