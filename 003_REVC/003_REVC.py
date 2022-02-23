"""
problem: Complementing a Strand of DNA
url: https://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/003_REVC.txt", "r") as file:
        dna = file.read()
    
    complement = dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")[::-1].upper()
    print(complement)

if __name__ == "__main__":
    main()