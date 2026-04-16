class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(xy):
            return (xy[0]**2 + xy[1]**2)**1/2
        def quickSort(arr,start,end):
            if (end-start+1 <= 1):
                return arr
            pivot = dist(arr[end])
            partition = start
            for i in range(start,end):
                if dist(arr[i]) <= pivot:
                    temp = arr[i]
                    arr[i] = arr[partition]
                    arr[partition] = temp
                    partition += 1
            temp = arr[end]
            arr[end] = arr[partition]
            arr[partition] = temp
            quickSort(arr,start,partition-1)
            quickSort(arr,partition+1,end)
            return arr
        points = quickSort(points,0,len(points)-1)
        return points[:k]