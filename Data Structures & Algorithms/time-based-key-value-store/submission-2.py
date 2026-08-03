class TimeMap:

    def __init__(self):
        self.dicti={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dicti:
            self.dicti[key]=[]
        self.dicti[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dicti:
            return ""
        l1=self.dicti[key]
        left=0
        right=len(l1)-1
        res=''
        while left<=right:
            mid=(left+right)//2
            if timestamp>=l1[mid][1]:
                res=l1[mid][0]
                left=mid+1
            else:
                right=mid-1
        return res



             
