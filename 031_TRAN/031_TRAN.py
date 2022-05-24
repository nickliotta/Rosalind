"""
problem: Transitions and Transversions
url: https://rosalind.info/problems/tran/

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

from Bio import SeqIO

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/031_TRAN.txt", "r") as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    s, t = sequence[0], sequence[1]
    transitions, transversions = 0, 0

    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] == "A" and t[i] == "G":
                transitions += 1
            elif s[i] == "G" and t[i] == "A":
                transitions += 1
            elif s[i] == "C" and t[i] == "T":
                transitions += 1
            elif s[i] == "T" and t[i] == "C":
                transitions += 1
            else:
                transversions += 1
    
    print(transitions/transversions)

if __name__ == "__main__":
    main()