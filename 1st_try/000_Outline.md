## 03/20/2019
Due to the work load of ME interviews, I do more easy questions these days.
### 136 Single Number:
  You may choose either less memory, or shorter run time. Hard to get both. Leetcode has a few solutions and it may worth to take a look, especially for the hash table one, and the logic relation one.
### 017 Letter Combination of a Phone Number:
  May check if others have anything faster than O(n**3)  

## 03/21/2019
### 049 Group Anagram:
  Spent a lot of time on comparing letter by letter in strings, while finally figured out that it can be easily solved by dictionary. Each dict key is the sorted string. Then output is the list of values for each key.
### 048 Rotate Image:
  Assign some value to a variable: assign the value itself or assign the memory location?
  One line to loop over lists in list
  Sometimes it is useful to calculate the first few items in hand writing and then try to find the rule or equaion for bigger set.
  Another solution uses zip command in Python. Should learn about how to use it.

## 03/22/2019
Did an interview with Facebook in hardware development

## 03/23/3019
No update. Did some heavy house work.

## 03/24/2019
### 070 Climbing Stairs
  It is a fibonacci list. Like what I found in 048, it is useful to calculate the first few items and find the rules.
  Later, it may be useful to try dynamic programming

## 03/25/2019
Started CC189 study
### 961 N-Repeated Element in Size 2N Array
  Not so challenge. a easy question. Easier than what the question describes.

## 03/27/2019
### 066 Plus One
  An easy one. Not much to add.

## 03/30/2019
### 021 Merge Two Sorted Lists
  Useful to understand linked list
  Could do it shorter, see the 5 line python solution in leetcode.

## 03/31/2019
### 028 Implement strStr()
  Another easy question. Pay attention to the concer cases.

## 04/08/2019
### 141 Linked List Cycle
  Another easy question
### 023 Merge k Sorted Lists
  A good practice for linked list address allocation and exchange.
  Sometimes it may be helpful to jump out of a fixed frame. For example, list in this problem will be very helpful.
### 024 Swap Nodes in Pairs
  A good practice for linked list address allocation and exchange. Should repeat it and do some similar ones soon.

## 04/22/2019
### 127 Word Ladder
  BFS question. Needs to pay attention to the defaultdict function.
  Think further about which way is more efficient, when facing with some tedious logic.

## 05/04/2019
### 043 Multiply Strings
  A strange problem. Multiply digit by digit and add them up.

## 05/05/2019
### 034	Find First and Last Position of Element in Sorted Array
  Binary search. Try to be more proficient in binary search
### 038 Count and Say
  Normal string problem. Be more careful with boundary conditions
### 046 Permutations
  Similar to 017. It is a backtracking problem. I did not use recursive way, but rescursion should definitely be practised.

## 05/10/2019
### 033 Search in Rotated Sorted Array
  Form a way to do binary search and repeat the way.
  Duplicate the data then do operate. Using pointers and movers is not so efficient.

## 05/11/2019
  Try to understand shallow copy and deep copy!!
  Try to understand shallow copy and deep copy!!
  Try to understand shallow copy and deep copy!!
### 039 Combination Sum
  Backtracking. Very typical question. Should try to deeply understand the circles. Make the circles and loops clear.

## 07/30/2019
### 310 Minimum Height Trees
To be learning the better idea.
### 417 Pacific Atlantic Water Flow
It is BFS. Sometimes if it is hard to solve a problem in normal order, reserve it and think it from backend.


## 08/02/2019
### 079 Word search
Backtracking
There is one way to mark a item you visited: create a set or create a visited list
There is another way: visit it, then change the value, so that later comers cannot find it -- change it back in time if it is still needed in the future.

## 08/03/2019
1st round done with BFS. More harder problems to go.

## 08/04/2019
Start of Greedy algorithm
### 435 Non-overlapping interval
Sort by end so that early item does not impact later ones

### 452 Minimum number of Arrows to burst balloons
Almost the same as 435. As far as it does not go exceed end point, items can be treated the same way.

## 08/05/2019
### 714 Best Time to buy and sell stock with transaction fee
### 309 Best Time to buy and sell stock with cooldown
These stock problems are really a lot of fun. Make clear the dynamic programming in status of each node.
