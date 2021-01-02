import this
from MidtermHeaps import Heap

h = Heap()

h.set_backing_array([-1, 7, 2, 11, 5, 3, 1, 9, 4, 0, 10, 8])
# h.heap_sort_inc()
print(h.a)
# h.min_heap_insert(0)
#h.min_heap_insert(1)
v = h.a[7]
print(v)
print("Before we remove, the heap is " + str(h.a))
print("Removing " + str(h.a[6]))
h.min_heap_remove(6)
print("After we remove, the heap is " + str(h.a))
#print(h.a)
