class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ret=[]
        adi=len(nums1)+len(nums2)
        mid=adi//2
        m=0
        i=0
        j=0
        ret=[]
        while len(nums1)>i and len(nums2)>j and mid>=m:
            if nums1[i]<nums2[j]:
                ret.append(nums1[i])
                i+=1
            else:
                ret.append(nums2[j])
                j+=1
            m+=1
        while len(nums1)>i and mid>=m:
            ret.append(nums1[i])
            m+=1
            i+=1
        while len(nums2)>j and mid>=m:
            ret.append(nums2[j])
            m+=1
            j+=1
        print(ret)
        if adi%2==1:
            return ret[-1]
        else:
            return (ret[-1]+ret[-2])/2



            
