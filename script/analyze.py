import textwrap
from utils import directread, fileread, typeread

def nucleic(seq_type, sequence, i):
    data =[]
    if seq_type == "DNA":
        data = [
            ["Type",
             seq_type],
            ["Length",
             f"{len(sequence)} bp"],
            ["%A",
             f"{sequence.count('A')/len(sequence)*100:.3f}% ({sequence.count('A')}/{len(sequence)})"],
            ["%T", 
             f"{sequence.count('T')/len(sequence)*100:.3f}% ({sequence.count('T')}/{len(sequence)})"],
            ["%G", 
             f"{sequence.count('G')/len(sequence)*100:.3f}% ({sequence.count('G')}/{len(sequence)})"],
            ["%C", 
             f"{sequence.count('C')/len(sequence)*100:.3f}% ({sequence.count('C')}/{len(sequence)})"],
            ["AT%",
             f"{(sequence.count('A')+sequence.count('T'))/len(sequence)*100:.3f}%"],
            ["GC%",
             f"{(sequence.count('G')+sequence.count('C'))/len(sequence)*100:.3f}%"],
            ["AT Skew",
             f"{(sequence.count('A')-sequence.count('T'))/((sequence.count('A')+sequence.count('T'))):.3f}"],
            ["GC Skew",
             f"{(sequence.count('G')-sequence.count('C'))/((sequence.count('G')+sequence.count('C'))):.3f}"],
            ["Ambiguous",
             f"{sum(1 for b in sequence.upper() if b not in 'ATGC')/len(sequence)*100:.3f}% ({sum(1 for b in sequence.upper() if b not in 'ATGC')}/{len(sequence)})"]
        ]
    else :
        data = [
            ["Type",
             seq_type],
            ["Length",
             f"{len(sequence)} nt"],
            ["%A",
             f"{sequence.count('A')/len(sequence)*100:.3f}% ({sequence.count('A')}/{len(sequence)})"],
            ["%U", 
             f"{sequence.count('U')/len(sequence)*100:.3f}% ({sequence.count('U')}/{len(sequence)})"],
            ["%G", 
             f"{sequence.count('G')/len(sequence)*100:.3f}% ({sequence.count('G')}/{len(sequence)})"],
            ["%C", 
             f"{sequence.count('C')/len(sequence)*100:.3f}% ({sequence.count('C')}/{len(sequence)})"],
            ["AU%",
             f"{(sequence.count('A')+sequence.count('U'))/len(sequence)*100:.3f}%"],
            ["GC%",
             f"{(sequence.count('G')+sequence.count('C'))/len(sequence)*100:.3f}%"],
            ["AU Skew",
             f"{(sequence.count('A')-sequence.count('U'))/((sequence.count('A')+sequence.count('U'))):.3f}"],
            ["GC Skew",
             f"{(sequence.count('G')-sequence.count('C'))/((sequence.count('G')+sequence.count('C'))):.3f}"],
            ["Ambiguous",
             f"{sum(1 for b in sequence.upper() if b not in 'AUGC')/len(sequence)*100:.3f}% ({sum(1 for b in sequence.upper() if b not in 'AUGC')}/{len(sequence)})"]
        ]

    if i != 0:
        print("\n")
    print("="*47)
    loop_number = f"Sequences number {i+1}"
    for line in textwrap.wrap(loop_number, width=43):
        print(f"| {line:<43} |")
    print("="*47)
    for line in textwrap.wrap(sequence, width=43):
        print(f"| {line:<43} |")
    print("="*47)
    for row in data:
        print("| {:<15} | {:<25} |".format(*row))
    print("="*47)

def protein(sequence, i):
    seq = sequence.upper()
    aa_standard = "ACDEFGHIKLMNPQRSTVWYUO"
    aa_names = {
        'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe',
        'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys', 'L': 'Leu',
        'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg',
        'S': 'Ser', 'T': 'Thr', 'V': 'Val', 'W': 'Trp', 'Y': 'Tyr',
        'U': 'Sec', 'O': 'Pyl'
    }

    hydrophobic = "AILMFWV"
    polar = "STNQYCG"
    charged = "DEKRH"
    acidic = "DE"
    basic = "KRH"

    total_len = len(seq)
    amb_count = sum(1 for b in seq if b not in aa_standard)

    aa_stats = [
        [f"%{aa} ({aa_names[aa]})",
         f"{seq.count(aa)/total_len*100:.3f}% ({seq.count(aa)}/{total_len})"]
        for aa in aa_standard
    ]

    data = [
        ["Type", 
         "Protein"],
        ["Length", 
         f"{total_len} aa"],
        ["Ambiguous",
         f"{amb_count/total_len*100:.3f}% ({amb_count}/{total_len})"],
        ["Hydrophobic (%)",
         f"{sum(seq.count(a) for a in hydrophobic)/total_len*100:.3f}%"],
        ["Polar (%)",
         f"{sum(seq.count(a) for a in polar)/total_len*100:.3f}%"],
        ["Charged (%)",
         f"{sum(seq.count(a) for a in charged)/total_len*100:.3f}%"],
        ["Acidic (%)",
         f"{sum(seq.count(a) for a in acidic)/total_len*100:.3f}%"],
        ["Basic (%)",
         f"{sum(seq.count(a) for a in basic)/total_len*100:.3f}%"]
    ]

    if i != 0:
        print("\n")
    print("="*47)
    loop_number = f"Sequences number {i+1}"
    for line in textwrap.wrap(loop_number, width=43):
        print(f"| {line:<43} |")
    print("="*47)
    for line in textwrap.wrap(sequence, width=43):
        print(f"| {line:<43} |")
    print("="*47)
    for row in data:
        print("| {:<15} | {:<25} |".format(*row))
    print("="*47)
    for row in aa_stats:
        print("| {:<15} | {:<25} |".format(*row))
    print("="*47)

def analyze(mode):
    if mode == 0:
        seqcount, sequence = directread()
    elif mode == 1:
        seqcount, sequence = fileread()

    for i in range(seqcount):
        seq_type = typeread(sequence[i])
        if seq_type in {"DNA", "RNA"} :
            nucleic(seq_type, sequence[i], i)
        else:
            protein(sequence[i], i)