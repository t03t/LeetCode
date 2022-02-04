class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        #test for lengths:
        # sqrt of y2-y1 square and x2-x1 sqr
        if p1==p2==p3==p4:
            return False
        def size(a,b):
            return math.sqrt((a[1]-b[1])**2 + (a[0]-b[0])**2)
        
        #this will be four adjacents and two diagonals
        ls = [size(p1,p2),size(p1,p3),size(p1,p4), size(p2,p3), size(p3,p4), size(p2,p4)]
        ls.sort()
        print(ls)
        
        return ls[0]==ls[1]==ls[2]==ls[3] and ls[4]==ls[5]
        
            