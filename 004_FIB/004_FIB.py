"""
problem: Rabbits and Recurrence Relations
url: https://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/004_FIB.txt", "r") as file:
        file = file.read()
    
    def fib(n, k):
        if n <= 2:
            return 1
        else:
            return fib(n - 1, k) + k * fib(n - 2, k)

    n, k = file.split(" ")
    print(fib(int(n), int(k)))

if __name__ == "__main__":
    main()