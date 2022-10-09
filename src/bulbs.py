# T: O(N)
# S: O(1)

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
		cost = 0

		for b in A:
      # if even number of flips, flips back to original
			if cost % 2 == 0: b = b
      # else flip
			else: b = not b
      
      # need to turn on or not?
			if b % 2 == 1: continue
			else: cost += 1

		return cost
