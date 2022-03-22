"""
problem: Consensus and Profile
url: https://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

from Bio import SeqIO
import numpy as np

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/010_CONS.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    name_length = len(name)
    sequence_length = len(sequence[0])
    bases = ["A", "C", "G", "T"]
    consensus = ""
    graph = np.zeros(shape=(4, sequence_length), dtype=int)

    for c in range(sequence_length):
        position_symbol = [s[c] for s in sequence]
        most_common_symbol = max(position_symbol, key=position_symbol.count)
        consensus += most_common_symbol
        for r in range(len(bases)):
            graph[r][c] = position_symbol.count(bases[r])

    print(consensus)
    for i in range(4):
        print("{}: {}".format(bases[i], " ".join([str(j) for j in graph[i]])))    

if __name__ == "__main__":
    main()