#Сложность алгоритма O(n^2)

a = [-7, 8, 5, -56, 1, 10]

def selection_sort(arr):
   for i in range(len(arr)):
       min_index = i
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(a)
print(a)