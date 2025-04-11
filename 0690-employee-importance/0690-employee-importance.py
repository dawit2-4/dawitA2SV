"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
       
        for i in range(len(employees)):
            if employees[i].id == id:
                importance = employees[i].importance
                for subordinate in employees[i].subordinates:
                    importance += self.getImportance(employees, subordinate)
                return importance
                

            
