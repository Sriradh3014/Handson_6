# Handson_6

# 3)Mathematically derive the average runtime complexity of the non-random pivot version of quicksort.

To determine the average runtime complexity of the non-random pivot quicksort, let's begin by examining its recurrence relation.

In this version, the pivot selection is deterministic, often opting for the last element in the array as the pivot. Let's denote the array's length as n.

The recurrence relation for this quicksort variant is expressed as:

T(n)=T(k)+T(n-k-1)+O(n)

Here:
T(n) represents the time needed to sort an array of size n.

k signifies the index where the pivot settles after partitioning.
The O(n) term stems from the partitioning step, where we traverse the array once to partition it around the chosen pivot.

Now, let's explore the average case complexity. In this scenario, we assume that the pivot divides the array into approximately equal parts. Hence, on average, 
k tends to be around n/2.

T(n)=T(n/2)+T(n/2)+O(n)

The two recursive calls handle arrays of roughly n/2 in size, and the partitioning step consumes O(n) time.
To solve this recurrence relation, we can apply the Master Theorem. In this case, a=2,b=2, and f(n)=O(n).

Given that f(n)=O(n), which is polynomially larger than n^(log a base b) = n^( log 2 base 2) = n ,we fall into case 2 of the Master Theorem.

Hence, the average runtime complexity of the non-random pivot quicksort isO(nlogn).
