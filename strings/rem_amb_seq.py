# write aProgram to remove ambiguous character from DNA sequence.

# Original DNA sequence
dna_sequence = "ATGCNNGATGC"

# Create a translation table to remove ambiguous characters (N in this case)
translation_table = str.maketrans("", "", "N")

# Translate the DNA sequence using the translation table
cleaned_dna_sequence = dna_sequence.translate(translation_table)

print(cleaned_dna_sequence)  # Output: ATGCGATGC