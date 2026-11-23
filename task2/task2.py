import sys
from math import isclose

def ell_pos(x, y, xc, yc, rx, ry):
    dx = x - xc
    dy = y - yc
    left = dx**2 * ry**2 + dy**2 * rx**2
    right = rx**2 * ry**2

    if isclose(left, right):
        return 0
    
    return 1 if left < right else 2

def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        xc, yc, rx, ry = map(float, f.read().split()[:4])

    with open(sys.argv[2], encoding="utf-8") as f:
        coords = list(map(float, f.read().split()))

    res = "\n".join(str(ell_pos(x, y, xc, yc, rx, ry)) for x, y in zip(coords[::2], coords[1::2]))
    print(res)

if __name__ == "__main__":
    main()