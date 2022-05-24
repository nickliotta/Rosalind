"""
problem: Enumerating k-mers Lexicographically
url: https://rosalind.info/problems/lexf/

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
"""

import itertools

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/023_LEXF.txt", "r") as file:
        string = file.readline().strip().split(" ")
        n = int(file.readline().strip())

        result = list(itertools.product(string, repeat = n))
        print("\n".join(["".join(r) for r in result]))

if __name__ == "__main__":
    main()