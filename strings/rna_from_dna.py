# prompt: write a program to generate rna from a dna sequence using a string method only not use function

# Original DNA sequence
dna_sequence = "ATGCGATGC"

# Create a translation table for DNA to RNA conversion
translation_table = str.maketrans("T", "U")

# Translate the DNA sequence to RNA using the translation table
rna_sequence = dna_sequence.translate(translation_table)

print(rna_sequence)  # Output: AUGCNGAUGC