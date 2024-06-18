import heapq
heap = []
heapq.heappush(heap,10)  #heappush push the given element to the heap, by default it is min-heap
heapq.heappush(heap,1)
heapq.heappush(heap,12)
heapq.heappush(heap,20)
heapq.heappush(heap,6)

heap2=[10,1,12,20,6]
heapq.heapify(heap2)  #Another way of creating a min-heap

heapq.heappushpop(heap,22) #Pop out the smalest element and push in the given element
heapq.heappop(heap2)      #Pop out the element from the heap.

print(heap)
print(heap2)
