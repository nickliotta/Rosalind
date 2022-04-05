"""
problem: Enumerating Gene Orders
url: https://rosalind.info/problems/perm/

Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""

from itertools import permutations
from math import factorial

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/019_PERM.txt", "r") as file:
        n = int(file.readline().strip())
        n = [str(o) for o in range(1, n + 1)]

    perms = list(permutations(n))

    with open("data/output/019_PERM.txt", "w") as file:
        file.write(f"{len(perms)}\n")
        for permutation in perms:
            file.write('{}\n'.format(" ".join(permutation)))

if __name__ == "__main__":
    main()