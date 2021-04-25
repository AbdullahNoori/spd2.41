"""Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20 ⇒ [13, 6] or [4, 17] or [5, 14]"""

# let a = [9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20 ⇒ [13, 6] or [4, 17] or [5, 14]
# create function closest_sum(a, b, arr_size, sum):
# sort the array 
# traverse the array for the two elements 
# 

# create function closest_sum(a, arr_size, sum):
def closest_sum(a, b, a_len, b_len, t):
# Initialized the difference of the pair and sum
    diff=sys.maxsize

# result_1 and result_2 are the results
# indexes from a[] and b[]
# start from left side of a and right side of b.
    left = 0
    right = b_len-1

    while (left < a_len and right >= 0):
        # if pair is clser to target (t) than previusly found closest, 
        # then update results_1, results_2 and diff.
        if abs (a[left] + b[right] - t) < diff:
            results_1 = left
            results_2 = right
            diff = abs(a[left] + b[right] -t)

        # If the sum of pair is more than t(target)
        # Then move to smaller side
        if a[left] + b[right] > t:
            right = right -1
        # move to the greater side
        else:
            left = left + 1

#   print results       
    print("The closest pair/numbers in both arrays are [",a[results_1],",",b[results_2],"]")



# Driver program to test above functions
a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
a_len = len(a)
b_len = len(b)
t = 20
closest_sum(a, b, a_len, b_len, t)

