class Translator:
    def __init__(self):
        self.codon_table = {
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

    def translate(self, mrna_sequence):
        protein_sequence = ''.join(self.codon_table.get(mrna_sequence[i:i+3], 'X')
                                  for i in range(0, len(mrna_sequence), 3))
        return protein_sequence

# Example usage:
mrna_sequence = input("Enter the Sequence")
translator = Translator()
protein_sequence = translator.translate(mrna_sequence)
print("Protein sequence:", protein_sequence)