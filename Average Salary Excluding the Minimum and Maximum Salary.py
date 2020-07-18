//https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/submissions/
//1491. Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    def average(self, salary: List[int]) -> float:
        
        minimum=min(salary)
        maximum=max(salary)
        
        addition=sum(salary)-(minimum+maximum)
        length=len(salary)-2
        average=addition/length
        
        return average
    
