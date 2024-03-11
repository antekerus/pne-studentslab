from pathlib import Path
import operator
class Seq:
    def __init__(self, bases=None):
        if bases is not None:
            if "A" and "C" and "G" and "T" not in bases:
                self.strbases = "ERROR"
                print("INVALID sequence!")
            else:
                self.strbases = bases
                print("New sequence created!")
        else:
            self.strbases = "NULL"
            print("NULL sequence created")


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return self.strbases.count(base)
    def count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return d
        else:
            for base in self.strbases:
                if base == "A":
                    d["A"] += 1
                elif base == "C":
                    d["C"] += 1
                elif base == "G":
                    d["G"] += 1
                elif base == "T":
                    d["T"] += 1
            return d

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        comp_seq = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "ERROR"
        else:
            for base in self.strbases:
                if base == "A":
                    comp_seq += "T"
                elif base == "C":
                    comp_seq += "G"
                elif base == "G":
                    comp_seq += "C"
                elif base == "T":
                    comp_seq += "A"
            return comp_seq

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line
        return self.strbases

    def most_frequent_base(self, filename):
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        c = 0
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line
        while c < len(self.strbases):
            if self.strbases[c] == "A":
                count_a += 1
            elif self.strbases[c] == "C":
                count_c += 1
            elif self.strbases[c] == "G":
                count_g += 1
            elif self.strbases[c] == "T":
                count_t += 1
            c += 1
        bases = ["A", "C", "G", "T"]
        count_bases = [count_a, count_c, count_g, count_t]
        d = dict(zip(bases, count_bases))
        m = max(d.items(), key=operator.itemgetter(1))
        return m[0]




