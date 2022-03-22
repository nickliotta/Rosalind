"""
problem: Overlap Graphs
url: https://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

from Bio import SeqIO

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/012_GRPH.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if i != j:
                if sequence[i][-3:] == sequence[j][:3]:
                    print(name[i], name[j])

if __name__ == "__main__":
    main()