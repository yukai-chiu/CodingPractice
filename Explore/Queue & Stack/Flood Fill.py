class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not image or not newColor:
            return []
        if newColor == image[sr][sc]:
            return image
 
        target = image[sr][sc]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        #initialize stack
        stack = [(sr,sc)]
        image[sr][sc] = newColor
        
        while stack:
            sr,sc = stack.pop()
            for r, c in directions:
                r += sr
                c += sc
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == target:
                    image[r][c] = newColor
                    stack.append((r,c))
        return image