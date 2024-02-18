
1. **Bubble Sort** :

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Time complexity: O(N^2) in worst and average case scenarios.
```
![bubble dsort](../statics/bubble.png)
 
1. **Selection Sort** :

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Time complexity: O(N^2) in all cases.
```
![bubblefe sort](../statics/selection.png)
![bubblew sort](../statics/selection_sorting.png)
 
1. **Insertion Sort** :

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Time complexity: O(N^2) in worst case, but O(N) in best case when the list is nearly sorted.
```

 
1. **Merge Sort** :

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Time complexity: O(N log N) in all cases.
```

![buvbble sort](../statics/mergesort.png)
 
1. **Quick Sort** :

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Time complexity: O(N log N) in average case, but O(N^2) in worst case (rare).
```

 
1. **Heap Sort** :

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Time complexity: O(N log N) in all cases.
```

 
1. **Counting Sort** :

```python
def counting_sort(arr):
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)
    for num in arr:
        count_arr[num] += 1
    for i in range(1, max_val + 1):
        count_arr[i] += count_arr[i - 1]
    for num in reversed(arr):
        sorted_arr[count_arr[num] - 1] = num
        count_arr[num] -= 1
    return sorted_arr

# Time complexity: O(N + K) where K is the range of the non-negative key values.
```

 
1. **Radix Sort** :

```python
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

# Time complexity: O(N * k) where k is the number of digits in the largest number.
```

 
1. **Bucket Sort** :

```python
def bucket_sort(arr):
    buckets = []
    for _ in range(len(arr)):
        buckets.append([])
    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

# Time complexity: O(N^2) in worst case, but typically O(N + k) on average.
```

 
1. **Shell Sort** :

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Time complexity: Depends on the chosen sequence of gaps, but typically between O(N log N) and O(N^2).
```
