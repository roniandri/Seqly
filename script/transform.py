import textwrap
import warnings
from Bio.Seq import Seq
from Bio import BiopythonWarning
from utils import directread, fileread, typeread
warnings.simplefilter("ignore", BiopythonWarning)

def transcribe_func(sequence, i):
    dna_seq = Seq(sequence)
    rna_coding = dna_seq.transcribe()
    rna_template = dna_seq.reverse_complement().transcribe()

    if i != 0:
        print(f"\n> Sequence number {i+1}")
    else:
        print(f"> Sequence number {i+1}")
    print("5'3'")
    for line1 in textwrap.wrap(str(rna_coding), width=60):
        print(line1)
    print("3'5'")
    for line2 in textwrap.wrap(str(rna_template), width=60):
        print(line2)

def translate_func(sequence, type, i):
    if i != 0:
        print(f"\n> Sequence number {i+1}")
    else:
        print(f"> Sequence number {i+1}")

    sequence = Seq(sequence)

    for frame in range(3):
        sub_seq = sequence[frame:]
        if type == "DNA":
            sub_seq = sub_seq.transcribe()
        protein = sub_seq = sub_seq.translate(to_stop=False)
        print(f"5'3' Frame {frame+1}")
        for line in textwrap.wrap(str(protein), width=60):
            print(line)
    
    rev_seq = sequence.reverse_complement()
    for frame in range(3):
        sub_seq = rev_seq[frame:]
        if type == "DNA":
            sub_seq = sub_seq.transcribe()
        protein = sub_seq.translate(to_stop=False)
        print(f"3'5' Frame {frame+1}")
        for line in textwrap.wrap(str(protein), width=60):
            print(line)


def transform(mode, command):
    if mode == 0:
        seqcount, sequence = directread()
    elif mode == 1:
        seqcount, sequence = fileread()
    
    for i in range(seqcount):
        seq_type = typeread(sequence[i])
        if command == 0:
            if seq_type == "DNA":
                transcribe_func(sequence[i], i)
            else :
                print("Transcribe can only be done if the sequence is DNA.")
        elif command == 1:
            if seq_type in {"DNA", "RNA"}:
                translate_func(sequence[i], seq_type, i)
            else :
                print("Translate can only be done if the sequence is DNA or RNA.")