"""
problem: Evolution as a Sequence of Mistakes
url: https://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/006_HAMM.txt", "r") as file:
        hamm = file.read().strip().split("\n")
    
    mutations = 0
    for i in range(len(hamm[0])):
        if hamm[0][i] != hamm[1][i]:
            mutations += 1

    print(mutations)

if __name__ == "__main__":
    main()