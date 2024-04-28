#It is highly recommended to know 2 nlogn algorithms
#Long term wise understanding heapsort would be wise since it is used in Trees and linked list 

def heapify(self,arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)


def heap_sort(self,arr):
        n = len(arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Sort the heap
        sorted_arr = [0] * n
        for i in range(n - 1, -1, -1):
            sorted_arr[i] = arr[0]
            arr[0] = arr[i]
            self.heapify(arr, i, 0)

        return sorted_arr
