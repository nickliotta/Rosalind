"""
problem: Partial Permutations
url: https://rosalind.info/problems/pper/

Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.
"""

import math

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/027_PPER.txt", "r") as file:
        n, k = map(int, file.readline().strip().split(" "))
        p_per = math.factorial(n) / math.factorial(n - k) % 1000000
        print(p_per)

if __name__ == "__main__":
    main()