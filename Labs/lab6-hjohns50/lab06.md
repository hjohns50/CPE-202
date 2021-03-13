Spring 2020 Lab 6

In addition to completing the selection and insertion sorts in sorts.py and pushing code to GitHub, you will need to submit a pdf to **Canvas** containing answers to lab06_questions.pdf and the table at the bottom of this document.

**Lab 6: Basic Comparison Sorts**

A comparison sort is a type of sorting algorithm that compares elements in a list (array, file, etc) using a comparison operation that determines which of two elements should occur first in the final sorted list. The operator is almost always a **total order** :

1. a ≤ a for all a in the set

2. if a ≤ b and b ≤ c then a ≤ c (transitivity)

3. if a ≤ b and b ≤ a then a=b

4. for all a and b, either a ≤ b or b ≤ a // any two items can be compared (makes it a total order)

In situations where three does not strictly hold then, it is possible that a and b are in some way different and both a ≤ b and b ≤ a; in this case either may come first in the sorted list. In a **stable sort** , the input order determines the sorted order in this case.

A metaphor for thinking about comparison sorts in the abstract is that someone has a set of unlabeled weights and a balance scale. Their goal is to line up the weights in order by their weight without any information except that obtained by placing two weights on the scale and seeing which one is heavier (or if they weigh the same).

The following link is helpful.

Comparison Sorting Visualizations: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

Your goal for this lab is to implement simple versions of Insertion Sort - **insertion\_sort(alist)**, Selection Sort - **selection\_sort(alist),** that will sort an array of integers and **count the number of comparisons**. Include your test cases as lists in the same file as your functions. Each function takes as input a list of integers, sorts the list counting the comparisons at the same time, **and returns the number of comparisons**. After the function completes, the " **alist**" should be sorted.

**Also include a comment with your test cases explaining why the testcases for the worst case are the worst case!**

**Lab 6b: Quicksort**

QuickSort is a "Divide and Conquer" algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of QuickSort that pick the pivot in different ways, including:

1. Always picking first element as pivot.
2. Always picking last element as pivot.
3. Always picking the middle element as pivot.
4. Picking a random element as pivot.
5. Picking a median (usually from 3 elements) as pivot.

The key process in QuickSort is partition(). The goal of the partition() function is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

The following link is helpful - Comparison Sorting Visualizations: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html


|   | **Number of QuickSort Comparisons** | **Number of QuickSort Comparisons** |
| --- | --- | --- |
| **Starting List** | pivot = first | pivot = median of 3 |
| Ordered, ascending |   |   |
| n = 100 |   |   |
| n = 200 |   |   |
| n = 400 |   |   |
| n = 800 |   |   |
| Random |   |   |
| n = 100 (average 10 runs) |   |   |
| n = 200 (average 10 runs) |   |   |
| n = 400 (average 10 runs) |   |   |
| n = 800 (average 10 runs) |   |   |
|   |   |   |
| Observed Big O() behavior, ordered with pivot = first : |
| Observed Big O() behavior, ordered with pivot = median of 3 : |
