"""
problem: Creating a Distance Matrix
url: https://rosalind.info/problems/pdst/

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
"""

from Bio import SeqIO

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/041_PDST.txt", "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    def p_distance(s, n):

        b = len(s)
        m = 0

        for i in range(b):
            if s[i] != n[i]:
                m += 1

        return "%.5f" % (float(m) / b)

    for i in range(len(name)):
        for j in range(len(name)):
            print(p_distance(sequence[i], sequence[j]), end=" ")

        print(" ")

if __name__ == "__main__":
    main()