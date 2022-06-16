"""
problem: Catalan Numbers and RNA Secondary Structures
url: https://rosalind.info/problems/cat/

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
"""

from Bio import SeqIO

def main():
    def count_matchings(i, j):
        if pairs[i][j] != -1:
            return(pairs[i][j])

        result = 0
        if i > j or j == 1 and match[sequence[i] == sequence[j]]:
            result = 1
        else:
            for k in range(i + 1, j + 1, 2):
                if sequence[k] == match[sequence[i]]:
                    result += count_matchings(i + 1, k - 1) * count_matchings(k + 1, j)

        pairs[i][j] = result
        return result
        
    match = { "A" : "U", "U" : "A", "C" : "G", "G" : "C" }
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/033_CAT.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    sequence = sequence[0]
    pairs = [[-1 for x in range(len(sequence) + 1)] for y in range(len(sequence) + 1)]
    matches = count_matchings(0, len(sequence)-1) % 1000000
    print(matches)

if __name__ == "__main__":
    main()