"""
problem: Speeding Up Motif Finding
url: https://rosalind.info/problems/kmp/

Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.
"""

from Bio import SeqIO
from itertools import product 

def failure_array(s):
    f = [0 for i in range(len(s))]
    n = len(s)
    k = 1 
    j = 0 

    while k < n:
        if s[k] == s[j]:
            j += 1
            f[k] = j
            k += 1
        else:
            if j != 0:
                j = f[j - 1]
            else:
                f[k] = 0
                k += 1

    return f

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/037_KMP.txt", "r") as file:
        with open("data/output/037_KMP.txt", "w") as out:
            out.write(" ".join(map(str, failure_array(SeqIO.read(file, "fasta")))))

if __name__ == "__main__":
    main()