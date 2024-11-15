import math

num_ = int(input().strip())
base_ = 1000000007


def solve(num, base):
    def sigma(numm):
        return (numm * (numm + 1) // 2) % base

    # Discount the trivial case
    # Trivial case where the divisor of the number is the number itself
    res = ((num * (num + 1)) // 2) % base
    # Trivial case where the divisor of the number is 1
    # we do not count 1 itself, hence (num - 1) ones
    res += (num - 1 % base)
    sq_int = int(math.sqrt(num))
    for i in range(2, 1 + sq_int):
        d = num // i
        # When counting say the cases where the present number (i)
        # is the lesser of the divisor
        # 4, ... 20 for num = 20 and i = 2
        # 9, .... 18 for num = 20 and i = 3
        # in the line below we count the number of times i appears as lesser divisor
        res = (res + (i * (d - i + 1))) % base
        # in the following line we consider the larger divisor
        # 9, .... 18 for num = 20 and i = 3
        # higher divisors are 3, 4, 5
        # sig = sigma(6) - sigma(3)
        sig = (sigma(d) - sigma(i)) % base
        res = (res + sig) % base
    return res


print(solve(num_, base_))
