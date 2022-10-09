# T: o(NlogN)
# S: O(N)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x: x[1])
        
        prev_s, prev_e = A[0]
        count = 1
        
        for s, e in A:
            if s <= prev_e:
                pass
            else:
                prev_s, prev_e = s, e
                count += 1
        
        return count
