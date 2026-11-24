import sys

def find_steps(nums):
    srt = sorted(nums)
    med = srt[len(nums) // 2]
    return sum(abs(val - med) for val in srt)

MSSG = "«20 ходов недостаточно для приведения всех элементов массива к одному числу»."

def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        nums = list(map(int, f.read().split()))

    steps = find_steps(nums) 

    print(MSSG if steps > 20 else steps)

if __name__ == "__main__":
    main()