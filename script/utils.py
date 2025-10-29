from Bio import SeqIO
from Bio.Data import IUPACData

def fileread():
    file_path = input("Input=> ").strip().strip('"')
    file_format = input("Format=> ").strip().lower() or "fasta"

    sequences = list(SeqIO.parse(file_path, file_format))
    list_sequence = [str(record.seq) for record in sequences]

    return len(sequences), list_sequence

def directread():
    list_sequence = input("Input=> ").upper().split()

    return len(list_sequence), list_sequence

def typeread(sequence):
    seq_upper = sequence.upper()
    seq_set = set(seq_upper)

    rna_symbols = set(IUPACData.ambiguous_rna_values.keys())
    dna_symbols = set(IUPACData.ambiguous_dna_values.keys())
    protein_symbols = set("ACDEFGHIKLMNPQRSTVWYXBJZOU")

    if seq_set.issubset(rna_symbols):
        return "RNA"
    elif seq_set.issubset(dna_symbols):
        return "DNA"
    elif seq_set.issubset(protein_symbols):
        return "Protein"
    else:
        return "Unknown sequence"

def help():
    with open("help.txt", 'r', encoding='utf-8') as f:
        print("\n")
        print(f.read())