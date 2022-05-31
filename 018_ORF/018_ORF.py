"""
problem: Open Reading Frames
url: https://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
"""
from Bio import SeqIO

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/018_ORF.txt", "r") as file:
        s = file.readline().strip()

if __name__ == "__main__":
    main()