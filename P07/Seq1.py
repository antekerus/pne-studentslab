from pathlib import Path
class Seq1:
    BASES = ["A", "C", "T", "G"]
    COMPLEMENTS = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    @staticmethod #es una funcion como en fundamentos pero para meterlo dentro del class usas @staticmethod
    def is_valid(bases):
        ok = True
        i = 0
        while ok and i < len(bases):
            base = bases[i]
            #V1
            if not base in Seq1.BASES:
                ok = False
            #V2
            #ok = base in Seq1.BASES
            #V3
            #ok = bases[i] in Seq1.BASES
            i += 1
        return ok




    def __init__(self, bases=None):
        #if bases is None:
            #self.bases = "NULL"
            #print("NULL seq created!")
        #else:
            #if Seq1.is_valid(bases):
                #self.bases = bases
                #print("New sequence created")
            #else:
                #self.bases = "EROOR"
                #print("Invalid seq!")

        if bases is not None:
            if Seq1.is_valid(bases):
                self.bases = bases
                print("New sequence created")
            else:
                self.bases = "ERROR"
                print("Invalid seq!")
        else:
            self.bases = "NULL"
            print("NULL seq created!")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            total = 0
            for c in self.bases:
                if c == base:
                    total += 1
            return total
            #return self.bases

    def count(self):
        #result = {
            #'A': self.count_base("A"),
            #'C': self.count_base("C"),
            #'T': self.count_base("T"),
            #'G': self.count_base("G")
        #}
        #return result
    #para recorrer la lista del principio
        result = {}
        for base in Seq1.BASES:
            result [base] = self.count_base(base)
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
            result = ""
            for base in self.bases:
                result += Seq1.COMPLEMENTS[base]
            # for base in self.bases:
            #     if base == "A":
            #         result += "T"
            #     elif base == "C":
            #         result += "G"
            #     elif base == "G":
            #         result += "C"
            #     elif base == "T":
            #         result += "A"
            return result
        #otra forma de hacerlo con el diccionario complementario



    #def complement(self):
        #if self.bases == "NULL" or self.bases == "EROOR":
            #return self.bases
        #else:
            #rna = ""
            #for base in self.bases:
                #if base == "A":
                    #rna += "T"
                #elif base == "C":
                    #rna += "G"
                #elif base == "G":
                    #rna += "C"
                #elif base == "T":
                    #rna += "A"
            #return rna

    # def read_fasta(self, filename=None):
    #     from pathlib import Path
    #     if filename:
    #         file_contents = Path(filename).read_text()
    #         index = file_contents.find('\n')
    #         self.strbases = file_contents[index:].replace('\n', '')

    def read_fasta(self, file_name):
        content = Path(file_name).read_text()
        lines = content.splitlines() #te separa cada linea que tenga un caracter y te lo mete en la lista
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def most_frequent_base(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return None
        else:
            result = None
            for base, count in self.count().items(): #el self.count te hace un diccionario
                if result is None: #if not result
                    result = {"base": base, "count": count}
                else:
                    if count > result ['count']:
                        result = {"base": base, "count": count} #vuelves a poner el nuevo diccionario con el mayor valor
            return result['base']




    def info(self):
        result = f"Total length: {self.len()}\n"
        for base, count in self.count().items():  # el self.count te hace un diccionario
                percentage = (count * 100) / self.len()
                result += f"{base}: {count} ({percentage:.1f}%)\n"
        return result




                # if result is None or count > result ['count']: #if not result
                #     result = {"base": base, "count": count}


    # def most_frequent_base(self):
    #     number_A = 0
    #     number_C = 0
    #     number_G = 0
    #     number_T = 0
    #     for i in self.strbases:
    #         if str(i) == "A":
    #             number_A += 1
    #         elif str(i) == "C":
    #             number_C += 1
    #         elif str(i) == "G":
    #             number_G += 1
    #         elif str(i) == "T":
    #             number_T += 1
    #     values = [number_A, number_C, number_G, number_T]
    #     max_value = max(values)
    #     max_base = ""
    #     if max_value == int(number_A):
    #         max_base += "A"
    #     elif max_value == int(number_C):
    #         max_base += "C"
    #     elif max_value == int(number_G):
    #         max_base += "G"
    #     elif max_value == int(number_T):
    #         max_base += "T"
    #     return max_base
