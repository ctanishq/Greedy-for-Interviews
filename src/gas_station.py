# T: O(N)
# S: O(1)
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        n = len(A)
        
        curr = start = 0
        for i, (g, c) in enumerate(zip(A + A, B*2)):
            if i == start + n:
                return start

            curr = curr + g - c         
            
            if curr < 0:
                start = i + 1
                curr = 0
            
        return -1
