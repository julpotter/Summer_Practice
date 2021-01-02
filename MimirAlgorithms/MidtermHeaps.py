class Heap:
    def __init__(self):
        a = [-1]  # -1 is that fake, first element.
        heap_size = 0

    @staticmethod
    def left(k):
        return 2 * k

    @staticmethod
    def right(k):
        return 2 * k + 1

    @staticmethod
    def parent(k):
        return k // 2

    # Turn an array a into a min heap
    def min_heapify(self):
        for i in range(self.heap_size, 0, -1):
            # Precondition
            # Before we call min_heap_fix on the ith element,
            # every element after i is the root of a min heap
            self.min_heap_fix(i)
            # Postcondition
            # After this call, i is also the root of a min heap

    # Fix element i in array a to make sure it satisfies
    # the min heap property. Recursively fix child violations.
    def min_heap_fix(self, i):
        # find the min among i and its children
        if self.left(i) <= self.heap_size and self.a[self.left(i)] < self.a[i]:
            min_index = self.left(i)
        else:
            min_index = i
        if self.right(i) <= self.heap_size and self.a[self.right(i)] < self.a[min_index]:
            min_index = self.right(i)

        # At this point, we know the index of the min element
        if min_index == i:  # nothing to do here
            return
        self.a[min_index], self.a[i] = self.a[i], self.a[min_index]
        self.min_heap_fix(min_index)

    def heap_sort_dec(self):
        self.min_heapify()
        for i in range(self.heap_size, 1, -1):
            self.a[1], self.a[self.heap_size] = self.a[self.heap_size], self.a[1]
            self.heap_size -= 1
            self.min_heap_fix(1)
        self.heap_size = len(self.a) - 1

    # arr is an array which should be thought of as
    # indexed from 1
    def set_backing_array(self, arr):
        self.a = arr
        self.heap_size = len(arr) - 1

    # Functions for midterm

    #
    #     This function does a new heap sort so that the backing array ends up in increasing order.
    #     Of course, the first element of the array, a[0], is ignored.

    #     Note: This function should not simply heap_sort_dec, and then reverse the array.
    #     Nor should it use any sort of built-in to do the sorting. Just implement heap stuff, please.

    def max_heap_fix(self, i):
        # print ([self.a, i, self.heap_size])
        if self.left(i) <= self.heap_size and self.a[self.left(i)] > self.a[i]:
            max_index = self.left(i)
        else:
            max_index = i
        if self.right(i) <= self.heap_size and self.a[self.right(i)] > self.a[max_index]:
            max_index = self.right(i)

        if max_index == i:
            return
            # print(["max_index = ", max_index])
        self.a[max_index], self.a[i] = self.a[i], self.a[max_index]
        self.max_heap_fix(max_index)

    def max_heapify(self):
        for i in range(self.heap_size, 0, -1):
            self.max_heap_fix(i)

    def heap_sort_inc(self):
        self.max_heapify()
        for i in range(self.heap_size, 0, -1):
            self.a[1], self.a[self.heap_size] = self.a[self.heap_size], self.a[1]
            self.heap_size -= 1
            self.max_heap_fix(1)
        self.heap_size = len(self.a) - 1

    # This function should allow you to insert an arbitrary number into a min_heap, so that the
    # result is still a min_heap.
    #
    # Make sure that your run time is O(log n), where n is the size of the heap

    def min_heap_fix_upwards(self, i):

        if self.a[self.parent(i)] != -1:
            if self.a[self.parent(i)] < self.a[i]:
                return
            else:
                self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
                self.min_heap_fix_upwards(self.parent(i))

    def min_heap_insert(self, item):
        # self.a.insert(1, item)
        self.a.append(item)
        self.heap_size += 1
        N = self.heap_size
        # len(self.a) - 1
        self.min_heap_fix_upwards(N)
        # self.min_heapify()

    def parent_shift(self, i):
        if self.a[self.parent(i)] != -1:
            index = self.parent(i)
            self.a[i] = self.a[index]
            self.parent_shift(index)
        else:
            return

    # Removes the item at (array) index i from a min_heap.
    # The resulting heap should still be a min_heap, but with one fewer element.
    # Your code should run in O(log n) time, where n is the size of the heap.
    def min_heap_remove(self, i):
        if len(self.a) <= 2:
            self.a = [-1]
            self.heap_size -= 1
        else:
            temp = self.a[-1]
            del self.a[-1]
            self.heap_size -= 1
            self.parent_shift(i)
            self.a[1] = temp
            self.min_heap_fix(1)
