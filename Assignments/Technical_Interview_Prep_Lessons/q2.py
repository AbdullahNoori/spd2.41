"""Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]"""
# 1. Sort the elements in the array in descending order.
# Sort the given array in reverse order
# set array a=[5, 1, 3, 6, 8, 2, 4, 7]
# Print the first k numbers (k = 3 largest nums) in sorted array. 


def k_number(arr, k):

    a.sort;(reverse =True)

    for i in range(k):
        print (a[i], end = " ")


a = [5, 1, 3, 6, 8, 2, 4, 7]

k = 3

k_number(a ,k)