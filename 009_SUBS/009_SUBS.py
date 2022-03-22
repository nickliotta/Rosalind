"""
problem: Mortal Fibonacci Rabbits
url: https://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/009_SUBS.txt", "r") as file:
        s, t = file.read().strip().split("\n")

    position = []
    for i in range(len(s)):
        if s.startswith(t, i):
            position.append(i + 1)
    
    print(" ".join(map(str, position)))

if __name__ == "__main__":
    main()