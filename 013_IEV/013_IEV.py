"""
problem: Calculating Expected Offspring
url: https://rosalind.info/problems/iev/

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""

import math

def main():
    p = [2., 2., 2., 1.5, 1, 0]

    with open("/Users/nick/Desktop/internships/rosalind/data/014_IEV.txt", "r") as file:
        couples = map(int, file.readline().split(" "))

    print(sum([a * b for a, b in zip(p, couples)]))

if __name__ == "__main__":
    main()