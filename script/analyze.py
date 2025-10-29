from utils import directread, fileread, typeread

def nucleic(type, sequence):
    print (type, sequence)

def protein(sequence):
    print ("Protein", sequence)

def analyze(mode):
    if mode == 0:
        seqcount, sequence = directread()
    elif mode == 1:
        seqcount, sequence = fileread()

    for i in range(seqcount):
        type = typeread(sequence[i])
        if type == "DNA" or "RNA" :
            nucleic(type, sequence[i])
        else :
            protein(sequence[i])