"""
problem: RNA Splicing
url: https://rosalind.info/problems/splc/

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
"""

from Bio import SeqIO

coding_table = {
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", 
    "TTT": "F", "TTC": "F",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "TAT": "Y", "TAC": "Y",
    "TGT": "C", "TGC": "C",
    "TGG": "W", 
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I",
    "ATG": "M", 
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", 
    "AAT": "N", "AAC": "N", 
    "AAA": "K", "AAG": "K",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "TAA": "end", "TAG": "end", "TGA": "end"
}

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/022_SPLC.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    s, introns = sequence[0], sequence[1:]

    for intron in introns:
        s = s.replace(intron, "")

    rna = ""
    for i in range(0, len(s) - 2, 3):
        if coding_table[s[i:i + 3]] == "end":
            break

        rna += coding_table[s[i:i + 3]]

    print(rna)

if __name__ == "__main__":
    main()