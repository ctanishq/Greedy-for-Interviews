# T: O(NlogN)
# S: O(N)

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxp3(self, A):
        A = sorted(A)

        hi3 = A[-1] * A[-2] * A[-3]
        lo2hi1 = A[0] * A[1] * A[-1]

        return max(hi3, lo2hi1)
