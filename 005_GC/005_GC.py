"""
problem: Computing GC Content
url: https://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

from Bio import SeqIO

def main():
    name, sequence = [], []

    with open("/Users/nick/Desktop/internships/rosalind/data/005_GC.txt", "r") as file:
        for seq_record  in SeqIO.parse(file, "fasta"):
            name.append(str(seq_record.name))
            sequence.append(str(seq_record.seq))

    strings = {name[i]:sequence[i] for i in range(len(name))}
    contents = {}

    for k, v in strings.items():
        content = ((v.count("G") + v.count("C")) / len(v)) * 100
        contents[k] = content
    
    contents = sorted(contents.items(), key=lambda d: d[1], reverse=True)
    highest = contents[0]

    print(highest[0])
    print(highest[1])

if __name__ == "__main__":
    main()