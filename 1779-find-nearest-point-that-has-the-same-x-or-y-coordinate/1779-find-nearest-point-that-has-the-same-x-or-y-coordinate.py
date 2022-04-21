import sys

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        distance = sys.maxsize
        
        for i in range(len(points)):
            if points[i][0] == x:
                if distance > abs(points[i][1] - y):
                    distance = abs(points[i][1] - y)
                    index = i
                
            elif points[i][1] == y:
                if distance > abs(points[i][0] - x):
                    distance = abs(points[i][0] - x)
                    index = i
   
        return index
            