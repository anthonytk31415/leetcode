class Solution:
    def fib(self, n: int) -> int:
        fibSeq = {0: 0, 1:1, 2:1}
        if n <= 2:
            return fibSeq[n]

        for i in range(3, n+1, 1):
            fibSeq[i] = fibSeq[i - 1] + fibSeq[i - 2]

        return fibSeq[n]


