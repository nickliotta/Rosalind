"""
problem: Finding a Protein Motif
url: https://rosalind.info/problems/mprt/

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

import requests
import re

def parse_sequence(fasta):
    sequence = re.sub("^\>(.*)\n", "", fasta, 1)
    sequence = sequence.replace("\n", "")

    return sequence

def motifs(sequences):
    pattern = re.compile("^N[A-O,Q-Z](S|T)[A-O,Q-Z]")
    results = {}

    for name in sequences:
        index = []
        seq = sequences[name]
        
        for j in range(len(seq)):
            if pattern.match(seq[j:j+4]):
                index.append(str(j+1))
        
        if len(index) != 0:
            results[name] = " ".join(index)

    return sorted(results.items())

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/016_MPRT.txt", "r") as file:
        uniprots = file.read().strip().split("\n")

    fastas = {}
    for u in uniprots:
        response = requests.get(f"http://www.uniprot.org/uniprot/{u}.fasta")
        sequence = parse_sequence(response.text)
        fastas[u] = sequence

    for u, loc in motifs(fastas):
        print(u)
        print(loc)

if __name__ == "__main__":
    main()