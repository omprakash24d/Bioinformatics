dna='''GGCATGAAAGTCAGGGCAGAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAAC
CTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGT
GAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAG
ACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCTGATAGGCACTGACTCTCTCTGC
CTATTGGTCTATTTTCCCACCCTTAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCT
TTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCT
CGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTG
CACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGGTGAGTCTATGGGACCCTTGATGTTTTCTTT
CCCCTTCTTTTCTATGGTTAAGTTCATGTCATAGGAAGGGGAGAAGTAACAGGGTACAGTTTAGAATGGG
AAACAGACGAATGATT'''
dna1='GGCATGAAAGTCAGG'
print("The total length of the above DNA sequence is:",len(dna))
count_ATGC= dna.count('ATGC')
print("Total number of ATGC sequence in the given dna sequence is:",count_ATGC)
# calculate GC%
count_GC= dna.count('GC')
#total_dnalength= len.dna()
gcpercentage= (count_GC*100)/len(dna)
print('The total percentage of GC in the above dna is:', gcpercentage)
start_codon='ATG'
index= dna.find(start_codon)
print("Weather Stop Codon Found or not")
print("Start codon found at index:",index)
startcodon=dna.startswith('ATG')
print(startcodon)
stopcodon=dna.startswith('UUU')
print("Weather Stop Codon Found or not")
print(stopcodon)
print(dna1)
complementarty_dna= dna.replace('A', 'T').replace('G', 'C')
print("The Original DNA Sequence is:\n", dna)
print("The complimentary of above DNA Sequence is:\n",complementarty_dna)
