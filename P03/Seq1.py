from pathlib import Path

class Seq1:
    BASES = ['A', 'C', 'T', 'G']
    BASES_VALUE = {"A": 2, "C": -1, "G": 3, "T": 5}
    COMPLEMENTS = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    @staticmethod
    def are_bases_ok(bases):
        ok = True
        i = 0
        while ok and i < len(bases):
            # base = bases[i]
            # V1
            # if base not in Seq1.BASES:
            #    ok = False
            # V2
            # ok = base in Seq1.BASES
            # V3
            ok = bases[i] in Seq1.BASES
            i += 1
        return ok

    def __init__(self, bases=None):
        if bases is not None:  # if bases:
            if Seq1.are_bases_ok(bases):
                self.bases = bases
                print("New sequence created!")
            else:
                self.bases = "ERROR"
                print("Invalid seq!")
        else:
            self.bases = "NULL"
            print("NULL seq created!")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR": #if s.is_valid()
            return 0
        else:
            return len(self.bases)
        #return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            # total = 0
            # for c in self.bases:
                # if c == base:
                    # total += 1
            # return total
            return self.bases.count(base)

    def count(self):
        # result = {
            # 'A': self.count_base('A')
            # 'C': self.count_base('C')
            # 'T': self.count_base('T')
            # 'G': self.count_base('G')
        # }
        #return result
        result = {}
        for base in Seq1.BASES:
            result[base] = self.count_base(base)
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        else:
            return self.bases[::-1]

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        else:
            rna = ""
            for base in self.bases:
                rna += Seq1.COMPLEMENTS[base]
            # for base in self.bases:
            #     if base == "A":
            #         rna += "T"
            #     elif base == "C":
            #         rna += "G"
            #     elif base == "G":
            #         rna += "C"
            #     elif base == "T":
            #         rna += "A"
            return rna

    def read_fasta(self, file_name):
        content = Path(file_name).read_text()
        lines = content.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def most_frequent_base(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return None
        else:
            result = None
            for base, count in self.count().items():
                if result is None or count > result['count']: #if not result:
                    result = {'base': base, 'count': count}
            return result['base']

    def info(self):
        result = f"Sequence: {self.bases}\n"
        result += f"Total length: {self.len()}\n"
        d = self.count()
        for base, count in d.items():
            percentage = (count * 100) / self.len()
            result += f"{base}: {count} ({percentage:.1f}%)\n"
        return result

    def mult(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            total = 1
            for base in self.bases:
                total *= Seq1.BASES_VALUE[base]
            return total

    def is_valid(self):
        return self.bases != "ERROR" and self.bases != "NULL"
