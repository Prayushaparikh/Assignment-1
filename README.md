# Assignment-1
Algorithm Explanations and Complexity Analysis

1) Two Sum

Approach:

Use a hash map (dictionary) to store indices of visited numbers.

Iterate through the array, checking if the complement (target - current number) exists in the hash map.

If found, return the indices of the two numbers.

Time Complexity: O(n) (single pass through the list)

Space Complexity: O(n) (stores indices in a dictionary)

2) Find First and Last Position of Element in Sorted Array

Approach:

Use binary search to find the first and last occurrence of the target.

Perform two binary searches: one for the leftmost index and another for the rightmost index.

Time Complexity: O(log n) (binary search)

Space Complexity: O(1) (constant space usage)

3) Median of Two Sorted Arrays

Approach:

Merge the two sorted arrays (conceptually) and find the median.

If the combined length is odd, return the middle element; if even, return the average of the two middle elements.

Optimized approach: Use binary search to partition the two arrays efficiently in O(log (m+n)).

Time Complexity: O(log (m+n)) (optimized approach)

Space Complexity: O(1) (no extra space used beyond variables)

4) Remove Nth Node From End of List

Approach:

Use a two-pointer approach: move one pointer n+1 steps ahead, then move both pointers together until the first reaches the end.

The second pointer will then be at the node before the one to remove.

Update the pointers to skip the target node.

Time Complexity: O(sz) (single traversal of the list)

Space Complexity: O(1) (modifies the list in place)

5) Merge k Sorted Lists

Approach:

Use a min-heap (priority queue) to efficiently extract the smallest element from the k lists.

Push the first node of each list into the heap.

Extract the smallest element, append it to the result, and push its next node (if exists) into the heap.

Repeat until all nodes are merged.

Time Complexity: O(N log k) (where N is the total number of nodes and k is the number of lists)

Space Complexity: O(k) (heap stores k elements at a time)
