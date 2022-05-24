"""
problem: Counting Phylogenetic Ancestors
url: https://rosalind.info/problems/inod/

Given: A positive integer n (3≤n≤10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves.
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/035_INOD.txt", "r") as file:
        n = int(file.readline().strip())
    
    print(n - 2)

if __name__ == "__main__":
    main()