class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n,cache):
            if (n <= 1):
                return 1
            if (n in cache):
                return cache[n]
            cache[n] = fib(n-1,cache) + fib(n-2,cache)
            return cache[n]
        return fib(n,{})