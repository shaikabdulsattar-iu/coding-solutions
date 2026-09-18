class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        def is_prime(x: int) -> bool:
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        count = 0
        for x in range(2, n):
            if is_prime(x):
                count += 1

        return count


        