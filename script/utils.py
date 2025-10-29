from Bio import SeqIO

def fileread():
    file_path = input("Input=> ").strip().strip('"')
    file_format = input("Format=> ").strip()

    sequences = list(SeqIO.parse(file_path, file_format))
    list_sequence = [str(record.seq) for record in sequences]

    return len(sequences), list_sequence

def directread():
    list_sequence = input("Input=> ").upper().split()

    return len(list_sequence), list_sequence

def typeread(sequence):
    seqset =  set(sequence)
    if seqset.issubset({'A', 'C', 'G', 'T'}):
        return "DNA"
    elif seqset.issubset({'A', 'C', 'G', 'U'}):
        return "RNA"
    elif seqset.issubset({
        'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
        'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}):
        return "Protein"
    else:
        return "Unknown sequence"

def help():
    with open("help.txt", 'r', encoding='utf-8') as f:
        print("\n")
        print(f.read())