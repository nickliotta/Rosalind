"""
problem: Introduction to Mendelian Inheritance
url: https://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/007_IPRB.txt", "r") as file:
        k, m, n = map(int, file.read().strip().split(" "))
    
    x = m * m + 4 * n * n + 4 * m * n - 4 * n - m
    y = 4 * (k + m + n) * (k + m + n - 1)
    probability = 1 - float(x) / y

    print(probability)

if __name__ == "__main__":
    main()