"""
problem: Inferring mRNA from Protein
url: https://rosalind.info/problems/mrna/

Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don"t neglect the importance of the stop codon in protein translation.)
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/017_MRNA.txt", "r") as file:
        sequence = file.readline().strip()

    codons = {
        "I" : 3, 
        "L" : 6, 
        "V" : 4, 
        "F" : 2,
        "M" : 1, 
        "C" : 2, 
        "A" : 4, 
        "G" : 4, 
        "P" : 4, 
        "T" : 4, 
        "S" : 6, 
        "Y" : 2, 
        "W" : 1, 
        "Q" : 2, 
        "N" : 2, 
        "H" : 2, 
        "E" : 2, 
        "D" : 2, 
        "K" : 2, 
        "R" : 6,
        "*" : 3 
    }

    if sequence[-1] != "*":
        sequence += "*"
        
    count = 1
    for s in sequence:
        count *= codons[s]

    print(count % 1000000)

if __name__ == "__main__":
    main()