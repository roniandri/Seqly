from Bio import SeqIO
from Bio.Data import IUPACData
import os
import shlex

def fileread():
    file_paths = shlex.split(input("Input file(s)=> ").strip())
    file_format = input("Format=> ").strip().lower() or "fasta"

    all_sequences = []
    total_count = 0

    for file_path in file_paths:
        if "\\" not in file_path and "/" not in file_path:
            print(f"{file_path} bukan path file yang valid!")
            continue
        
        sequences = list(SeqIO.parse(file_path, file_format))
        all_sequences.extend([str(record.seq).upper() for record in sequences])
        total_count += len(sequences)
    
    return total_count, all_sequences


def directread():
    user_input = input("Input=> ").upper().strip()

    if not user_input:
        print("No sequences detected.")
        return
    
    if "\\" in user_input or "/" in user_input:
        print("Input detected as file path!")
        return

    list_sequence = user_input.split()

    return len(list_sequence), list_sequence

def typeread(sequence):
    seq_upper = sequence.upper()
    seq_set = set(seq_upper)

    rna_symbols = set(IUPACData.ambiguous_rna_values.keys())
    dna_symbols = set(IUPACData.ambiguous_dna_values.keys())
    protein_symbols = set("ACDEFGHIKLMNPQRSTVWYXBJZOU*")

    if seq_set.issubset(rna_symbols):
        return "RNA"
    elif seq_set.issubset(dna_symbols):
        return "DNA"
    elif seq_set.issubset(protein_symbols):
        return "Protein"
    else:
        return "Unknown sequence"

def help():
    here = os.path.dirname(__file__)
    help_path = os.path.join(here, "help.txt")
    
    with open(help_path, "r", encoding="utf-8") as f:
        print("\n")
        print(f.read())