class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-2
        highest = arr[-1]
        arr[-1] = -1
        while i>=0:
            temp = arr[i]
            arr[i] = highest
            if highest < temp:
                highest = temp
            i -= 1
        return arr