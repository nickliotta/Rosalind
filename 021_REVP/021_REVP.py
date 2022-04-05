"""
problem: Locating Restriction Sites
url: https://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""

from Bio import SeqIO

def switch(s):
    table = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}
    string = ""    

    for i in range(len(s)):
        string += table[s[i]]

    return string

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/021_REVP.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    palidrome = sequence[0]
    with open("data/output/021_REVP.txt", "w") as file:
        for i in range(len(palidrome)):
            for s in range(4, 13, 1):
                if palidrome[i:i + s] == switch(palidrome[i:i + s][::-1]) and (i + s <= len(palidrome)):
                    file.write(f"{i + 1} {s}\n")

if __name__ == "__main__":
    main()