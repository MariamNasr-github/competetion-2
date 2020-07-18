#https://leetcode.com/problems/the-kth-factor-of-n/submissions/
#1492. The kth Factor of n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factors=[]
        
        for i in range (1,n+1):
            if(n % i == 0):
                factors.append(i)
                
        if (len(factors)<k):
            return -1
        else:
            sorted_factors=sorted(factors)
            #print(sorted_factors)
            return factors[k-1]
        