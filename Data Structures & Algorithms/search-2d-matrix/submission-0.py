class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        l=0
        r=rows*cols-1
        while l<=r:
            mid=(l+r)//2
            midrow=mid//cols
            midcol=mid%cols
            if matrix[midrow][midcol]>target:
                r=mid-1
            elif matrix[midrow][midcol]<target:
                l=mid+1
            else:
                return True
        return False

