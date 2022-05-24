"""
problem: k-Mer Composition
url: https://rosalind.info/problems/kmer/

Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.
"""

from Bio import SeqIO
from itertools import product 

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/036_KMER.txt", "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    s = sequence[0]
    kmers = ["".join(x) for x in (product("ACGT", repeat=4))]
    seq = {i : 0 for i in kmers}

    for i in range(len(s) - 4 + 1):
        seq[s[i:i+4]] += 1

    for i in kmers:
        print(seq[i], end=" ")

if __name__ == "__main__":
    main()