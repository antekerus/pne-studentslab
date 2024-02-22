class Seq:
    """A class for representing sequences"""

    def __init__(self, sequence):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if not('A' or 'C' or 'G' or 'T' in sequence):
            self.strbases = "ERROR"
            print("ERROR")
        else:
            self.strbases = sequence
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
#1
s1 = Seq("AGCTC")
s2 = Seq("NIVNE")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

#2
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print("")