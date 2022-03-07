"""
problem: Mortal Fibonacci Rabbits
url: https://rosalind.info/problems/fibd/

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

def main():
    with open("/Users/nick/Desktop/internships/rosalind/data/011_FIBD.txt", "r") as file:
        n, m = map(int, file.readline().strip().split(" "))

    num_list = []
    num_list.append(0)
    num_list.append(1)
    
    for i in range(1, n+1, 1):
        if i < m:
            num_list.append(num_list[i] + num_list[i-1])
        if i == m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
        if i > m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])

    print(num_list[n])

if __name__ == "__main__":
    main()