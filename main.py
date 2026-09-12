import time

def IsHappy(n):
    start = time.monotonic()
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        summ = 0

        if time.monotonic() - start > 10.0:
            return 0

        for digit in str(n):
            summ += int(digit) ** 2 
        n = summ
    return n == 1

def FindHappy(limit):
    result = []
    count = 0
    n = 1

    while count < limit:
        if IsHappy(n):
            result.append(n)
            count += 1
        n += 1

    return result

if __name__ == "__main__":

    print(FindHappy(10));
