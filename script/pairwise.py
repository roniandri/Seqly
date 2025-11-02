from Bio.Align import PairwiseAligner, substitution_matrices
from itertools import combinations
from .utils import directread, fileread, typeread

def pairwise_nucleotide(sequence, model):
    aligner = PairwiseAligner()
    aligner.mode = model
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -0.5

    pairs = list(combinations(range(len(sequence)), 2))

    results = []
    for i, j in pairs:
        seq1 = str(sequence[i]).upper()
        seq2 = str(sequence[j]).upper()

        alignment = aligner.align(seq1, seq2)[0]
        results.append(((i+1, j+1), alignment.score))

        print(f"\n> Pair {i+1}-{j+1}")
        print(alignment)
        print(f"Score: {alignment.score:.2f}")

    return results

def pairwise_protein(sequence, model):
    aligner = PairwiseAligner()
    aligner.mode = model
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    
    valid_protein_letters = "ACDEFGHIKLMNPQRSTVWYBXZ"
    def clean_sequence(seq):
        seq = str(seq).upper()
        cleaned = "".join([c for c in seq if c in valid_protein_letters])
        return cleaned

    pairs = list(combinations(range(len(sequence)), 2))
    results = []
    
    for i, j in pairs:
        seq1 = clean_sequence(sequence[i])
        seq2 = clean_sequence(sequence[j])

        alignment = aligner.align(seq1, seq2)[0]
        results.append(((i+1, j+1), alignment.score))

        print(f"\n> Pair {i+1}-{j+1}")
        print(alignment)
        print(f"Score: {alignment.score:.2f}")

    return results

def pairwise(mode):
    if mode == 0:
        _, sequence = directread()
    elif mode == 1:
        _, sequence = fileread()
    
    modeler = input("(1. Needleman-Wunsch 'global') or (2. Smith-Waterman 'local') please type 1 or 2\nModel=> ") or "1"
    if modeler in {"1", "2"}:
        if modeler == "1":
            model = "global"
        elif modeler == "2":
            model = "local"
    else :
        print("Model not recognized.")
        return

    seq_types = [typeread(seq) for seq in sequence]

    if not all(t in {"DNA", "RNA", "Protein"} for t in seq_types):
        print("Pairwise can only be done if the sequence is DNA, RNA or Protein.")
        return

    if all(t in {"DNA", "RNA"} for t in seq_types):
        pairwise_nucleotide(sequence, model)
    else:
        pairwise_protein(sequence, model)