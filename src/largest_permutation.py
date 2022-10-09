# T: O(N)
# S: O(N)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        _max = len(A)
        
        # to store the places where the elements are
        d = {x: i for i, x in enumerate(A)}

        # while swaps can be made AND i still not at the end of the array
        while B and i < len(A):
            # find location of requrired element
            j = d[_max] 
            
            # if correct location, great
            if i == j:
                pass
            # else, swap
            else:
                B -= 1
                A[i], A[j] = A[j], A[i]
                d[A[i]], d[A[j]] = d[A[j]], d[A[i]]
            
            i += 1
            _max -= 1
        
        return A
