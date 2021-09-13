# List Comprehensions
def range1(number):
    return range(number + 1)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range1(x) for j in range1(y) for k in range1(z) if i + j + k != n])
