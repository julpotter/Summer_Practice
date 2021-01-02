class priorityQueue:
    def __init__(self):
        self.x = [None]  # The backing array
        self.location = {}
        self.flag = False
        self.count = 0

    # return the index of the left child of the n'th element
    def left(self, n):
        return 2 * n

    def right(self, n):
        return 2 * n + 1

    def parent(self, n):
        return n // 2

    def heapsize(self):
        return len(self.x) - 1

    # Heap the element with the given key, up the
    # tree to its proper location. It is assumed that
    # the element is either already properly located, or
    # needs to move higher in the heap, and that the

    class priorityQueue:
        def __init__(self):
            self.x = [None]  # The backing array
            self.location = {}
            self.flag = False
            self.count = 0

        # return the index of the left child of the n'th element
        def left(self, n):
            return 2 * n

        def right(self, n):
            return 2 * n + 1

        def parent(self, n):
            return n // 2

        def heapsize(self):
            return len(self.x) - 1

        # Heap the element with the given key, up the
        # tree to its proper location. It is assumed that
        # the element is either already properly located, or
        # needs to move higher in the heap, and that the
        # tree below the key item is a min heap (by value)
        # Must update the location map at each step
        def min_heap_up(self, key):
            # print("Visited heap_up")
            # print("min_heaped up " + str(self.count) + " times")
            # self.count += 1
            # print("The key now is " + str(key))
            index = self.location[key]

            if self.parent(index) != 0:
                min_index = self.parent(index)
            else:
                min_index = index

            min_key = self.x[min_index][0]
            # print("min_key is " + str(min_key))
            # print("min_index is " + str(min_index))
            if self.parent(index) > 0:
                if self.x[index][1] < self.x[self.parent(index)][1]:
                    # print("min_index was " + str(min_index))
                    min_index = index
                    self.flag = True
                    # print("min_index becomes " + str(min_index))

            if self.flag == True and self.parent(index) > 0 and min_index == index:
                # != self.parent(index) and self.parent(index) != 0:
                # print("Found min_index index mismatch")
                key1 = self.x[index][0]
                # print("key 1 is " + str(key1))
                # print(self.parent(index))

                key2 = self.x[self.parent(index)][0]
                # print("key 2 is " + str(key2))
                # print("x before looks like " + str(self.x))
                self.x[self.parent(index)], self.x[min_index] = self.x[min_index], self.x[self.parent(min_index)]
                # print("x after swap looks like " + str(self.x))
                # print("location before swap looks like " + str(self.location))
                self.location[key1] = self.parent(min_index)
                self.location[key2] = min_index
                # print("location after swap looks like " + str(self.location))
                # print("The current min_key is " + str(self.x[min_index][0]))

                if self.x[self.parent(min_index)] is not None:
                    self.min_heap_up(self.x[self.parent(min_index)][0])
                self.flag == False

            # Your code here

        # Adds the key to the priority queue, with the associated value.
        # After add(), the backing list x should be a min heap, by value
        def add(self, key, value):
            # print("Visited add")
            self.x.append(tuple((key, value)))
            # print(self.x)
            index = self.x.index((key, value))
            self.location[key] = index
            # print(self.x)
            # print(self.location)
            # index = self.location[key]
            self.min_heap_up(key)
            # print(self.x)
            # Your code here

        # Sets the value associated with the given key to new_value,
        # which is guaranteed to be no greater than its current value.
        # Heaps up the resulting (key, value) pair
        def decrease_value(self, key, new_value):
            index = self.location[key]  # Find the item in the heap
            self.x[index] = (key, new_value)  # give it its new value
            self.min_heap_up(key)  # heap it up

        # Removes the item at the top of the heap, which will be an item
        # of minimum value in the queue. Restores the min-heap property, by value,
        def remove_min(self):
            print("Visited remove_min")
            # Your code here

        # Swaps an item down the tree until it lands in its proper place in the
        # heap, according to its value.
        # Takes the index, not the key, and heaps the item at that index down to
        # its proper location. It uses index instead of key because it is called
        # only when the index is already known.
        # Must maintain the location map at each step.
        def min_heap_down(self, index):
            # print("visited min_heap_down")
            min_index = index
            if self.left(index) <= self.heapsize():
                if self.x[self.left(index)][1] < self.x[index][1]:
                    min_index = self.left(index)
            if self.right(index) <= self.heapsize():
                if self.x[self.right(index)][1] < self.x[min_index][1]:
                    min_index = self.right(index)

            if min_index != index:
                key1 = self.x[index][0]
                key2 = self.x[min_index][0]
                self.x[index], self.x[min_index] = self.x[min_index], self.x[index]
                self.location[key1] = min_index
                self.location[key2] = index
                self.min_heap_down(min_index)


