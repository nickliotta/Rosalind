"""
problem: Transcribing DNA into RNA
url: https://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def main():
    with open("problems/rosalind_rna.txt", "r") as file:
        dna = file.read()
    
    rna = dna.replace("T", "U")

    print(rna)


if __name__ == "__main__":
    main()