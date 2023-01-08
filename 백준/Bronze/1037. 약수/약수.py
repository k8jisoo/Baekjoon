def find_from_divisors(divisors):
    res = max(divisors) * min(divisors)
    return res

count = int(input())
divisors = list(map(int, input().split(' ')))

print(find_from_divisors(divisors))