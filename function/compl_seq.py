def print_complementary_dna(dna_sequence):
    complementary_sequence = ""
    
    for base in dna_sequence.upper():  
        if base == 'A':
            complementary_sequence += 'T'
        elif base == 'T':
            complementary_sequence += 'A'
        elif base == 'C':
            complementary_sequence += 'G'
        elif base == 'G':
            complementary_sequence += 'C'
    
    # complementary sequence
    print("Complementary DNA sequence: ", complementary_sequence)

# Input DNA sequence
dna_sequence = "atcGta"

print("Original DNA sequence: ", dna_sequence)

print_complementary_dna(dna_sequence)
