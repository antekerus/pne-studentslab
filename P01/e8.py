from Seq1 import Seq
print("-----| Practice 1, Exercise 8 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("AXHEY")
print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print(f"\tBases: {s1.count()}")
print(f"\tRev: {s1.reverse()}")
print(f"\tComp: {s1.complement()}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"\tBases: {s2.count()}")
print(f"\tRev: {s2.reverse()}")
print(f"\tComp: {s2.complement()}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print(f"\tBases: {s3.count()}")
print(f"\tRev: {s3.reverse()}")
print(f"\tComp: {s3.complement()}")