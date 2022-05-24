"""
problem: Completing a Tree
url: https://rosalind.info/problems/tree/

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
"""

import math

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/032_TREE.txt", "r") as file:
        n = int(file.readline().strip())
        adj = file.readlines()

    answer = n - len(adj) - 1
    print(answer)

if __name__ == "__main__":
    main()