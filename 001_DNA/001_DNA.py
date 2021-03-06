"""
problem: Counting DNA Nucleotides
url: https://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/001_DNA.txt", "r") as file:
        dna = file.read().strip()

        print(
            dna.count("A"),
            dna.count("C"),
            dna.count("G"),
            dna.count("T")
        )


if __name__ == "__main__":
    main()