## Merge Sort
Merge sort is a sorting algorighm, it devides the given array into two halves, then keep devides it self until the base level, compare and sort the root two values, then repeat the same process to merge back level by level.

### Pseudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

### Given sample array:
[8, 4, 23, 42, 16, 15]

### Process

#### Step 1
#### Step 2
#### Step 3
#### Step 4
#### Step 5
#### Step 6
#### Step 7
#### Step 8
#### Step 9
#### Step 10
#### Step 11
#### Step 12
#### Step 13
#### Step 14
#### Step 15
