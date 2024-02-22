from Seq1 import Seq
name_gene = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
genes = [("../P00/sequences/U5.txt"), ("../P00/sequences/ADA.txt"), ("../P00/sequences/FRAT1.txt"), ("../P00/sequences/FXN.txt"), ("../P00/sequences/RNU6_269P.txt")]
print("-----| Practice 1, Exercise 10 |------")
for i in range(0, 5):
    FILENAME = genes[i]
    name = name_gene[i]
    s = Seq()
    print(f"Gene {name}: Most frequent Base: {s.most_frequent_base(FILENAME)}")
