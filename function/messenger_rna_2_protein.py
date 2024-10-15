def translate_mrna_to_protein(mrna_sequence):
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
        'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L',
        'CUC': 'L', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H',
        'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R',
        'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N',
        'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S',
        'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
        'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G',
        'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    protein_sequence = ''.join(codon_table.get(mrna_sequence[i:i+3], 'X')
    for i in range(0, len(mrna_sequence), 3))
    print("Protein sequence:", protein_sequence)

# Example mRNA sequence
mrna_sequence = "AUGUUUCAUAA"
translate_mrna_to_protein(mrna_sequence)
