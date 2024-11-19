import messenger_rna_to_Protein_using_class
class Sequence:
    def __init__(self, seq="Provide Sequence", function="Write Function"):
        self.seq = seq
        self.function = function

    def get_sequence_info(self):
        print(self.seq)
        print(self.function)

    def __str__(self):
        return f"{self.seq}\t{self.function}"

class Exon(Sequence):
    def __init__(self, seq, function, posi="Located at"):
        super().__init__(seq, function)
        self.posi = posi

    def get_exon_info(self):
        print(self.seq, self.function, self.posi)

class Protein(Exon):
    def __init__(self, seq, function, posi, protein_len="Length Is"):
        super().__init__(seq, function, posi)
        self.protein_len = protein_len

    def print_protein_info(self):
        print(self.seq, self.function, self.posi, self.protein_len)

# Example:
protein = Protein('ATGC', 'Proline', 321, 543)
protein.print_protein_info()
mrna_sequence = "AUGUUUCAUAA"
print("Protein sequence:", protein_sequence)