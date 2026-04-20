class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(arr):
            arr.append(arr[0])
            arr[0] = -1
            cur = (len(arr)-1) // 2
            while cur > 0:
                i = cur
                while 2*i < len(arr):
                    if (2*i + 1 < len(arr) and arr[2*i + 1] > arr[2*i] 
                    and arr[i] < arr[2*i + 1]):
                        temp = arr[2*i + 1]
                        arr[2*i + 1] = arr[i]
                        arr[i] = temp
                        i = 2*i + 1
                    elif arr[i] < arr[2*i]:
                        temp = arr[2*i]
                        arr[2*i] = arr[i]
                        arr[i] = temp
                        i = 2*i
                    else:
                        break
                cur -= 1
            return arr
        def popHeap(heap):
            if len(heap) == 1:
                return None
            if len(heap) == 2:
                return (heap,heap.pop())
            res = heap[1]
            heap[1] = heap.pop()
            i = 1
            while 2*i < len(heap):
                if (2*i + 1 < len(heap) and heap[2*i + 1] > heap[2*i] 
                and heap[i] < heap[2*i + 1]):
                    temp = heap[2*i + 1]
                    heap[2*i + 1] = heap[i]
                    heap[i] = temp
                    i = 2*i + 1
                elif heap[i] < heap[2*i]:
                    temp = heap[2*i]
                    heap[2*i] = heap[i]
                    heap[i] = temp
                    i = 2*i
                else:
                    break
            return (heap,res)
        heap = heapify(nums)
        for j in range(k-1):
            heap, _ = popHeap(heap)
        return heap[1]