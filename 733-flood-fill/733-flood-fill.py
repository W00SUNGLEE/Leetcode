class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        check = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        
        print(check)
        
        Solution.dfs(self, image, sr, sc, newColor, check)
        
        return image
    
    
    def dfs(self, image: List[List[int]], sr: int, sc: int, newColor: int, check: List[List[int]]):
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        check[sr][sc] = 1
        
        if sr > 0:
            if image[sr-1][sc] == oldColor and check[sr-1][sc] == 0:
                Solution.dfs(self, image, sr-1, sc, newColor, check)
        
        if sr < len(image) - 1:
            if image[sr+1][sc] == oldColor and check[sr+1][sc] == 0:
                Solution.dfs(self, image, sr+1, sc, newColor, check)
        
        if sc > 0 :
            if image[sr][sc-1] == oldColor and check[sr][sc-1] == 0:
                Solution.dfs(self, image, sr, sc-1, newColor, check)
        
        if sc < len(image[0]) - 1:
            if image[sr][sc+1] == oldColor and check[sr][sc+1] == 0:
                Solution.dfs(self, image, sr, sc+1, newColor, check)
        
        
            
        