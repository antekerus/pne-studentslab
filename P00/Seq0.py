from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta():
    filename = "sequences/U5.txt"
    file_contents = Path(filename).read_text()
    first_line_i = file_contents.find("\n")
    sequence = file_contents[first_line_i:]
    sequence = sequence.replace("\n", "")
    print("DNA file: ", )
    print(sequence[:20])


def seq_len():
    u5 = ""
    ada = ""
    frat1 = ""
    fxn = ""
    genes = [("sequences/U5.txt"), ("sequences/ADA.txt"), ("sequences/FRAT1.txt"), ("sequences/FXN.txt")]
    for i in range(0, 4):
        FILENAME = genes[i]
        file_contents = Path(FILENAME).read_text()
        first_line_i = file_contents.find("\n")
        sequence = file_contents[first_line_i:]
        sequence = sequence.replace("\n", "")
        if i == 0:
            u5 += sequence
        elif i == 1:
            ada += sequence
        elif i == 2:
            frat1 += sequence
        elif i == 3:
            fxn += sequence
    u5_length = len(u5)
    ada_length = len(ada)
    frat1_length = len(frat1)
    fxn_length = len(fxn)
    return u5_length, frat1_length, ada_length, fxn_length


def seq_count_base():
    genes = [("sequences/U5.txt"), ("sequences/ADA.txt"), ("sequences/FRAT1.txt"), ("sequences/FXN.txt")]
    for i in range(0, 4):
        u5 = ""
        ada = ""
        frat1 = ""
        fxn = ""
        c = 0
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        FILENAME = genes[i]
        file_contents = Path(FILENAME).read_text()
        first_line_i = file_contents.find("\n")
        sequence = file_contents[first_line_i:]
        sequence = sequence.replace("\n", "")
        if i == 0:
            u5 += sequence
            print("Gene U5:")
        elif i == 1:
            ada += sequence
            print("Gene ADA:")
        elif i == 2:
            frat1 += sequence
            print("Gene FRAT1:")
        elif i == 3:
            fxn += sequence
            print("Gene FXN:")
        while c < len(sequence):
            if sequence[c] == "A":
                count_a += 1
            elif sequence[c] == "C":
                count_c += 1
            elif sequence[c] == "G":
                count_g += 1
            elif sequence[c] == "T":
                count_t += 1
            c += 1
        print("A:", count_a)
        print("C:", count_c)
        print("T:", count_t)
        print("G:", count_g, "\n")


def seq_count():
    genes = [("sequences/U5.txt"), ("sequences/ADA.txt"), ("sequences/FRAT1.txt"), ("sequences/FXN.txt")]
    for i in range(0, 4):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        u5 = ""
        ada = ""
        frat1 = ""
        fxn = ""
        c = 0
        FILENAME = genes[i]
        file_contents = Path(FILENAME).read_text()
        first_line_i = file_contents.find("\n")
        sequence = file_contents[first_line_i:]
        sequence = sequence.replace("\n", "")
        if i == 0:
            u5 += sequence
            print("Gene U5:")
        elif i == 1:
            ada += sequence
            print("Gene ADA:")
        elif i == 2:
            frat1 += sequence
            print("Gene FRAT1:")
        elif i == 3:
            fxn += sequence
            print("Gene FXN:")
        while c < len(sequence):
            if sequence[c] == "A":
                d["A"] += 1
            elif sequence[c] == "C":
                d["C"] += 1
            elif sequence[c] == "G":
                d["G"] += 1
            elif sequence[c] == "T":
                d["T"] += 1
            c += 1
        print(d)


def seq_reverse():
    filename = "sequences/U5.txt"
    file_contents = Path(filename).read_text()
    first_line_i = file_contents.find("\n")
    sequence = file_contents[first_line_i:]
    sequence = sequence.replace("\n", "")
    new_seq = sequence[:20]
    print("Gene U5")
    print("Fragment:", new_seq)
    print("Reverse:", new_seq[::-1])

def seq_complement():
    filename = "sequences/U5.txt"
    file_contents = Path(filename).read_text()
    first_line_i = file_contents.find("\n")
    sequence = file_contents[first_line_i:]
    sequence = sequence.replace("\n", "")
    new_seq = sequence[:20]
    c = 0
    comp_seq = ""
    print("Gene U5:")
    print("Frag:", new_seq)
    while c < len(new_seq):
        if new_seq[c] == "A":
            comp_seq += "T"
        elif new_seq[c] == "C":
            comp_seq += "G"
        elif new_seq[c] == "G":
            comp_seq += "C"
        elif new_seq[c] == "T":
            comp_seq += "A"
        c += 1
    print("Comp:", comp_seq)

def most_frequent_base():
    import operator
    genes = [("sequences/U5.txt"), ("sequences/ADA.txt"), ("sequences/FRAT1.txt"), ("sequences/FXN.txt")]
    for i in range(0, 4):
        u5 = ""
        ada = ""
        frat1 = ""
        fxn = ""
        c = 0
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        FILENAME = genes[i]
        file_contents = Path(FILENAME).read_text()
        first_line_i = file_contents.find("\n")
        sequence = file_contents[first_line_i:]
        sequence = sequence.replace("\n", "")
        if i == 0:
            u5 += sequence
            print("Gene U5:")
        elif i == 1:
            ada += sequence
            print("Gene ADA:")
        elif i == 2:
            frat1 += sequence
            print("Gene FRAT1:")
        elif i == 3:
            fxn += sequence
            print("Gene FXN:")
        while c < len(sequence):
            if sequence[c] == "A":
                count_a += 1
            elif sequence[c] == "C":
                count_c += 1
            elif sequence[c] == "G":
                count_g += 1
            elif sequence[c] == "T":
                count_t += 1
            c += 1
        bases = ["A", "C", "G", "T"]
        bases_count = [count_a, count_c, count_g, count_t]
        d = dict(zip(bases, bases_count))
        m = max(d.items(), key = operator.itemgetter(1))
        print("Most frequent Base:", m[0])


