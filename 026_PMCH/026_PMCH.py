"""
problem: Perfect Matchings and RNA Secondary Structures
url: https://rosalind.info/problems/pmch/

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""

from Bio import SeqIO
import math

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/026_PMCH.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    s = sequence[0]
    print(math.factorial(s.count("A")) * math.factorial(s.count("C")))

if __name__ == "__main__":
    main()