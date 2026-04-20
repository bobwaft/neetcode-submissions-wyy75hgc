class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
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
        def insertHeap(heap,val):
            heap.append(val)
            i = len(heap) - 1
            while i > 1 and heap[i] > heap[i//2]:
                temp = heap[i]
                heap[i] = heap[i//2]
                heap[i//2] = temp
                i = i//2
            return heap
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
        heap = heapify(stones)
        while len(heap) > 2:
            print(heap)
            heap, stone1 = popHeap(heap)
            heap, stone2 = popHeap(heap)
            heap = insertHeap(heap,abs(stone1-stone2))
        return heap[1]

                        