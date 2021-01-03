n=int(input())
def main(n):
    binary=bin(n)
    print(binary)
    binary=list(binary)
    print(binary)
    print(binary.count("1"))
main(n)
