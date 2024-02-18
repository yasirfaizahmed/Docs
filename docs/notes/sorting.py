def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  print(arr)
# Time complexity: O(N^2) in worst and average case scenarios.


bubble_sort([1,5,3,4,8,324,7,3])

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Time complexity: O(N^2) in all cases.