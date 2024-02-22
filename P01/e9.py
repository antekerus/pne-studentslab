from Seq1 import Seq
FILENAME = "../P00/sequences/U5.txt"
print("-----| Practice 1, Exercise 9 |------")
s = Seq()
s.read_fasta(FILENAME)
print(f"Sequence : (Length: {s.len()}) {s.strbases}")
print(f"\tBases: {s.count()}")
print(f"\tRev: {s.reverse()}")
print(f"\tComp: {s.complement()}")