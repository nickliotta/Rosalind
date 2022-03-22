"""
problem: Modeling Random Genomes
url: https://rosalind.info/problems/prob/

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
"""

import math

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/013_PROB.txt", "r") as file:
        s = file.readline().strip()
        a_ = map(float, file.readline().strip().split(" "))

    a = s.count("A") + s.count("T")
    c = s.count("C") + s.count("G")

    for n in a_:
        p = a * math.log((1 - n)/2, 10) + c * math.log(n / 2, 10)
        print("%.3f" % p, end=" ")

if __name__ == "__main__":
    main()