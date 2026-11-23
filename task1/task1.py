import sys
from math import gcd

def path(n, m):
    step = m - 1
    cnt = n // gcd(n, step)
    return "".join(str((i * step) % n + 1) for i in range(cnt))

def main():
    args = list(map(int, sys.argv[1:]))
    res = "".join(path(n, m) for n, m in zip(args[::2], args[1::2]))
    print(res)

if __name__ == "__main__":
    main()