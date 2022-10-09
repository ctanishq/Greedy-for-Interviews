# T: O(N)
# S: O(N)

class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):
        MOD = 10000003
        
        # all the indices of xs
        crosses = [i for i, c in enumerate(A) if c == "x"]
        # moves req assuming starting position is 0
        crosses = [(cross - i) for i, cross in enumerate(crosses)]

        n = len(crosses)
        if n == 0: return 0
        
        ans = float('inf')
        segment_start = crosses[n // 2]
        total = 0        
        for cross in crosses: # O(N)
            total += abs(cross - segment_start)
            total %= MOD
        ans = min(ans, total % MOD)
            
        return ans
