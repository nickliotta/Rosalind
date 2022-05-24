"""
problem: Finding a Shared Motif
url: https://rosalind.info/problems/lcsm/

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.
"""
from Bio import SeqIO

def main():
    name, sequences = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/014_LCSM.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequences.append(str(seq_record.seq))

    def get_motif():
        first = min(sequences, key=len)
        k = len(first)

        for i in range(k, 1, -1):
            for j in range(k - i + 1):
                motif = first[j:j+i]
                f = True

                for sequence in sequences:
                    s = sequence.find(motif)
                    if s == -1:
                        f = False
                        break

                if f == True:
                    return motif

    answer = get_motif()
    if answer != None:
        print(answer)
    else:
        print("None")

if __name__ == "__main__":
    main()