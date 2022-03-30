"""
problem: Independent Alleles
url: https://rosalind.info/problems/lia/

Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""

import math

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/015_LIA.txt", "r") as file:
        k, n = map(int, file.readline().strip().split(" "))

    def combinatorial(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    aab = 4 / 16.0

    p = []
    total = 2 ** k
    for r in range(n, (total + 1)):
        p.append(combinatorial(total, r) * (aab ** r) * ((1 - aab) ** (total - r)))

    print("%.3f" % sum(p))

if __name__ == "__main__":
    main()