How the Code Works

The solve(n, array, k) function processes an input array by removing certain elements and then summing the remaining values. Here’s a breakdown of the key steps:

1. Cloning the Array
   The function begins by creating two copies of the input array:

maxArr: This copy is used for removing the largest elements.
minArr: This copy is used for removing the smallest elements. 2. Removing Elements
A loop runs k times, and during each iteration:

Find and Remove the Maximum:

The function uses the findMax helper to locate the largest element in maxArr.
Once found, that element is removed from maxArr.
Find and Remove the Minimum:

Similarly, the findMin helper is used to locate the smallest element in minArr.
The identified element is then removed from minArr. 3. Summing the Remaining Values
After the loop completes:

maxValue:
This is calculated by summing all the elements that remain in maxArr (i.e., after k maximum elements have been removed).

minValue:
This is calculated by summing all the elements remaining in minArr (i.e., after k minimum elements have been removed).
